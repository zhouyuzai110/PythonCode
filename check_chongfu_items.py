#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 
import os
import hashlib
import shutil

# HOMEDIR = '/home/evas/Dropbox/Photo/'
HOMEDIR = raw_input("the path is : ")
WORKDIR = '/home/evas/test/'

file_hash = {}
hash_list_chongfu_item = []

os.chdir(HOMEDIR)
file_list =  os.listdir(HOMEDIR)

for i in file_list:
    print i
    if os.path.isfile(i):
        file_hash[i] = hashlib.sha1(open(i,'rb').read()).hexdigest()

hash_list = file_hash.values()

for j in hash_list:
    if hash_list.count(j) >1 :
        hash_list_chongfu_item.append(j)

hash_list_set = set(hash_list_chongfu_item)    

for hash_item in hash_list_set:
    for k in file_hash.keys():
        if file_hash[k] == hash_item:
            # print k,file_hash[k]
            new_pos = WORKDIR
            old_pos = HOMEDIR + k
            shutil.move(old_pos, new_pos)
            print old_pos + '---->' + new_pos

