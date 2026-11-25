#!/usr/bin/env python3
"""Read-only Vietnamese theater video QA: ffprobe, decode, freeze/black, audio-match and JSON timing.

CLI: python qa_video.py --video VIDEO.mp4 --audio SOURCE.mp3 --json SOURCE.json --out report.json
No file mutation. Automatic checks do NOT replace human word-by-word and story review.
"""
import argparse, json, math, os, re, subprocess, sys
from pathlib import Path
import numpy as np


def command(args):
    cp = subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    return cp


def probe(path):
    r=command(['ffprobe','-v','error','-show_format','-show_streams','-of','json',path]);
    if r.returncode:raise ValueError(f'ffprobe failed: {path}: {r.stderr[:500]}')
    return json.loads(r.stdout)


def decodes(path):
    r=command(['ffmpeg','-v','error','-i',path,'-map','0:v:0','-f','null','-'])
    return {'ok':r.returncode==0,'errors':r.stderr[-1500:] if r.returncode else ''}


def audio_pcm(path,sr=8000):
    p=subprocess.run(['ffmpeg','-v','error','-i',path,'-map','0:a:0','-ac','1','-ar',str(sr),'-f','s16le','-'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode:return None
    return np.frombuffer(p.stdout,dtype=np.int16).astype(np.float32)/32768.0


def windows_corr(a,b,sr=8000):
    if a is None or b is None:return {'status':'unavailable','windows':[]}
    # Check multiple windows. Allow small relative latency, best local lag ±120 ms.
    # Scoring is deliberately not used alone to approve content.
    starts=[3,10,20,30,40,55,70]
    results=[]
    for t in starts:
        i=int(sr*t); n=int(sr*1.5)
        if i+n>=min(len(a),len(b)) :continue
        x=a[i:i+n].copy();x-=x.mean()
        if np.linalg.norm(x)<0.05:continue
        best=-1.;best_lag=0
        for offset in range(-960,961,40):
            j=i+offset
            if j<0 or j+n>len(b):continue
            y=b[j:j+n]; y=y-y.mean()
            den=np.linalg.norm(x)*np.linalg.norm(y)
            if den>0:
                z=float(np.dot(x,y)/den)
                if z>best:best=z;best_lag=offset/sr
        results.append({'start_sec':t,'max_corr':round(best,3),'lag_sec':round(best_lag,3)})
    good=[w for w in results if w['max_corr']>0.62]
    return {'status':'likely_same_source' if len(good)>=max(2,(len(results)+1)//2) else 'needs_manual_check', 'windows':results}


def detect(video,filters):
    p=command(['ffmpeg','-hide_banner','-loglevel','info','-i',video,'-vf',filters,'-an','-f','null','-'])
    out=p.stderr
    freezes=[float(z) for z in re.findall(r'lavfi\.freezedetect\.freeze_start: ([0-9.]+)',out)]
    ends=[float(z) for z in re.findall(r'lavfi\.freezedetect\.freeze_end: ([0-9.]+)',out)]
    ranges=[]
    for i,s in enumerate(freezes):
        e=ends[i] if i<len(ends) else None
        ranges.append({'start_sec':round(s,3),'end_sec':round(e,3) if e is not None else None,'duration_sec':round(e-s,3) if e is not None else None})
    blacks=re.findall(r'black_start:([0-9.]+) black_end:([0-9.]+)',out)
    return {'static_image_windows_gt_1_5s':ranges,'black_intervals':[{'start_sec':float(s),'end_sec':float(e)} for s,e in blacks],'ffmpeg_scan_success':p.returncode==0}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--video',required=True);ap.add_argument('--audio',required=True);ap.add_argument('--json',required=True);ap.add_argument('--out',required=True);ap.add_argument('--episode',default='')
    args=ap.parse_args()
    data=json.load(open(args.json,encoding='utf-8'))
    pv,pa=probe(args.video),probe(args.audio)
    vs=next(s for s in pv['streams'] if s['codec_type']=='video');va=next((s for s in pv['streams'] if s['codec_type']=='audio'),None)
    av=next(s for s in pa['streams'] if s['codec_type']=='audio')
    vdur=float(pv['format']['duration']);adur=float(pa['format']['duration'])
    timeline=data.get('millisecond_timeline') or []
    json_dur=float(data.get('total_audio_duration_sec') or data.get('total_audio_duration_ms',0)/1000)
    last_end=max((float(s.get('end_ms') or 0)/1000 for s in timeline),default=0)
    scan=detect(args.video,'freezedetect=n=-45dB:d=1.5,blackdetect=d=0.3:pix_th=0.09')
    corr=windows_corr(audio_pcm(args.audio),audio_pcm(args.video))
    result={'episode':args.episode or data.get('episode_code'),'video':args.video,'source_audio':args.audio,'source_json':args.json,
      'video_sec':round(vdur,4),'source_mp3_sec':round(adur,4),'json_duration_sec':round(json_dur,4),'json_last_shot_end_sec':round(last_end,4),'json_shots':len(timeline),
      'video_audio_codec':va.get('codec_name') if va else None,'video_codec':vs.get('codec_name'),'video_fps':vs.get('r_frame_rate'),'width':vs.get('width'),'height':vs.get('height'),
      'video_decode':decodes(args.video), 'duration_diff_video_vs_source_sec':round(vdur-adur,4),
      'duration_check':'pass' if abs(vdur-adur)<0.4 else 'review',
      'audio_source_match':corr,'frame_scan':scan,
      'human_review_required':['listen_full_dialogue_naturalness','verify_every_subtitle_and_Vietnamese_tone','check_chat_pacing_and_story_ending','verify_avatars_and_safe_areas'],
      'final_release_status':'NOT_APPROVED_AUTOMATICALLY'}
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    open(args.out,'w',encoding='utf-8').write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'episode':result['episode'],'durations':[result['video_sec'],result['source_mp3_sec'],result['json_duration_sec']],'corr':corr['status'],'static':len(scan['static_image_windows_gt_1_5s']),'black':len(scan['black_intervals']),'out':args.out},ensure_ascii=False))

if __name__=='__main__': main()