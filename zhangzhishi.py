#!/usr/bin/env python
import os
import re

file_list = os.listdir("/home/evas/demo")
restr = re.compile("http.*?jpg")
outfile = open("out.txt","a")
for htmlfile in file_list:
    file_name = r"/home/evas/demo/ + htmlfile"
    target_file = open(file_name,"r").readlines()
    for line in target_file:
        mingzhong = restr.search(line)
        if mingzhong and len(mingzhong.group()) < 120:
            outfile.writelines(mingzhong.group())
            outfile.writelines("\n")
outfile.close()
