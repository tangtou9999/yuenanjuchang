# Grok 正式群聊渲染器迁移（2026-11-23）

## 已完成

- 在独立分支 `feature/grok-chat-final-20261123` 中保留旧 `main` 程序，尚未切换生产。
- 从 Grok 当天上传的正式源码包中筛选出 49 个文件，已实际提交到 `grok-migration/vn_theater_source_safe_20261123.zip`（977,386 字节）。
- 为避免在 GitHub 公共仓库发布不必要的素材，已排除字体文件、历史备份与测试 MP3。归档文件经 ZIP 完整性测试通过。
- 旧程序用 Node.js＋Playwright；新正式程序采用 Python＋FFmpeg、faster-whisper，与旧程序不同，不应直接覆盖。

## 尚未完成

- 代码目前作为 ZIP 已上传，**还没解包为仓库中可直接执行的目录**，所以 GitHub Actions 还不能使用这个正式程序。
- 15 人头像（83.8 MB）、BGM（28.9 MB）、字体未上传到公开仓库，仍在用户的 Google Drive 原素材区。
- 尚未在 GitHub Actions 环境完成单集渲染测试，更没有实现日更三集、自动配音、自动质检或移动端成品下载页。

## 原始程序与接口

正式入口为 `run_episode.py`，需要 Python 3.13、FFmpeg、`pip install -r requirements.txt`。示例：

```sh
python run_episode.py incoming/R03_render.json incoming/R03_audio.mp3 \\
  --style chat_final --no-cover-hold --no-endcard --no-cover --outdir output/R03
```

## 后续迁移要求

1. 将 ZIP 安全解压为新目录，不修改旧 `main` 代码。
2. 头像/音乐/字体使用有授权的私有素材渠道，并先核查素材的公开分发许可。
3. 在 GitHub Actions 上单集测试 R03：画面、人物、声音、时长、字幕、iPhone 兼容编码均须实际验证。
4. 只有单集完全通过后，再测试一次连续三集、定时运行、失败重试、限额与超时处理。
5. GitHub 仓库保持无真实密钥与敏感个人素材；任何收费或自动公开分发先取得用户同意。
