# The File Splitter (FS)

File splitter is a tool that split large file into multiple small file. Often in test or production environments it happens that you have to manage very heavy text files and opening them could take a long time.

FS allows you to split a heavy file into many small, small files. FS is easy to use. To launch it, just use the following command:
```python
python app.py -f <filename>
```
FS by default creates 1 small single file every 1000 lines. If you want to increase or decrease the number of lines use the command **-r**.

If you want to change the encoding type of the source file, just use the command **-e**.

For help:
```python
python app.py -h
```
Good use :smile:
Enjoy :beers:
