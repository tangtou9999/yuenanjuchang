# 《越南语趣味大剧场》｜Grok 15人群聊正式渲染器迁移

## 当前进度（2026-11-24）

- ✅ 已从 Grok 正式运行版本提取源码、修复代码并上传到独立分支 `feature/grok-chat-final-20261123`。
- ✅ GitHub Actions 已在 Ubuntu 24.04 + Python 3.13 上真正跑通 **12项自动测试**，运行记录： https://github.com/tangtou9999/yuenanjuchang/actions/runs/45228950236
- ✅ 修复15人版聊天方向、默认自己角色、可配置个人角色、每集时间、Z系列编号；增加音频与JSON同版本匹配与防止Base64假格式检查。
- ✅ 字体兼容修复；未提供中文谐音时不擅自编造。
- ✅ 已添加独立工作流 `.github/workflows/grok-chat-pipeline.yml`：受控读取Google Drive、运行Whisper/FFmpeg、格式校验、回传云盘（配置完整后才可运行）。
- ⚠️ **目前仅完成代码和自动测试。GitHub还未实测全长MP4渲染＋Google Drive回传。** 不要宣称自动生产已经上线。
- ⚠️ **暂未启用每天3集定时任务**；务必先通过单集真实渲染和回传测试，再验证连续3集。
- 🔒 **原 `main` 分支旧程序保持原样。Z002现有MP3、JSON、测试视频保持原样，不重渲、不覆盖。**

## 源码文件

- 原GroK源码：`grok-migration/vn_theater_source_safe_20261123.zip`（历史导入保留）
- **修正版源码**：`grok-migration/vn_theater_renderer_fixed_20261124.zip`（包含Python源码、测试、Drive接口，不含私有头像和BGM）
- GitHub工作流：`.github/workflows/grok-chat-pipeline.yml`
- 依赖清单：`grok-migration/requirements-actions.txt`

## Gemini→Grok 的JSON数据约定

- 必须有 `episode_code`、`total_audio_duration_sec`、`millisecond_timeline`、最新15人角色编号/姓名。
- 每个成片必须匹配**同集号、同版本**的MP3和JSON，不因上传日期晚就混用不同版本。
- 可选 `self_character` / `self_name`：指定群聊右边“自己”的角色；默认唐哥；新版无唐哥时群聊人物都按左侧显示。
- 可选 `chat_start_time`：`HH:MM` 格式；未提供时以集号稳定生成**虚构**聊天时间，每集不再固定20:49。
- `homophone` 为可选独立字段；**为空就不显示谐音，不从中文意思反推读音**。Gemini负责提供及核查、ChatGPT负责审稿、渲染程序负责显示，不改Z002。

## 下一阶段：Google Drive独立访问（尚未接通）

GitHub Actions无法直接继承 ChatGPT 的 Google Drive 登录，需要单独、安全的Google Drive账号授权，且应仅有指定输入、资产和输出目录访问权限。工作流预留以下 GitHub Actions Secrets：

- `GOOGLE_DRIVE_SA_JSON`：独立服务账号的JSON凭证（不得提交到仓库）
- `VN_INPUT_FOLDER_ID`：Gemini配音素材的Drive文件夹ID
- `VN_OUTPUT_FOLDER_ID`：GitHub独立渲染测试视频输出Drive文件夹ID
- `VN_AVATARS_ZIP_ID`：存放在私人Drive的15人头像ZIP文件ID
- `VN_BGM_ZIP_ID`：存放在私人Drive的音效/背景音乐ZIP文件ID

必须把上述文件和必要目录授权给服务账号，才能完成真实自动下载/上传测试。未经授权，不读取或公开头像、音乐、凭据；服务账号不能被放在仓库源码、issue、日志或公开网页中。

当前工作流仍在功能分支上。GitHub `workflow_dispatch` 人工入口正式可用前，需要经审查把新工作流合入默认分支；**不把尚未执行的工作流当作已跑通的自动化**。

## 下一步验收标准

1. 在GitHub真正读取一集新MP3＋JSON与所需私有素材。
2. 在GitHub执行Whisper时间轴＋完整FFmpeg渲染，检查1080×1920/H.264/AAC和逐帧人物/字幕。
3. 把新MP4自动上传到指定Drive测试目录，确认链接可访问。
4. 一次连续生产3集并验证去重、失败重试、配额与耗时。
5. 经单集和三集实测均成功后，才启用每日定时生产；发布仍由用户自行决定。
