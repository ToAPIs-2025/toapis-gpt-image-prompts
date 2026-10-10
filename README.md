# GPT Image 2 Prompts — ToAPIs

14 adapted prompt recipes with real outputs generated through ToAPIs, covering product photography, cinematic scenes, food, architecture, illustration, portraits, macro photography and concept art.

**All images: gpt-image-2 · 1K resolution tier · original requested aspect ratios.**

[Get an API key](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_top_key) · [Current pricing](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_pricing) · [Quickstart](https://github.com/ToAPIs-2025/toapis-quickstart) · [简体中文](README_zh-CN.md)

## Gallery

<table>
<tr>
<td width="33%" valign="top"><a href="assets/01-product-hero-perfume.png"><img src="assets/01-product-hero-perfume.png" width="300" alt="Product Hero Perfume"></a><br><b>Product Hero Perfume</b><br>1:1 · 1K</td>
<td width="33%" valign="top"><a href="assets/03-cinematic-street-rain.png"><img src="assets/03-cinematic-street-rain.png" width="300" alt="Cinematic Street Rain"></a><br><b>Cinematic Street Rain</b><br>16:9 · 1K</td>
<td width="33%" valign="top"><a href="assets/02-food-overhead-ramen.png"><img src="assets/02-food-overhead-ramen.png" width="300" alt="Food Overhead Ramen"></a><br><b>Food Overhead Ramen</b><br>4:3 · 1K</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/04-architectural-dusk.png"><img src="assets/04-architectural-dusk.png" width="300" alt="Architectural Dusk"></a><br><b>Architectural Dusk</b><br>16:9 · 1K</td>
<td width="33%" valign="top"><a href="assets/06-illustration-layered-paper.png"><img src="assets/06-illustration-layered-paper.png" width="300" alt="Illustration Layered Paper"></a><br><b>Illustration Layered Paper</b><br>1:1 · 1K</td>
<td width="33%" valign="top"><a href="assets/05-fashion-editorial-studio.png"><img src="assets/05-fashion-editorial-studio.png" width="300" alt="Fashion Editorial Studio"></a><br><b>Fashion Editorial Studio</b><br>3:4 · 1K</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/08-macro-botanical-detail.png"><img src="assets/08-macro-botanical-detail.png" width="300" alt="Macro Botanical Detail"></a><br><b>Macro Botanical Detail</b><br>3:2 · 1K</td>
<td width="33%" valign="top"><a href="assets/07-infographic-dashboard.png"><img src="assets/07-infographic-dashboard.png" width="300" alt="Infographic Dashboard"></a><br><b>Infographic Dashboard</b><br>16:9 · 1K</td>
<td width="33%" valign="top"><a href="assets/03-product-cosmetics-duo.png"><img src="assets/03-product-cosmetics-duo.png" width="300" alt="Product Cosmetics Duo"></a><br><b>Product Cosmetics Duo</b><br>1:1 · 1K</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/01-cyberpunk-motorbike.png"><img src="assets/01-cyberpunk-motorbike.png" width="300" alt="Cyberpunk Motorbike"></a><br><b>Cyberpunk Motorbike</b><br>16:9 · 1K</td>
<td width="33%" valign="top"><a href="assets/02-mythic-creature-concept.png"><img src="assets/02-mythic-creature-concept.png" width="300" alt="Mythic Creature Concept"></a><br><b>Mythic Creature Concept</b><br>3:2 · 1K</td>
<td width="33%" valign="top"><a href="assets/04-retro-poster-travel.png"><img src="assets/04-retro-poster-travel.png" width="300" alt="Retro Poster Travel"></a><br><b>Retro Poster Travel</b><br>3:4 · 1K</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/05-gourmet-dessert.png"><img src="assets/05-gourmet-dessert.png" width="300" alt="Gourmet Dessert"></a><br><b>Gourmet Dessert</b><br>4:3 · 1K</td>
<td width="33%" valign="top"><a href="assets/06-fantasy-city-aerial.png"><img src="assets/06-fantasy-city-aerial.png" width="300" alt="Fantasy City Aerial"></a><br><b>Fantasy City Aerial</b><br>16:9 · 1K</td>
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
