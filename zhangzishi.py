#!/usr/bin/env python
import os
import re

i = 0

file_list = os.listdir(os.getcwd())
restr = re.compile("http.*?jpg")
outfile = open("out.txt","a")
for htmlfile in file_list:
    i += 1
    print i,htmlfile
    target_file = open(htmlfile,"r").readlines()
    for line in target_file:
        mingzhong = restr.search(line)
        if mingzhong and len(mingzhong.group()) < 120:
            outfile.writelines(mingzhong.group())
            outfile.writelines("\n")
outfile.close()

order_file = open("out.txt").readlines()
set_order_file = list(set(order_file))
set_order_file.sort()
out_order_file = open("order_file.txt","a")
for l in set_order_file:
    out_order_file.writelines(l)
    #out_order_file.writelines("\n")

out_order_file.close()


