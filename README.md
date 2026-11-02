# 越南语小剧场 · 视频工厂

在 GitHub 云端自动渲染视频，不占手机、不花 AI token。

## 怎么出一条视频（点三下）
1. 打开仓库的 **Actions** 页面 → 左边选 **渲染视频** → 点右边 **Run workflow**。
2. 填：
   - `page`：`pages/kinetic.html#A`（口播动效，A=赛博霓虹，B=黄黑大字报）或 `pages/classroom.html`
   - `name`：成品名字
   - `audio`：要合进去的音频路径，留空就是无声
3. 等几分钟，到仓库右侧 **Releases** 里点开最新一条，下载 mp4。

## 目录
- `pages/`：画面页面（浏览器里按时间画每一帧）
- `tools/render.js`：逐帧截图 + ffmpeg 合成
- `.github/workflows/render.yml`：云端运行流程

## 以后要加
- Gemini 配音自动生成（密钥只放在 Settings → Secrets and variables → Actions，名字叫 `GEMINI_API_KEY`，不要写进代码）
- 按配置批量出片、定时运行
