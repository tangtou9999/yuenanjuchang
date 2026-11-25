# R03 / EP05 2026-11-25 渲染修复可复现说明

## 输入与安全边界
- 代码基线：`grok-migration/vn_theater_renderer_fixed_20261124.zip`，解开 `vn_theater/`。
- 15人素材从用户私人Drive `Grok交付_20261121/vn_theater_2_avatars15_20261123.zip` 解包到 `vn_theater/assets/avatars`；音乐压缩包 `vn_theater_3_bgm_20261123.zip` 放到 `vn_theater/assets/bgm`，不得提交头像、原音轨或密钥到公开GitHub。
- 03：`03｜R03` 文件夹中的 `01_配音_Gemini_20261123.mp3` + `02_时间轴JSON_Gemini_20261123.json`。
- 06：`06｜EP05` 文件夹的 **`01_新版配音_Gemini_20261122.mp3`** + **`02_新版时间轴JSON_Gemini_20261122.json`**；严禁混入旧MP4 89.328秒源。
- 输出必须到新文件夹 / v02 文件名，原件禁止覆盖，另保留已发布其他集。

## 为避免大单词卡遮挡聊天

本轮03/06本地渲染专用的临时源码副本，在 `styles/chat_final.py` 的 `draw_vocab_card(im,state,t)` 函数最开始直接 `return`，**仅影响了本地重渲出的03/06候选片，不是对GitHub zip进行了全局修改**。

未来更可控的建议改法（已做语法检查，但还未在GitHub Actions实测）：

```python
def draw_vocab_card(im, state, t):
    if (state.get("mix") or {}).get("disable_full_vocab_popup", False):
        return
    words = state.get("words") or []
    # existing rest of method unchanged...
```

使用时只在需修正的本集 `EP05_script.mix.json` / `R03_script.mix.json` 设置 `"disable_full_vocab_popup": true`，**不要让已发布作品显示变化**。保留 `word_phase/board_layer` 顶部词板及语音气泡内越语高亮；可能还有小型“划重点”卡须人工审片。

## 具体渲染参数
- JSON与MP3导入：`python run_episode.py in.json in.mp3 --no-align --style chat_final --no-cover --no-endcard --no-cover-hold --outdir 新目录`。
- 本轮本地环境缺 `faster-whisper`，所以用了 `--no-align`：**逐字字幕Karaoke按照JSON镜头内均匀字符时间占位，并未跑Whisper强制校准**。不能拿该参数当以后默认高质量方案，后继AI应在有模型/权限的执行环境做真正逐字同步。
- 03另从原MP3用16kHz 50ms窗口计算30fps声音RMS，写到 `R03_script.align.json` 的 `rms` 列表，让头像按声音变化；06本轮未注入RMS。
- 在完整视频重封装前，03/06都使用 `ffmpeg` `showwaves` 在底部输入区空白位置合成154×42的动态小声音波形，声音仍保留原始人声+BGM/SFX，编码H264 Main/AAC；这是**显示音频正在播的视觉指示**，不等于字幕已精确对齐。
- 产物（可直接核实）：
  - [03 v02候选版](https://drive.google.com/file/d/1vNDnAksqSWg8J6OmyNks7JHU92A5SuAl/view)（42.467s）
  - [06 v02候选版](https://drive.google.com/file/d/1YVcZreKBlUMOkVM03CAqbm2P9Ih12cWu/view)（88.032s）

## 质量验证（实际运行的自动程序）
`python grok-migration/qa_video.py --video clip.mp4 --audio source.mp3 --json source.json --out qa.json`

- 03/06：ffmpeg整片可解码，尺寸1080×1920，H264 Main、30fps、AAC；视频时长与原MP3一致；音频抽样相关性高，未检测到黑屏。
- 仍有近似静止窗口（聊天语音一条多秒时画面保持，但状态波纹会动），属于需主观确认的潜在观感问题。
- 全部人声的自然度、卡壳/口吃、越语声调、每句字幕都**尚未通过人耳逐句人工终验**。视频上传成品区的名称故带“待终验”，不可宣称已批准发布。
- 08尚无v02配音，见 [当前任务首页](./CURRENT_STATUS.md) 与其Drive v02补录稿。

**交接规范：** 先读 [CURRENT_STATUS.md](./CURRENT_STATUS.md)，再按 [VIDEO_QA_CHECKLIST.md](./VIDEO_QA_CHECKLIST.md) 全片验收；更新当前状态和[AI_HANDOFF.md](./AI_HANDOFF.md)日志。
