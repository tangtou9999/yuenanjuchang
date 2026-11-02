// 用法: node tools/render.js "pages/kinetic.html#B" output/out.mp4 [fps=30] [audio文件(可选)] [并行数=3]
// 页面需要提供: window.__ready(true) / window.__total(秒) / window.seek(秒)
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs'), os = require('os');
const { execFileSync } = require('child_process');
(async () => {
  const [pg, out, fpsArg, audio, parArg] = process.argv.slice(2);
  const fps = +(fpsArg || 30), par = +(parArg || 3);
  const [file, hash] = pg.split('#');
  const url = 'file://' + path.resolve(file) + (hash ? '#' + hash : '');
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'frames-'));
  const br = await chromium.launch();
  const mk = async () => {
    const p = await (await br.newContext({ viewport: { width: 540, height: 960 }, deviceScaleFactor: 2 })).newPage();
    p.on('pageerror', e => console.log('页面错误:', e.message));
    await p.goto(url);
    await p.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
    return p;
  };
  const first = await mk();
  const total = await first.evaluate(() => window.__total);
  const n = Math.round(total * fps);
  console.log(`总时长 ${total}s，共 ${n} 帧`);
  const pages = [first]; for (let i = 1; i < par; i++) pages.push(await mk());
  await Promise.all(pages.map(async (p, w) => {
    for (let i = w; i < n; i += par) {
      await p.evaluate(t => window.seek(t), i / fps);
      await p.screenshot({ path: `${tmp}/f${String(i).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    }
  }));
  await br.close();
  fs.mkdirSync(path.dirname(out), { recursive: true });
  const args = ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', `${tmp}/f%05d.jpg`];
  if (audio) args.push('-i', audio);
  args.push('-t', String(total), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p');
  args.push(...(audio ? ['-c:a', 'aac', '-b:a', '160k', '-shortest'] : ['-an']));
  args.push(out);
  execFileSync('ffmpeg', args, { stdio: 'inherit' });
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('完成:', out);
})();
