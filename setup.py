#!/usr/bin/python3
#-*- coding: utf-8 -*-

# modify the .gitignore file
from pathlib import Path
import sys

print('Modifying .gitignore in manim')
fileDir = Path(__file__).absolute().parent
path = Path.joinpath(fileDir.parent, ".gitignore")

if not path.is_file():
    print('Cannot find .gitignore in %s.' % str(path.absolute()), file=sys.stderr)

with open(path, 'a') as f:
    f.write('\n' + fileDir.name)
    f.write('\nbuild.py\n')
print('Done')

# copy run code to manim project
import shutil

print('Copy build.py to %s' % path.parent)
cmd = Path.joinpath(fileDir, 'build.py')
shutil.copy(cmd, path.parent)
print('Done')

# Making media directory
print('Making media directory')

mediaDir = Path.joinpath(fileDir, 'media')
if mediaDir.is_dir():
    print('media directory already exists.')
else:
    mediaDir.mkdir()
print('Done')