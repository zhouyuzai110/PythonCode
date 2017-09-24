#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 
import os
import hashlib
import shutil

# HOMEDIR = '/home/evas/Dropbox/Photo/'
HOMEDIR = u'/home/evas/音乐/'
WORKDIR = '/home/evas/test/'

file_sha1 = {}
os.chdir(HOMEDIR)
file_list =  os.listdir(HOMEDIR)

for i in file_list:
    print i
    if os.path.isfile(i):
        file_sha1[i] = hashlib.sha1(open(i,'rb').read()).hexdigest()

hash_list = file_sha1.values()
hash_list_chongfu_item = []

for j in hash_list:
    if hash_list.count(j) >1 :
        hash_list_chongfu_item.append(j)

hash_list_set = set(hash_list_chongfu_item)    

for hash_item in hash_list_set:
    for k in file_sha1.keys():
        if file_sha1[k] == hash_item:
            # print k,file_sha1[k]
            new_pos = WORKDIR
            old_pos = HOMEDIR + k
            shutil.move(old_pos, new_pos)
            print old_pos + '---->' + new_pos

