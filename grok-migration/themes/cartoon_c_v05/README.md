# 方案C｜越南语趣味大剧场手绘卡通主题 v05

## 已落实
- 固定内容（越南国旗、「越南语趣味大剧场」、「每天一分钟学习越南语」、「今日单词」黑板标题、顶部人物、底部风情插画）直接印在一张精确的 **1080×1920 PNG** 中，而不是运行时重复写字。
- 只把**每集会变化的单词卡、头像、聊天气泡、越语/谐音/中文、音效与动画**交给渲染器动态绘制。
- 群名标题栏已取消，黑板靠上；对话区从 y=610 到 y=1794，底部输入栏保留。
- 新主题存于 styles/chat_final.py，默认 C；在 mix.json 指定 `ui_theme: classic` 可以返回原v04主题（不是更改用户已发布作品）。
- 黑板的动态单词从 x>=350 开始摆放，不覆盖静态「今日单词」标题。
- 使用 EP05/06 新版MP3+JSON做了 13秒真实渲染静帧、19项自动测试通过。**还未完成03/06全片新主题渲染、逐句听审或最终发布。**

## 位置和运行
- 固定背景文件：`vn_theater/assets/banner/cartoon_c_fixed_1080x1920.png`
- 渲染代码：`vn_theater/styles/chat_final.py`
- 相对 v04 的增量修改：`theme_c_v05_from_v04.patch`，在ZIP顶层解包目录执行 `patch -p1 < theme_c_v05_from_v04.patch`。如果直接使用 v05 完整源码ZIP，则**不需再应用补丁**。
- 需要独立提供用户私人Google Drive中的15人头像、配音、BGM等。源码ZIP不含私有声纹、头像和音乐。
- 对新的06候选版可运行：`python run_episode.py episode.json audio.mp3 --no-align --style chat_final --still 13 --no-cover --no-endcard --no-cover-hold --outdir preview`。
- 注意：`--no-align`只用于快速静帧测试；最终视频按 VIDEO_QA_CHECKLIST.md 全片审音、字幕/谐音、卡顿和收尾，不得仅凭测试过了就说可发布。

## 当前项目边界
- 08 用户暂停修改；已发布01、02、04、05、07、09不动。新UI仅对后续未发布版本启用。


## 2026-11-27 跨聊天窗口源码恢复入口
GitHub 原始 v05 ZIP 保留。用户上传的同名完整源码包已另存 Google Drive：`越南语趣味大剧场/00_固定规范/vn_theater_themeC_v05_20261125.zip`。
备用下载：https://drive.google.com/file/d/1BMqExhR_-oaab9xCatqop0jpJT2eqA6w/view
若 GitHub 文本连接器不能读取二进制 ZIP，直接通过已授权的 Google Drive 文件下载/物化功能取得该备份，不要求用户重新搬运。配音素材、JSON、头像和 BGM 仍从原 Drive 目录获取。新聊天窗口需重新解包执行，不能依赖旧窗口临时文件。预览确认后才做整片；不覆盖旧作品。此次备份上传成功，不代表渲染验收通过。


## 2026-11-27 最新 C v05 裁切修正版（优先使用）
仅修聊天视口：y=610 到 1794，全部头像、昵称、时间、气泡及弹入动画统一裁切，不覆盖黑板与品牌标题。旧主题不变。真实第20秒静帧已检查，原19项单测通过；未渲染完整视频。
完整已修复源码 ZIP（Google Drive）：https://drive.google.com/file/d/1RJa2xM8ShC3qZngpmBRTsfEUj_TGwEPc/view 。文件位于 `越南语趣味大剧场/00_固定规范/vn_theater_themeC_v05_clipfix_20261127.zip`，新窗口优先直接读取此包，不再应用补丁。旧 ZIP 保留作为历史备份；若使用 GitHub 原 ZIP，解包后执行 `patch -p1 < grok-migration/themes/cartoon_c_v05/chat_viewport_clipfix.patch`（从仓库根目录执行）。GitHub Actions 已配置解包后应用此补丁，尚未实际启动验证。其他风格、素材与历史作品不动。
