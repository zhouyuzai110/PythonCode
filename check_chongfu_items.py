#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 
import os
import hashlib
import shutil

# HOMEDIR = '/home/evas/Dropbox/Photo/'
HOMEDIR = raw_input("the homedir path is : ")
WORKDIR = '/home/evas/test/'


def check_uniq_file_hash(HOMEDIR):
    file_hash = {}
    file_list =  os.listdir(HOMEDIR)
    for i in file_list:
        if os.path.isfile(i):
            file_hash[i] = hashlib.sha1(open(i,'rb').read()).hexdigest()
    return file_hash


def uniq_file_hash(HOMEDIR):
    hash_list_chongfu_item = [] 
    file_hash = check_uniq_file_hash(HOMEDIR)
    hash_list = file_hash.values()
    for i in hash_list:
        if hash_list.count(i) >1 :
            hash_list_chongfu_item.append(i)

    hash_list_set = set(hash_list_chongfu_item)
    return hash_list_set


def move_uniq_file(HOMEDIR, WORKDIR):
    file_hash = check_uniq_file_hash(HOMEDIR)
    hash_list_set = uniq_file_hash(HOMEDIR)
    for hash_item in hash_list_set:
        for i in file_hash.keys():
            if file_hash[i] == hash_item:
                new_pos = WORKDIR
                old_pos = HOMEDIR + i
                shutil.move(old_pos, new_pos)
                print old_pos + '---->' + new_pos + i   


def del_uniq_file(WORKDIR):
    file_hash = check_uniq_file_hash(WORKDIR)
    hash_list_set = uniq_file_hash(WORKDIR)
    for hash_item in hash_list_set:
        file_name_list =[]
        for i in file_hash.keys():
            if file_hash[i] == hash_item:
                file_name_list.append(i)
        for j in file_name_list:
            print j
        check_yes = raw_input("Do you want del this files [y/n] ? : ")
        if check_yes == 'y':
            for j in file_name_list[1:]:
                file_path = os.path.join(WORKDIR, j)
                os.remove(file_path)
                print 'del %s complete' %file_path



def main():
    os.chdir(HOMEDIR)
    move_uniq_file(HOMEDIR, WORKDIR)

    os.chdir(WORKDIR)
    del_uniq_file(WORKDIR)
    print 'All files are del completed'

if __name__ == '__main__':
    main()