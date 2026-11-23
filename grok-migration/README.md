# 正式群聊渲染器迁移记录（2026-11-23）

**状态：准备迁移；完整源码和素材尚未上传到 GitHub。** 不要把这个分支当成可运行的渲染系统。

## 来源与文件清单
Grok 已将当前《越南语趣味大剧场》正式程序上传到项目的 Google Drive「Grok交付」文件夹：

- `vn_theater_1_code_20261123.zip`：源码，7,088,093 字节
- `vn_theater_2_avatars15_20261123.zip`：15 人头像，83,800,864 字节
- `vn_theater_3_bgm_20261123.zip`：背景音乐，28,931,595 字节
- `vn_theater_HANDOFF_交接说明_20261123.md`：详细运行说明

已核对三个 ZIP 均完整、可解压。正式渲染入口为 `run_episode.py`，依赖 Python 3.13、FFmpeg 和 `requirements.txt` 中的 CPU 包。指令样例：

```bash
python run_episode.py incoming/R03_render.json incoming/R03_audio.mp3 --style chat_final --no-cover-hold --no-endcard --no-cover --outdir output/R03
```

## 迁移安全边界

1. 旧 main 分支暂不更改。
2. **仓库当前是公开的**；未经进一步处理，不要把用户提供的角色头像原件、私有音频、未审查版权的 BGM 或任何凭证提交到公开仓库。
3. 任何缺失的 Google Drive 访问凭据只能放在 GitHub Actions Secrets；不能写入源码、工作流、提交记录或 Release。
4. 新渲染器先做单集 R03 测试，核对人物、音画时长、视频编码和字幕；稳定后再考虑每天3集。
5. 上传源码不等于配音、审核、封面生成自动化已经实现。

## 当前阻碍
当前 GitHub 连接器支持写入 UTF-8 文本，不支持直接把 Google Drive 的大 ZIP 二进制文件作为附件提交。需要一次支持二进制文件的 GitHub 上传通道，才能完成正式程序和素材的迁移。
