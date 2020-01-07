import sys
import os
import tempfile
from pathlib import Path

media_dir = '../media/videos'
if len(sys.argv) > 1:
    media_dir = sys.argv[1]

video_path = Path(media_dir)

video_files = []

def iterdir(targetDir):
    for f in targetDir.iterdir():
        if f.name == 'partial_movie_files':
            pass
        elif f.is_dir():
            iterdir(f)
        elif f.suffix == ".mp4":
                video_files.append(f)

iterdir(video_path)
video_files.sort(
    key=lambda m:m.stat().st_mtime,
    reverse=True)

if len(video_files) == 0:
    print('Cannot find any mp4 files in {}'.format(video_path))
    exit(1)

print("Please select your video file(s) (seperate by ,):")
for i, f in enumerate(video_files, 1):
    print('%d:\t%s' % (i, f.relative_to(video_path)))

select = input('Video File(s): ')

index = [int(e) for e in select.split(',')]
tmp_name = Path(tempfile.mkdtemp()).name
with open(tmp_name, mode='w+t') as fp:
    for i in index:
        select_file = str(video_files[i - 1])
        fp.write("file {}\n".format(select_file.replace('\\', '/')))

cmd = 'ffmpeg -f concat -safe 0 -i {} -c copy output.mp4'.format(tmp_name)
os.system('type {}'.format(tmp_name))
print('Executing: {}'.format(cmd))
os.system(cmd)
print('Done. output: output.mp4')
os.remove(tmp_name)

audio = input('Audio file:')

if audio == '':
    print('No audio file.')
    exit(0)

cmd = 'ffmpeg -i output.mp4 -i {} -codec copy -shortest final.mp4'.format(audio)
print('Executing')
os.system(cmd)
print('Done. output: final.mp4')