# GPT Image 2 提示词图集 — ToAPIs


<!-- TOAPIS-MODELS-20261020 -->
## 模型与价格更新 · 2026-10-20

新增可独立运行的31套图片请求模板、8套视频模板。当前26套图片与8套视频可匹配同Key精确价格；另5套图片缺价，默认阻止新付费调用。它们属于额外API脚本；项目原生Provider、UI、导入及完整出片的验收范围仍以下方原教程为准。

| 图片模型／实测档位 | 当前档位报价／张 | 历史案例金额／张 | 费用证据 |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | 计费日志，阶段未知 |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | 当前Key暂未返回报价 | **$0.005272/image**<br><sub>Token计费；当前$/M未返回，本例金额不是固定单张价。</sub> | 任务回执已结算 |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | 计费日志，阶段未知 |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | 计费日志，阶段未知 |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | 计费日志，阶段未知 |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | 计费日志，阶段未知 |
| qwen-image-3.0<br><sub>1K</sub> | 当前Key暂未返回报价 | **$0.021/image** | 计费日志，阶段未知 |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | 计费日志，阶段未知 |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | 计费日志，阶段未知 |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | 计费日志，阶段未知 |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | 计费日志，阶段未知 |

| 视频模型 | 档位／输入 | 本例消费 | 文件时长 | 本例每秒金额（升序） |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / 文生视频 | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>pricing底层费率：$0.025/s</sub> |
| seedance-2-mini | 4s / 480p / 首帧 | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>pricing底层费率：$3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / 文生视频 | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>pricing底层费率：$5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / 文生视频 | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>pricing底层费率：$0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / 文生视频 | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>pricing底层费率：$0.064/s</sub> |
| seedance-2 | 4s / 480p / 首帧 | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>pricing底层费率：$6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / 文生视频 | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>pricing底层费率：$0.08/s</sub> |
| seedance-2-5 | 4s / 480p / 文生视频 | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>pricing底层费率：$10/M total tokens</sub> |

报价核对：2026-10-20。图片案例日期2026-10-17；视频案例日期2026-10-20。表格按本例金额／秒金额排序，质量、分辨率和输入不同，不是同配置质量排名。图片日志的阶段未知，不能当作单任务最终净结算；当前报价与历史金额分别显示。视频金额均由billing=settled确认，$/s按实际文件时长折算，任务处理耗时不参与计算。Token模型不是固定每秒价，底层$/M只作小字补充。

gpt-image-2(VIP)通用价格为$0.0019/image起；本例low/1K为$0.0019/image。新脚本有31套历史成功图片请求模板、8套视频模板；当前26套图片与8套视频可匹配价格，另5套图片因当前Key缺价而默认阻止新付费调用。

[本仓库多模型脚本](toapis-models/README_zh-CN.md) · [完整价表](PRICING_zh-CN.md) · [原图／视频及费用证据](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/model-support-2026-10-20)

下方保留原项目历史案例、消费及集成说明；历史金额不改成今天的新报价。

<!-- /TOAPIS-MODELS-20261020 -->

14 个改写提示词及 ToAPIs 实测图片，覆盖产品摄影、电影感场景、美食、建筑、插画、人像、微距和概念设计。

**全部使用 gpt-image-2，分辨率档位严格为 1K，请求比例沿用参考案例。**

