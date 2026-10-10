# 批量生成与逐条复现命令

在本仓库根目录执行。以下使用昨天 quickstart.py 的请求和任务轮询函数。

固定参数：model=gpt-image-2；resolution=1k；n=1。每条比例从 data/recipes.json 读取，不使用 quickstart 原来的固定 1:1。

## 先检查请求，不扣费

~~~powershell
py examples/generate_gallery.py --dry-run --workers 14 --rpm 240
~~~

## 并发生成全部案例

~~~powershell
py examples/generate_gallery.py --env-file "你的环境文件完整路径" --workers 14 --rpm 240 --interval 8 --max-wait 900
~~~

14 个工作线程、全局 API 请求上限 240 RPM；每个未完成任务约每 8 秒查询一次。请求和查询共同计入限流。下载结果不计入 ToAPIs API 请求限流。

脚本读取 TOAPIS_API_KEY 和可选的 TOAPIS_BASE_URL。保留真实环境文件在项目外，上传目录只含 .env.example。

## 只跑一个案例

~~~powershell
py examples/generate_gallery.py --id 01-product-hero-perfume --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

可重复传入 --id 选择多个案例。若这些任务已经完成，脚本会跳过现有结果；如果已有任务 ID 则继续查询，不重新提交。想重新生图时，请复制项目到新的本地工作目录、保留提示词但不复制 data/runs 和 assets 中的旧结果，避免误覆盖已发布图集。

提交超时且没有确认任务 ID 时，脚本记录 submission_unconfirmed 并停止该案例的新提交。先从后台找回任务 ID，再人工核对记录；不要直接删除记录盲目重跑。

## 14 条逐条命令

### Product Hero Perfume · 1:1 · 1K

~~~powershell
py examples/generate_gallery.py --id 01-product-hero-perfume --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/01-product-hero-perfume.json

### Cinematic Street Rain · 16:9 · 1K

~~~powershell
py examples/generate_gallery.py --id 03-cinematic-street-rain --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/03-cinematic-street-rain.json

### Food Overhead Ramen · 4:3 · 1K

~~~powershell
py examples/generate_gallery.py --id 02-food-overhead-ramen --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/02-food-overhead-ramen.json

### Architectural Dusk · 16:9 · 1K

~~~powershell
py examples/generate_gallery.py --id 04-architectural-dusk --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/04-architectural-dusk.json

### Illustration Layered Paper · 1:1 · 1K

~~~powershell
py examples/generate_gallery.py --id 06-illustration-layered-paper --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/06-illustration-layered-paper.json

### Fashion Editorial Studio · 3:4 · 1K

~~~powershell
py examples/generate_gallery.py --id 05-fashion-editorial-studio --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/05-fashion-editorial-studio.json

### Macro Botanical Detail · 3:2 · 1K

~~~powershell
py examples/generate_gallery.py --id 08-macro-botanical-detail --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/08-macro-botanical-detail.json

### Infographic Dashboard · 16:9 · 1K

~~~powershell
py examples/generate_gallery.py --id 07-infographic-dashboard --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/07-infographic-dashboard.json

### Product Cosmetics Duo · 1:1 · 1K

~~~powershell
py examples/generate_gallery.py --id 03-product-cosmetics-duo --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/03-product-cosmetics-duo.json

### Cyberpunk Motorbike · 16:9 · 1K

~~~powershell
py examples/generate_gallery.py --id 01-cyberpunk-motorbike --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/01-cyberpunk-motorbike.json

### Mythic Creature Concept · 3:2 · 1K

~~~powershell
py examples/generate_gallery.py --id 02-mythic-creature-concept --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/02-mythic-creature-concept.json

### Retro Poster Travel · 3:4 · 1K

~~~powershell
py examples/generate_gallery.py --id 04-retro-poster-travel --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/04-retro-poster-travel.json

### Gourmet Dessert · 4:3 · 1K

~~~powershell
py examples/generate_gallery.py --id 05-gourmet-dessert --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/05-gourmet-dessert.json

### Fantasy City Aerial · 16:9 · 1K

~~~powershell
py examples/generate_gallery.py --id 06-fantasy-city-aerial --env-file "你的环境文件完整路径" --workers 1 --rpm 240
~~~

完整请求：requests/06-fantasy-city-aerial.json

完整提示词和对应图片见 PROMPTS.md。机器可读参数及来源见 data/recipes.json。
