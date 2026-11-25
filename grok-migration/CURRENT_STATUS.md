# 【最新状态｜先读这页】越南语趣味大剧场｜2026-11-25 实际施工结果

> **接手本项目的 AI：先读本页，再读 [VIDEO_QA_CHECKLIST.md](./VIDEO_QA_CHECKLIST.md)，最后需要细节再读 [AI_HANDOFF.md](./AI_HANDOFF.md)。** 本页最新；历史日志中“尚未开工/仍在渲染”的说法已过期。每次完成新工作必须更新本页，否则视为未交接。

## 2026-11-25 22:00｜UI v03 实际修改与预览（最新）

- **用户新指示：08 暂时不换、不重做。** 03和06仍是尚未发布待终验的作品；其他已发布作品仍禁止修改。此前08“待补配音”的任务在新指示后应标为**暂停**，不要擅自推进。
- 用户提供的手机照片指出旧UI问题：群名“肖雨晴的越南语学习群(15)”不妥、品牌标题太低与口号拥挤、右侧戏剧插画丑、讲话头像只抖不放大、大型词卡干扰聊天、越语下方错误重复了括号中的中文翻译。
- **已完成的UI引擎改动（真实源码，不只是效果图）**：`import_voiceapp.py`、`render.py`、`styles/chat_final.py`：群名统一`越南语学习交流群`；国旗+品牌标题上移并排版，口号分行；右侧替换原创3D舞台图片；讲话头像真实放大最多约30%；黑板单词先在黑板上缘放大呈现，停留0.6秒，再约1.15秒平滑缩小归位；移除重复“划重点”大卡、整屏叮咚字效；越语下方仅展示已审核JSON `homophone` 谐音，括号中文释义保留在正文；若源JSON未写谐音就不显示、不自编。
- **实际测试**：使用尚未发布的EP05新MP3+JSON做了1080×1920真实静帧和3秒30fps H264/AAC动画片段，`python -m unittest discover -s tests -q` **17项通过**；这只是UI和短片测试，**未完成03/06全长重渲及全片验收，未发布。**
- 实际成果：[新UI完整截图](https://drive.google.com/file/d/1aFZki-haLVVstwrTdjCuNO3DjNn-pI_f/view)、[今日单词四阶段截图](https://drive.google.com/file/d/1s3pPQco1vtijSXRcInyrc9mTQ5VYKBc0/view)、[3秒真实动画样片](https://drive.google.com/file/d/1zJbfP0HF6QwE01HNNfJgfvXzjWbKPth1/view)。
- **新源码可恢复**：[Google Drive v03源码ZIP（含新Banner，不含私有头像/BGM）](https://drive.google.com/file/d/16ZXzfDCaD9QHA1bBxeag9W1e3ORseF-1/view)；GitHub [可应用补丁](./patches/20261125_ui_v03.patch)、[交接说明](./patches/20261125_ui_v03_README.md)。补丁在原修正版ZIP解包目录上用`patch -p1 --dry-run`检查成功，测试数据无需外传。后续别直接使用原来的旧ZIP当新版。
- **交接下一步**：用户对UI截图确认后，用新模板先小范围验证03/06的词卡、字幕和配音；若用户还要求正式全长视频，则独立输出v03、逐字/全片带声验收、再按六件套归档。旧v02/原音频全部保留。08暂停。

## 只处理的范围与严禁事项

用户现场确认 Google Drive 中 **01、02、04、05、07、09 已经发布**，禁止重新检查、改名、替换、删除、重排、覆盖。
**03、06 尚未发布且仍在整改；08 尚未发布但用户要求暂时暂停重做**。原片始终保留，修正版另存新文件。没有用户明确授权不自动向抖音或 TikTok 发布。

## 一眼看懂：接下来的具体任务

| 序号 | 当前真实状态 | 已实际完成的工作与链接 | 接班 AI 下一步 |
|---|---|---|---|
| **03 / R03《小宇护苏姐怼黑心房东》** | 🟡 **v02视频已渲染并上传，待最终带声审片** | [03 v02候选MP4 42.467秒](https://drive.google.com/file/d/1vNDnAksqSWg8J6OmyNks7JHU92A5SuAl/view)、[修正版质检报告](https://drive.google.com/file/d/1aQL8IgOxHnVLMeYvSVyk2sOJz46FZtet/view)、[原版问题排查](https://drive.google.com/file/d/1X7vTM16WDHbJfdcFMCZDYnOgDkx46B7z/view)。删除遮挡聊天的大型单词弹窗，保留顶部/气泡词卡；加入音量驱动头像微动和底部小声波；新片1080×1920、30fps、H.264/AAC、音轨与原MP3匹配、全片解码正常、无黑屏。**仍有近似静态窗口和未人工逐字/全片试听项目。** | 完整从头到尾带声观看，检查语句/音效/错字/人物、最后5秒、静止感。合格才可改“可发布”；不合格修新版本。 |
| **06 / EP05《半夜外卖员乌龙》** | 🟡 **v02全长新版已重新渲染并上传，待最终带声审片** | [06 v02候选MP4 88.032秒](https://drive.google.com/file/d/1YVcZreKBlUMOkVM03CAqbm2P9Ih12cWu/view)、[修正版质检报告](https://drive.google.com/file/d/1DSR7bQ18uHA1k2XKyMFkbLEUGdtrFcs6/view)。旧视频89.328秒与新配音不符，新v02使用同一版本MP3 88.032秒 + JSON十句，7个时间窗口音源相关性0.955～0.975，**错音轨问题已实际修复**。解码正常、无黑屏、去大型遮挡弹窗并加入底部声波。**机器检测仍有长静态窗口，未真人全片逐字听审；只能叫候选版。** | 播放实际Drive MP4，逐句检查字幕、越南语、波形/音量、人物声线、聊天滚动和最后反转。通过才把06改为可发布。 **旧视频保留，不要取错版**。 |
| **08 / EP07《猛男坦克的药店惊魂》** | ⏸️ **用户明确暂停：不重渲、不补配音** | 现有MP4和原MP3均约28.8秒、9句，已备份6句续写稿但仅作历史备忘。原视频尚未满足用户观感要求。 | **无需动作；等用户明确恢复08再继续。** 不调用Gemini补录、不覆盖原片。 |

## 质量验收为什么仍是“待终验”

- 全集已通过：ffprobe编码/真实时长、全片ffmpeg视频解码、MP3与输出音轨抽样波形、黑帧扫描；自动检测静止画面并留报告。
- 机器检测和截帧**不能替代实际从头听完整音频及逐字看字幕**；目前没有做到这一点，不得写“合格可发布”。
- 03、06 的音频对齐缓存使用JSON每镜头分配字符时间，**没有运行Whisper强制逐字对齐**；请检查字幕是否存在错拍。
- 大弹窗已从03/06本次候选中取消，保留小词条与顶部黑板；仍应关注小字卡是否挡字幕。
- 自动检查脚本现已保存为 GitHub [qa_video.py](./qa_video.py)，支持按三个文件进行时长、音轨来源、黑帧、静帧、视频解码检测；命令见下方。人工核对仍是必要环节。
- 旧版片/素材一律保留，不重排已发布01/02/04/05/07/09。

## 工作入口

- [正式成品区](https://drive.google.com/drive/folders/1lQngmeGPUJN5aoDmGDFjkkAqZPxqioLk)
- [03文件夹](https://drive.google.com/drive/folders/1G_217TVQ54mmEOSoi6fPn6-em-GHe1hf)：可见原MP4、v02候选和质检两份报告
- [06文件夹](https://drive.google.com/drive/folders/1uWeZlSYtbnKeK2A4I7L6SP18KPiCL__o)：旧版错配MP4和独立新v02 MP4、QA报告
- [08文件夹](https://drive.google.com/drive/folders/10bF9Xx6LoeY26KcBnHOVpYpTRNi_nH5m)：原9句MP3/JSON/MP4及v02补录稿
- [Gemini原始素材](https://drive.google.com/drive/folders/1Unt8ggki_j7KWq-AA5k4sp1lgeUAjDjI)；[Grok渲染器/头像包/BGM](https://drive.google.com/drive/folders/1g8ZzYqAQn90rITPHVoBOinrHIXCqD3nk)

## 每次新渲染必须做的动作

1. 对齐同集同版本 MP3 + JSON；角色ID/声线/谐音严格匹配，不乱换。
2. 产出1080×1920 30fps H.264/AAC MP4；跑 `python grok-migration/qa_video.py --video 成品.mp4 --audio 原配音.mp3 --json 原时间轴.json --out QA.json`。仅机器检查不标通过。
3. **完整带声观看**，逐句核对字幕、角色、时长、音轨、卡顿、冻帧、遮挡、末句及剧情完整性。
4. 修复只新增版本，不能覆盖原件；合格后按云盘01MP3/02JSON/03剧情/04视频/05独立3:4封面/06文案＋首评＋交付记录整理。
5. 在本页更新状态、具体输出链接和下一位接手要做什么，再在 [AI_HANDOFF.md](./AI_HANDOFF.md) 追加实际操作日志。**不允许说“做完了”但没有文件和验收证据。**

## 本轮变更（2026-11-25）

- 03和06分别实际重渲视频并上传Google Drive，**不是只写建议**；原版仍在原位。
- EP07续写稿已产出并上传，**没有新声线MP3/JSON时不能完成08重渲**。
- 新增GitHub可运行机器QA工具；已在真实03/06旧版/08和新03/06视频上测试。
- 01、02、04、05、07、09已发布，完全未改。
