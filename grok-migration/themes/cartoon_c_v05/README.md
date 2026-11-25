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
