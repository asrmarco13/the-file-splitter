# The File Splitter (FS)

<p align="center">
  <a href="https://github.com/asrmarco13/the-file-splitter"><img alt="Python" src="https://img.shields.io/pypi/pyversions/latest"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter/blob/master/LICENSE"><img alt="License: GPL3" src="https://img.shields.io/github/license/asrmarco13/the-file-splitter"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter"><img alt="Latest commit" src="https://img.shields.io/github/last-commit/asrmarco13/the-file-splitter/master"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter/issues"><img alt="Open Issues" src="https://img.shields.io/github/issues/asrmarco13/the-file-splitter"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter/issues?q=is%3Aissue+is%3Aclosed"><img alt="Closed Issues" src="https://img.shields.io/github/issues-closed/asrmarco13/the-file-splitter"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter/pulls"><img alt="Pull requests" src="https://img.shields.io/github/issues-pr/asrmarco13/the-file-splitter"></a><img alt="Latest commit" src="https://img.shields.io/github/last-commit/asrmarco13/the-file-splitter/master"></a>
  <a href="https://pypi.org/project/FileSplitter/"><img alt="Pypi" src="https://img.shields.io/pypi/v/FileSplitter"></a>
  <a href="https://aur.archlinux.org/packages/python-filesplitter/"><img alt="AUR Archlinux" src="https://img.shields.io/aur/version/python-filesplitter"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    <a href="https://github.com/asrmarco13/the-file-splitter"><img alt="Follower" src="https://img.shields.io/github/followers/asrmarco13?style=social"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter"><img alt="Follower" src="https://img.shields.io/github/stars/asrmarco13/the-file-splitter?style=social"></a>
  <a href="https://github.com/asrmarco13/the-file-splitter"><img alt="Follower" src="https://img.shields.io/github/watchers/asrmarco13/the-file-splitter?style=social"></a>  
<p>

## **Content index**
1. [Introduction](#introduction)
2. [Archlinux AUR one line package install](#archlinux-aur-one-line-package-install)
3. [Pypi installation](#pypi-installation)

###  **Introduction**

File splitter is a tool that split large file into multiple small file. Often in test or production environments it happens that you have to manage very heavy text files and opening them could take a long time.

FS allows you to split a heavy file into many small, small files. FS is easy to use. To launch it, just use the following command:
```python
filesplitter -f <filename>
```
FS by default creates 1 small single file every 1000 lines. If you want to increase or decrease the number of lines use the command **-r**.

If you want to change the encoding type of the source file, just use the command **-e**.

For help:
```python
filesplitter -h
```

### Archlinux AUR one line package install

Install File Splitter with a single command with [Yay](https://github.com/Jguer/yay) or another AUR helper:

| Aur Helper | Command                         |
| ---------- | ------------------------------- |
| Yay        | yay -S python-filesplitter      |
| Pakku      | pakku -S python-filesplitter    |
| Aurutils   | aurutils -S python-filesplitter |

### Pypi installation

Install File Splitter like Python package with pip:

| Command                  |
| ------------------------ |
| pip install FileSplitter |

Good use :smile:

Enjoy :beers:
