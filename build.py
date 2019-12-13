#!/usr/bin/python3
# -*- coding: utf8 -*-

from pathlib import Path
import sys
import re
import os

projectFolder = 'ManimProjects'

projectPath = Path.joinpath(
    Path(__file__).absolute().parent,
    projectFolder)

mediaPath = Path.joinpath(projectPath, 'media')

files = []
extraFiles = ['build.py', 'setup.py', 'media', 'concat_video.py']

def iterdir(targetDir):
    for f in targetDir.iterdir():
        if f.name in extraFiles:
            pass
        elif f.is_dir():
            iterdir(f)
        elif f.suffix == ".py":
                files.append(f)

iterdir(projectPath)
files.sort(key=lambda m:m.stat().st_mtime, reverse=True)

print("Please select your file:")
for i, f in enumerate(files, 1):
    print('%d:\t%s' % (i, f.relative_to(projectPath)))

select = input('Build File: ')

targetFile = files[int(select) - 1]
# classes = []
# with open(targetFile, 'r', encoding='utf8') as f:
#     for ln in f.readlines():
#         if ln.lstrip().startswith('class'):
#             words = re.split('\s|\(', ln)
#             if len(words) > 1:
#                 classes.append(words[1])

# classNum = len(classes)
# print("Please select build scene:")
# for i, c in zip(range(classNum), classes):
#     print('%d:\t%s' % (i, c))
# select = input('Build Class (All): ')
# if select == '':
#     targetClass = '-a'
# else:
#     targetClass = classes[int(select)]
targetClass = ''

cmd = 'python -m manim %s %s %s --media_dir %s' %\
    (str(targetFile), targetClass,\
    ' '.join(sys.argv[1:]), mediaPath)
print('Executing: ')
print(cmd)
os.system(cmd)
