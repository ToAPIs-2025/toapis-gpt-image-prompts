"""Generate gallery images using the existing quickstart.py functions.
Fixed model: gpt-image-2. Fixed resolution tier: 1k. Source aspect ratios.
No automatic resubmission after an ambiguous POST failure.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen
import quickstart
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[1]

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)

def load_env(path):
    if not path:
        return
    for raw in Path(path).read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:]
        if "=" not in line:
            continue
        name, value = line.split("=", 1)
        name, value = name.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        if name in ("TOAPIS_API_KEY", "TOAPIS_BASE_URL"):
            os.environ[name] = value

def suffix(data):
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith(b"\xff\xd8"):
        return ".jpg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    raise RuntimeError("Downloaded output is not a supported image")

def generate(recipe, base, key, args):
    slug = recipe["id"]
    record_path = ROOT / "data" / "runs" / (slug + ".json")
    record = json.loads(record_path.read_text(encoding="utf-8")) if record_path.exists() else {}
    if not args.dry_run and record.get("status") == "completed" and (ROOT / record.get("output_path", "_missing_")).is_file():
        print("SKIP " + slug, flush=True)
        return
    path, payload = quickstart.build_request("image", recipe["prompt"])
    payload.update(model="gpt-image-2", resolution="1k", size=recipe["request"]["size"], n=1)
    payload.pop("quality", None)
    if args.dry_run:
        print(json.dumps({"id": slug, "endpoint": base + path, "request": payload}, ensure_ascii=False), flush=True)
        return
    task_id = record.get("task_id")
    if not task_id:
        if record.get("status") == "submission_unconfirmed":
            raise RuntimeError(slug + ": inspect the account's existing tasks before another submission")
        record = {"id": slug, "request": payload, "status": "submission_unconfirmed",
                  "submitted_at": datetime.now(timezone.utc).isoformat()}
        write_json(record_path, record)
        created = quickstart.request_json("POST", base + path, key, payload)
        task_id = created.get("id") or created.get("task_id")
        if not task_id:
            raise RuntimeError("No task ID returned for " + slug)
        record.update(task_id=str(task_id), status="submitted")
        write_json(record_path, record)
        print("SUBMITTED " + slug + " " + str(task_id), flush=True)
    task = quickstart.wait_for_task(base, key, "image", str(task_id), args.interval, args.max_wait)
    result = quickstart.result_url(task)
    if not result:
        raise RuntimeError("No output URL returned for " + slug)
    if not result.startswith("https://"):
        raise RuntimeError("Expected HTTPS output URL")
    with urlopen(Request(result, headers={"User-Agent": "ToAPIs-Gallery/1.0"}), timeout=90) as response:
        image_bytes = response.read()
    output = ROOT / "assets" / (slug + suffix(image_bytes))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(image_bytes)
    record.update(status="completed", completed_at=datetime.now(timezone.utc).isoformat(),
                  output_path=output.relative_to(ROOT).as_posix(),
                  output_sha256=hashlib.sha256(image_bytes).hexdigest(),
                  actual_credits=task.get("credits_cost"), reported_cost=task.get("cost"),
                  cost_source="task_response; null means not supplied",
                  provider_model=task.get("model"))
    write_json(record_path, record)
    print("SAVED " + slug + " " + output.name, flush=True)

def install_rate_limit(rpm):
    original = quickstart.request_json
    lock = threading.Lock()
    next_slot = [0.0]
    def limited(method, url, key, payload=None):
        with lock:
            scheduled = max(time.monotonic(), next_slot[0])
            next_slot[0] = scheduled + 60.0 / rpm
        delay = scheduled - time.monotonic()
        if delay > 0:
            time.sleep(delay)
        return original(method, url, key, payload)
    quickstart.request_json = limited

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file")
    parser.add_argument("--id", action="append", help="recipe id; repeat for multiple recipes")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--rpm", type=int, default=240, help="global API request cap, at most 300")
    parser.add_argument("--interval", type=int, default=8)
    parser.add_argument("--max-wait", type=int, default=900)
    args = parser.parse_args()
    if args.interval < 1 or args.max_wait < 1:
        parser.error("interval and max-wait must be positive")
    if not 1 <= args.workers <= 14 or not 1 <= args.rpm <= 300:
        parser.error("workers must be 1..14 and rpm must be 1..300")
    load_env(args.env_file)
    base = quickstart.api_base(os.getenv("TOAPIS_BASE_URL", quickstart.DEFAULT_BASE))
    key = os.getenv("TOAPIS_API_KEY")
    if not args.dry_run and not key:
        parser.error("Set TOAPIS_API_KEY or provide --env-file; never paste a key into source code")
    recipes = json.loads((ROOT / "data" / "recipes.json").read_text(encoding="utf-8"))["recipes"]
    if args.id:
        unknown = set(args.id) - {r["id"] for r in recipes}
        if unknown:
            parser.error("Unknown recipe IDs: " + ", ".join(sorted(unknown)))
        recipes = [r for r in recipes if r["id"] in args.id]
    install_rate_limit(args.rpm)
    failures = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        pending = {pool.submit(generate, recipe, base, key, args): recipe["id"] for recipe in recipes}
        for future in as_completed(pending):
            slug = pending[future]
            try:
                future.result()
            except Exception as exc:
                failures.append(slug)
                detail = str(exc).replace(key, "[REDACTED]") if key else str(exc)
                print("FAILED " + slug + ": " + detail, flush=True)
    if failures:
        raise SystemExit("Failed recipes: " + ", ".join(failures))

if __name__ == "__main__":
    main()
