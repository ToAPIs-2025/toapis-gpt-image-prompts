# GPT Image 2 Prompts — ToAPIs


<!-- TOAPIS-MODELS-20261020 -->
## Model support and prices · 2026-10-20

Added standalone API presets: 31 image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid calls while pricing is unavailable. Native provider/UI/import/render acceptance remains as documented in the original guide below.

| Image model / tested preset | Current preset quote / image | Historical example amount / image | Fee evidence |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | Billing log, phase unknown |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | Current-key quote unavailable | **$0.005272/image**<br><sub>Token-metered; current $/M unavailable. This sample is not a fixed image tariff.</sub> | Task receipt settled |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | Billing log, phase unknown |
| qwen-image-3.0<br><sub>1K</sub> | Current-key quote unavailable | **$0.021/image** | Billing log, phase unknown |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | Billing log, phase unknown |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | Billing log, phase unknown |

| Video model | Preset / input | Settled clip charge | File duration | Case USD/s, ascending |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / text-to-video | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>Pricing tariff: $0.025/s</sub> |
| seedance-2-mini | 4s / 480p / first-frame | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>Pricing tariff: $3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / text-to-video | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>Pricing tariff: $5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / text-to-video | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>Pricing tariff: $0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / text-to-video | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>Pricing tariff: $0.064/s</sub> |
| seedance-2 | 4s / 480p / first-frame | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>Pricing tariff: $6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / text-to-video | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>Pricing tariff: $0.08/s</sub> |
| seedance-2-5 | 4s / 480p / text-to-video | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>Pricing tariff: $10/M total tokens</sub> |

Pricing checked 2026-10-20. Image examples are dated 2026-10-17; video examples 2026-10-20. Tables sort by example amount or case USD/s. Presets and input modes differ; this is not a matched-settings quality ranking. Unknown-phase image logs are not confirmed final net settlements. Current quotes and historical amounts are separate. Video charges are billing=settled; case USD/s divides charge by actual file duration, never processing time. Token tariffs appear in small text and do not imply a fixed per-second price.

gpt-image-2(VIP) starts at $0.0019/image; this low/1K preset is $0.0019/image. The standalone sampler has 31 historically successful image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid submission until an exact price is available.

[Local sampler](toapis-models/README.md) · [Full price table](PRICING.md) · [Original media and fee evidence](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/model-support-2026-10-20)

Original project examples, historical charges and integration instructions follow. Historical amounts are not rewritten as today’s quotes.

<!-- /TOAPIS-MODELS-20261020 -->

14 adapted prompt recipes with real outputs generated through ToAPIs, covering product photography, cinematic scenes, food, architecture, illustration, portraits, macro photography and concept art.

**All images: gpt-image-2 · 1K resolution tier · original requested aspect ratios.**