[获取 API Key](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_top_key) · [当前价格](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_pricing) · [Quick Start](https://github.com/ToAPIs-2025/toapis-quickstart) · [English](README.md)

## 生成费用与模型价格

**本图集每张图片的生成耗费仅 $0.015/张（gpt-image-2 · 1K）。** 按此单价，14 张图片合计 $0.21。

| 模型 | 1K | 2K | 4K |
| --- | --- | --- | --- |
| `gpt-image-2` | $0.015 | $0.020 | $0.025 |
| `gpt-image-2.5-flare` | $0.0225 | $0.030 | $0.0375 |
| `gpt-image-2.5-sunburst` | $0.0225 | $0.030 | $0.0375 |

价格单位为美元/张（每次请求生成 1 张）。`gpt-image-2.5-flare` 与 `gpt-image-2.5-sunburst` 同价；本图集的图片均使用 `gpt-image-2`，未使用 2.5 模型。

价格依据维护者提供的 ToAPIs 价目表，更新于 2026-10-10。以上为标价，具体账单以账户用量记录为准；最新价格见 [ToAPIs 价格页](https://toapis.com/en/pricing)。

## 图集

<table>
<tr>
<td width="33%" valign="top"><a href="assets/01-product-hero-perfume.png"><img src="assets/01-product-hero-perfume.png" width="300" alt="Product Hero Perfume"></a><br><b>Product Hero Perfume</b><br>1:1 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/03-cinematic-street-rain.png"><img src="assets/03-cinematic-street-rain.png" width="300" alt="Cinematic Street Rain"></a><br><b>Cinematic Street Rain</b><br>16:9 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/02-food-overhead-ramen.png"><img src="assets/02-food-overhead-ramen.png" width="300" alt="Food Overhead Ramen"></a><br><b>Food Overhead Ramen</b><br>4:3 · 1K · $0.015/张</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/04-architectural-dusk.png"><img src="assets/04-architectural-dusk.png" width="300" alt="Architectural Dusk"></a><br><b>Architectural Dusk</b><br>16:9 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/06-illustration-layered-paper.png"><img src="assets/06-illustration-layered-paper.png" width="300" alt="Illustration Layered Paper"></a><br><b>Illustration Layered Paper</b><br>1:1 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/05-fashion-editorial-studio.png"><img src="assets/05-fashion-editorial-studio.png" width="300" alt="Fashion Editorial Studio"></a><br><b>Fashion Editorial Studio</b><br>3:4 · 1K · $0.015/张</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/08-macro-botanical-detail.png"><img src="assets/08-macro-botanical-detail.png" width="300" alt="Macro Botanical Detail"></a><br><b>Macro Botanical Detail</b><br>3:2 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/07-infographic-dashboard.png"><img src="assets/07-infographic-dashboard.png" width="300" alt="Infographic Dashboard"></a><br><b>Infographic Dashboard</b><br>16:9 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/03-product-cosmetics-duo.png"><img src="assets/03-product-cosmetics-duo.png" width="300" alt="Product Cosmetics Duo"></a><br><b>Product Cosmetics Duo</b><br>1:1 · 1K · $0.015/张</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/01-cyberpunk-motorbike.png"><img src="assets/01-cyberpunk-motorbike.png" width="300" alt="Cyberpunk Motorbike"></a><br><b>Cyberpunk Motorbike</b><br>16:9 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/02-mythic-creature-concept.png"><img src="assets/02-mythic-creature-concept.png" width="300" alt="Mythic Creature Concept"></a><br><b>Mythic Creature Concept</b><br>3:2 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/04-retro-poster-travel.png"><img src="assets/04-retro-poster-travel.png" width="300" alt="Retro Poster Travel"></a><br><b>Retro Poster Travel</b><br>3:4 · 1K · $0.015/张</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="assets/05-gourmet-dessert.png"><img src="assets/05-gourmet-dessert.png" width="300" alt="Gourmet Dessert"></a><br><b>Gourmet Dessert</b><br>4:3 · 1K · $0.015/张</td>
<td width="33%" valign="top"><a href="assets/06-fantasy-city-aerial.png"><img src="assets/06-fantasy-city-aerial.png" width="300" alt="Fantasy City Aerial"></a><br><b>Fantasy City Aerial</b><br>16:9 · 1K · $0.015/张</td>
</tr>
</table>

点击图片可打开原图。所有素材通过 ToAPIs 重新生成，没有复制参考仓库图片。完整提示词见 [PROMPTS.md](PROMPTS.md)。

## 复现案例

生成工具复用已有 quickstart.py 的请求与轮询函数，补上各案例的比例和图片保存。

~~~bash
python examples/generate_gallery.py --id 01-product-hero-perfume --dry-run
python examples/generate_gallery.py --id 01-product-hero-perfume --env-file /path/to/private.env --workers 14 --rpm 240
~~~

需要 Python 3.10 或以上，生图只使用标准库。Windows 可以用 py 替代 python。环境文件中配置 TOAPIS_API_KEY 和可选的 TOAPIS_BASE_URL，真实环境文件放在仓库外。

不传 --id 会处理全部案例，--workers 14 可并发执行；完整批量与逐条命令见 [COMMANDS.md](COMMANDS.md)。已完成的输出跳过，已确认任务 ID 的请求继续查询；提交中断但未拿到任务 ID 时，先检查后台任务，避免重复提交。

## 参数与实际尺寸

| 案例 | 请求比例 | 实际像素 |
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

模型固定 gpt-image-2，resolution 字段固定 1k，n 为 1。1K 是分辨率档位，不表示所有比例的最长边都只有 1024 像素。接口返回尺寸与文档对照表有差异，表格分别记录请求比例和实际像素；微小比例偏差记录在任务文件中。保留 API 原图，不裁切、不放大。

[接口文档](https://docs.toapis.com/docs/en/api-reference/images/gpt-image-2/generation) · [完整提示词与参数](data/recipes.json)

## 生成记录与费用

data/runs/ 保存脱敏请求、任务 ID、完成时间、实际像素和图片校验值。展示的是单次成功生成案例，不是稳定性测试。

没有沿用竞品费用；接口没提供费用时保留 null。实际扣费以同账户 Usage Logs 为准，预算前查看当前价格。

## 来源与改写

提示词改写自两个 MIT 许可的参考图集，保留题材与比例，调整光线、配色、材质或约束。全部图片通过 ToAPIs 使用 gpt-image-2 重新生成。

每条提示词的来源仓库、原案例 ID 和源文件版本保存在 data/recipes.json。版权及许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 关于 ToAPIs

本项目由 ToAPIs 维护，用于展示其图像 API。模型名称属于对应权利方，ToAPIs 是第三方 API 服务。

[用 ToAPIs 生成图片](https://toapis.com/dashboard/tokens?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_gpt_image_prompts&utm_content=readme_bottom_key)

实测时间见任务记录。许可证：[MIT](LICENSE)，并保留上游提示词许可。
