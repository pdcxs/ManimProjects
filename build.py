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

files = [f for f in projectPath.iterdir()\
    if f.name not in ['build.py', 'setup.py']\
        and f.suffix == ".py"]

fileNum = len(files)
print("Please select your file:")
for i, f in zip(range(fileNum), files):
    print('%d:\t%s' % (i, f.name))

select = input('Build File: ')

targetFile = files[int(select)]
classes = []
with open(targetFile, 'r', encoding='utf8') as f:
    for ln in f.readlines():
        if ln.lstrip().startswith('class'):
            words = re.split('\s|\(', ln)
            if len(words) > 1:
                classes.append(words[1])

classNum = len(classes)
print("Please select build scene:")
for i, c in zip(range(classNum), classes):
    print('%d:\t%s' % (i, c))
select = input('Build Class: ')
targetClass = classes[int(select)]

cmd = 'python -m manim %s %s %s --media_dir %s' %\
    (str(targetFile), targetClass,\
    ' '.join(sys.argv[1:]), mediaPath)
print('Executing: ')
print(cmd)
os.system(cmd)
