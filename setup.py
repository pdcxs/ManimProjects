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
    f.write('\nbuild.py')
    f.write('\nbuild.ps1\n')
print('Done')

# copy run code to manim project
import shutil

print('Copy build.py to %s' % path.parent)
cmd = Path.joinpath(fileDir, 'build.py')
shutil.copy(cmd, path.parent)
print('Done')

print('Copy build.ps1 to %s' % path.parent)
cmd = Path.joinpath(fileDir, 'build.ps1')
shutil.copy(cmd, path.parent)
print('Done')

print('Does .vscode exist?')
vscode_path = Path.joinpath(fileDir.parent, '.vscode')
if vscode_path.is_dir():
    print('Yes, .vscode exists')
else:
    print('No. Making .vscode')
    vscode_path.mkdir()
print('Copy tasks.json %s' % path.parent)
shutil.copy(
    Path.joinpath(fileDir, 'tasks.json'),
    vscode_path)
print('Done')

# Making media directory
print('Making media directory')

mediaDir = Path.joinpath(fileDir, 'media')
if mediaDir.is_dir():
    print('media directory already exists.')
else:
    mediaDir.mkdir()
print('Done')