#!/usr/bin/python
import os

os.chdir('/home/marquise/testParsing')

for f in os.listdir():

    file_name , file_ext =(os.path.splitext(f))# extension cut off
    file_title , file_num =(file_name))# extension cut off
    print(file_num)