[Get an API key](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_top_key) · [Current pricing](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_pricing) · [Quickstart](https://github.com/ToAPIs-2025/toapis-quickstart) · [简体中文](README_zh-CN.md)

## Image generation pricing

**Each image in this gallery costs only $0.015 at the listed ToAPIs rate (gpt-image-2 · 1K).** At this unit price, 14 images total $0.21.

| Model | 1K | 2K | 4K |
| --- | --- | --- | --- |
| `gpt-image-2` | $0.015 | $0.020 | $0.025 |
| `gpt-image-2.5-flare` | $0.0225 | $0.030 | $0.0375 |
| `gpt-image-2.5-sunburst` | $0.0225 | $0.030 | $0.0375 |

Prices are in USD per image, with one image per request. `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst` have identical pricing. All images in this gallery use `gpt-image-2`; the 2.5 models are listed for comparison.

Prices supplied by the maintainer from the ToAPIs price list, updated 2026-10-10. These are listed rates; account Usage Logs determine billed charges. See [current ToAPIs pricing](https://toapis.com/en/pricing) for updates.

## Gallery

<table>
<tr>
<td width="33%" valign="top"><a href="assets/01-product-hero-perfume.png"><img src="assets/01-product-hero-perfume.png" width="300" alt="Product Hero Perfume"></a><br><b>Product Hero Perfume</b><br>1:1 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/03-cinematic-street-rain.png"><img src="assets/03-cinematic-street-rain.png" width="300" alt="Cinematic Street Rain"></a><br><b>Cinematic Street Rain</b><br>16:9 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/02-food-overhead-ramen.png"><img src="assets/02-food-overhead-ramen.png" width="300" alt="Food Overhead Ramen"></a><br><b>Food Overhead Ramen</b><br>4:3 · 1K · $0.015/image</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/04-architectural-dusk.png"><img src="assets/04-architectural-dusk.png" width="300" alt="Architectural Dusk"></a><br><b>Architectural Dusk</b><br>16:9 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/06-illustration-layered-paper.png"><img src="assets/06-illustration-layered-paper.png" width="300" alt="Illustration Layered Paper"></a><br><b>Illustration Layered Paper</b><br>1:1 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/05-fashion-editorial-studio.png"><img src="assets/05-fashion-editorial-studio.png" width="300" alt="Fashion Editorial Studio"></a><br><b>Fashion Editorial Studio</b><br>3:4 · 1K · $0.015/image</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/08-macro-botanical-detail.png"><img src="assets/08-macro-botanical-detail.png" width="300" alt="Macro Botanical Detail"></a><br><b>Macro Botanical Detail</b><br>3:2 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/07-infographic-dashboard.png"><img src="assets/07-infographic-dashboard.png" width="300" alt="Infographic Dashboard"></a><br><b>Infographic Dashboard</b><br>16:9 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/03-product-cosmetics-duo.png"><img src="assets/03-product-cosmetics-duo.png" width="300" alt="Product Cosmetics Duo"></a><br><b>Product Cosmetics Duo</b><br>1:1 · 1K · $0.015/image</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/01-cyberpunk-motorbike.png"><img src="assets/01-cyberpunk-motorbike.png" width="300" alt="Cyberpunk Motorbike"></a><br><b>Cyberpunk Motorbike</b><br>16:9 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/02-mythic-creature-concept.png"><img src="assets/02-mythic-creature-concept.png" width="300" alt="Mythic Creature Concept"></a><br><b>Mythic Creature Concept</b><br>3:2 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/04-retro-poster-travel.png"><img src="assets/04-retro-poster-travel.png" width="300" alt="Retro Poster Travel"></a><br><b>Retro Poster Travel</b><br>3:4 · 1K · $0.015/image</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/05-gourmet-dessert.png"><img src="assets/05-gourmet-dessert.png" width="300" alt="Gourmet Dessert"></a><br><b>Gourmet Dessert</b><br>4:3 · 1K · $0.015/image</td>
<td width="33%" valign="top"><a href="assets/06-fantasy-city-aerial.png"><img src="assets/06-fantasy-city-aerial.png" width="300" alt="Fantasy City Aerial"></a><br><b>Fantasy City Aerial</b><br>16:9 · 1K · $0.015/image</td>
</tr>
</table>

Click an image to open the original output. All images were newly generated through ToAPIs. Full prompts: [PROMPTS.md](PROMPTS.md).

## Reproduce a recipe

The included gallery wrapper reuses the existing quickstart.py request and task-polling functions. It overrides the recipe aspect ratio, fixes gpt-image-2 and 1k, and saves the returned image.

~~~bash
python examples/generate_gallery.py --id 01-product-hero-perfume --dry-run
python examples/generate_gallery.py --id 01-product-hero-perfume --env-file /path/to/private.env --workers 14 --rpm 240
~~~

Use Python 3.10 or newer; generation requires only the standard library. Windows users can use py in place of python. Set TOAPIS_API_KEY and optionally TOAPIS_BASE_URL in a private environment file outside this repository.

Without --id, the wrapper processes all 14 recipes concurrently when --workers is set. Full batch and per-recipe commands: [COMMANDS.md](COMMANDS.md). Completed outputs are skipped and known task IDs are resumed. After a submission failure without a confirmed task ID, inspect existing account tasks before resubmitting.

## Settings and actual dimensions

| Recipe | Requested ratio | Actual pixels |
| --- | --- | --- |
| Product Hero Perfume | 1:1 | 1024×1024 |
| Cinematic Street Rain | 16:9 | 1696×960 |
| Food Overhead Ramen | 4:3 | 1152×864 |
| Architectural Dusk | 16:9 | 1280×720 |
| Illustration Layered Paper | 1:1 | 1024×1024 |
| Fashion Editorial Studio | 3:4 | 864×1152 |
| Macro Botanical Detail | 3:2 | 1264×848 |
| Infographic Dashboard | 16:9 | 1280×720 |
| Product Cosmetics Duo | 1:1 | 1024×1024 |
| Cyberpunk Motorbike | 16:9 | 1376×768 |
| Mythic Creature Concept | 3:2 | 1248×832 |
| Retro Poster Travel | 3:4 | 896×1184 |
| Gourmet Dessert | 4:3 | 1200×896 |
| Fantasy City Aerial | 16:9 | 1280×720 |

1K is the API resolution tier. It does not mean every output has a maximum edge of 1024 pixels. The API returned dimensions that differ from its reference size table; requested ratios and actual pixels are both recorded. Small ratio deviations are documented in the task records. Images are preserved as returned, without cropping or upscaling.

[API reference](https://docs.toapis.com/docs/en/api-reference/images/gpt-image-2/generation) · [Machine-readable prompts and parameters](data/recipes.json)

## Generation records and costs

Sanitized records in data/runs/ include the exact request, task ID, completion timestamp, pixel dimensions and output checksum. These are individual successful examples, not a reliability benchmark.

No competitor price is presented as a ToAPIs cost. Missing cost fields remain null. Verify actual charges in your account's Usage Logs before budgeting. Model availability and pricing can change.

## Sources

Prompt text is adapted from MIT-licensed Nano Banana Pro and Grok Imagine galleries. Original topics and aspect ratios are retained; lighting, palette, materials and constraints are adjusted. All images were generated afresh with gpt-image-2.

Per-recipe source IDs and blob versions are recorded in data/recipes.json. Copyright and license notices are preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Upstream images and cost figures are not reused.

## About ToAPIs

Maintained by ToAPIs to demonstrate its image API. ToAPIs is a third-party API service; model names belong to their respective owners.

[Try a recipe through ToAPIs](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_bottom_key)

Generation timestamps: individual task records. License: [MIT](LICENSE), with upstream prompt notices preserved.
