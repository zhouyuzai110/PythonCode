#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}

   

#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
        r = requests.get(url, headers = headers)
        net_easy_json = json.loads(r.content) 
        download_id = net_easy_json['songs'][0]['lMusic']['dfsId']
        song_link = net_easy_json['songs'][0]['mp3Url']
        song_link_list = song_link.split('/')
        del song_link_list[0]
        del song_link_list[0]
        del song_link_list[-1]
        song_link_addr = 'http://' + "/".join(song_link_list) + '/' + str(download_id) + '.mp3'
        print song_link_addr
        name = net_easy_json['songs'][0]['name']
        return [name, song_link_addr]

    except Exception,e:
        print str(e)
        return None          

#u"将图片写入文件"
def write_into_files(lists):

    conn = requests.get(lists[1], timeout = 5)
    jpgname = lists[0] + ".mp3"
    f = open(jpgname,'wb')  
    f.write(conn.content)  
    f.close()
    print('song --%s-- Saved!') %lists[0]  



def main():

    while True:
        os.chdir("/home/evas/图片/NetEastMusic/")
        song_num = raw_input("The Song Num is : ")
        url = 'http://music.163.com/api/song/detail/?id=%s&ids=[%s]' %(song_num,song_num)
        song_link_name = get_hyper_links(url)
        write_into_files(song_link_name)
        
        

        
if __name__ == "__main__":

    main()  
    
    