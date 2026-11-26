# 唯一生产入口｜2026-11-27 用户最终指示
**旧生产链路优先，只升级画面。禁止重新部署。以下规则覆盖所有历史交接中相反的建议。**
1. 直接复用原有 Python/Pillow/FFmpeg 渲染引擎及已经成功的本地关键时间绘制、分段定帧合成流程。先查现有工作目录及原有素材，缺文件才从授权云盘取现成包。不重新开发，不要求用户购买服务器、配置 Secrets、安装插件或消耗 Codex。GitHub Actions 仅历史实验，不是生产入口。
2. 当前视觉基线：[C v05 裁切修正版完整源码](https://drive.google.com/file/d/1RJa2xM8ShC3qZngpmBRTsfEUj_TGwEPc/view)。已有原始15人表情包及BGM包沿用。只改背景、黑板、聊天视口、头像动画等用户指定细节；不要重写音频/时间轴/编码流程。
3. 已成功交付的09号采用145张关键时间画面+FFmpeg补帧至30fps；本轮6张/秒实际绘制也曾完成70.44秒，但重复全长渲染发生超时。优先复用关键时间/分段缓存方法，保留已完成片段，不反复从零开始；30fps封装不等于原生30fps。Whisper不是开工前置条件，已有JSON时间轴可用，未精确对齐须如实记录。
4. 音频以01—05号成品和本期原始MP3为基准，保留人声，BGM低于对白，必要时防破音。多风格曲库：https://drive.google.com/drive/folders/1JAdjk0IYM51fKkIMoZicrjI1DV8Q3DAh 。本期 cho thêm 谐音按用户指定“敲太木”。不擅改原稿。
5. 唯一交付顺序：匹配MP3/JSON/TXT → 完整视频实际渲染、检查并上传 → 多人物3:4封面上传 → 简短互动文案、首评和交付记录上传。按原成品区01—06六件套归档。封面以原版15人头像为准，唐哥、欣欣均用原版；参考库：https://drive.google.com/drive/folders/1C9GPmveGC1bUIsIVWFg37Gui7eS5DHXM 。文案引发评论，不复述剧情。无需逐步请示，完成后一次告知；确有阻塞才说明。
6. 本期《阿强点餐惊魂》最终版尚未交付，不能冒充完成。已发布01/02/04/05/07/09不动，08暂停。历史资料保留但不作为开工入口。不得公开私有素材或密钥。

---

<details><summary>历史记录（仅供溯源，不作为生产指令）</summary>

# 【最新状态｜先读这页】越南语趣味大剧场｜2026-11-25 实际施工结果

> **接手本项目的 AI：先读本页，再读 [VIDEO_QA_CHECKLIST.md](./VIDEO_QA_CHECKLIST.md)，最后需要细节再读 [AI_HANDOFF.md](./AI_HANDOFF.md)。** 本页最新；历史日志中“尚未开工/仍在渲染”的说法已过期。每次完成新工作必须更新本页，否则视为未交接。

## 2026-11-25｜方案C【带固定品牌的9:16背景】已完成并入 GitHub（当前最新）

- **用户纠错：** 前一张941×1672只是近似9:16；且旧版方案C未把固定节目名称提前做进背景，不符合要求。新版背景已严格处理为**1080×1920**。
- **静态背景中已直接印好**越南国旗、「越南语趣味大剧场」、「每天一分钟学习越南语」、两侧卡通人物、绿色黑板的「今日单词」字样、底部越南河畔装饰。**运行时严禁再画第二遍标题/口号/黑板固定字**。
- **动态部分才由代码负责：** 每集单词卡飞入黑板、头像/发言放大、15人聊天消息、每集越语／正确的谐音／括号里的中文翻译、滚动及配音。
- GitHub已创建独立开发分支：`feature/cartoon-c-v05-20261125`，从上一v04功能分支提交派生；**旧分支与全部已发布作品未动**。
- 新文件在本分支：`grok-migration/themes/cartoon_c_v05/background_1080x1920.png`（固定背景）；`grok-migration/themes/cartoon_c_v05/vn_theater_themeC_v05_20261125.zip`（包含实际渲染代码的干净完整源码，不含个人音轨和头像）；`grok-migration/themes/cartoon_c_v05/theme_c_v05_from_v04.patch`（相对于v04的代码增量）；`grok-migration/themes/cartoon_c_v05/README.md`（使用说明）。
- **实际验证：** EP05/06新版配音和JSON的13秒画面已由这版Python渲染器生成，不是AI假想效果图；19项单元测试通过；消除了固定「今日单词」与动态词卡重叠。真实截图保存在Google Drive `01_任务与回报/方案C_真实渲染预览_EP05_13秒_v05.png`，独立背景在`方案C_固定品牌背景_1080x1920_v05.png`。
- **未完成：** 未做03/06整集的C主题重新渲染、逐句听审和运动卡顿审查；本次只确认单帧及代码集成。08仍按用户指示暂停，已发布01/02/04/05/07/09不动。
- **接班下一步：** 新AI先查看本分支v05源码ZIP与README，继续用私人Drive的配音/JSON/头像实际渲染03或06，按VIDEO_QA_CHECKLIST逐项验收，再在本页填写确切MP4链接和结论，禁止“背景上传了”就宣布全片通过。

## 2026-11-25｜最新确认：UI v04「聊天区拉满＋文字放大」已实测（当前有效）

- 用户选定**不要方案A/B/C，直接聊天区拉满，所有消息正文字号加大**。保留v03顶部插画、群名、黑板飞入和谐音/括号译文规则。
- **已完成真实源码修改与19项测试通过**（比v03多两项）：1080×1920画面中的模拟输入栏由 y1710 下移至 y1810、消息下边界 y1690→1794（+104px），为输入栏保留16px；正文46→54px（+17.4%），发言人名字30→34px，越南语谐音26→32px，行高66→76px，谐音行高32→39px。
- **已用未发布06/EP05的同版本MP3+JSON真实渲染13s、37s、56s、78s四张静帧检查**，画面与输入栏未重叠。这些是静帧QA，不代表全片视频通过审片。
- 保存位置：[v04完整源码 ZIP](https://drive.google.com/file/d/1S3WmsqDdTpFG36zUmEfNMXo7b6QkyCy1/view)（不含私有头像/配音/BGM）；[13秒实际大字截图](https://drive.google.com/file/d/1Yf8B-vhO-U-xoxUXApY_r5Sgjt5DuzM6/view)、[v03/v04同秒对比](https://drive.google.com/file/d/1z1czLdFIPF2FILuUr9nSHMYkgfv87haF/view)、[四时间点核查图](https://drive.google.com/file/d/1loSL5TWGWT0_F1kJ3Uuj92F8wrvGwptV/view)。
- GitHub增量：[v04补丁](./patches/20261125_ui_v04_from_v03.patch) + [v04说明](./patches/20261125_ui_v04_README.md)。增量基线是v03，不是20261124的原版ZIP；继续开发**以v04源码包为准**，新补丁勿覆盖v03已实现功能。
- **边界：08仍暂停，已发布01/02/04/05/07/09完全未改；03/06正式全长v04尚未重渲、未做逐句字幕/全片配音卡顿终验，仍是待验收。** 后续仅在新v04版本中继续，不要冒充已经发布。

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


</details>
