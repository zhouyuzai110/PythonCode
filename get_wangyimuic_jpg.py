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
        cover_img = net_easy_json['result']['coverImgUrl']
        name = net_easy_json['result']['name']
        return [name, cover_img]

    except Exception,e:
        print str(e)
        return None          

#u"将图片写入文件"
def write_into_files(lists):

    conn = requests.get(lists[1], timeout = 5)
    jpgname = lists[0] + ".jpg"
    f = open(jpgname,'wb')  
    f.write(conn.content)  
    f.close()
    print('Pic --%s-- Saved!') %lists[0]  



def main():

    while True:
        os.chdir("/home/evas/图片/NetEastMusic/")
        url = 'http://music.163.com/api/playlist/detail?id=' + raw_input("The URL is : ")
        cover_img_name = get_hyper_links(url)
        write_into_files(cover_img_name)
        
        

        
if __name__ == "__main__":

    main()  
    
    