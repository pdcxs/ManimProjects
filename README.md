# ManimProjects

I will put my manim files in this repository.

To run the code, please use [manimlib](https://github.com/3b1b/manim).

## USAGE:

### Step 1

Install manimlib according to the instructions in [manimlib](https://github.com/3b1b/manim).

We need to clone all of the files to local machine, rather than use pip to install the manimlib.

### Step 2

1. Change directory to the manimlib directory.
2. Clone the repository: `git clone https://github.com/pdcxs/ManimProjects`

### Step3

Stay in the manimlib directory, deploy the build tools with:
`python ManimProjects/setup.py`

### Step4

If you use vscode and install python with anaconda or miniconda (env name is manim, if not, please change the line 6 of file `build.ps1`), you can just open the manim folder with vscode, then open your file, put the cursor in the class that you want to build (any line), press `Ctrl-Shift-B`, and select the build solution to build your scene.

Otherwise, build projects with: `python build.py [options]`

For example: `python build.py -pl`

Then select the target file and classes.

You can also manually build the code without the tools, of course.
