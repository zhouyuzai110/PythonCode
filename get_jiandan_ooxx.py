#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

URL = 'http://jandan.net/ooxx/page-'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
url = '/mags/58772dc0a8d90d792c03c6d2'

renwu_url_list = []   

#u"获取源码中得超链接"
def get_hyper_links(url, key_word):

    try:
        links = []
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content,"lxml")
        p = soup.find_all('img')
        for i in p:
            target_link = i.get('src')
            if key_word in target_link:
                target_link = 'http:' + target_link
                print target_link
                links.append(target_link)
        return links
    except Exception,e:
        print str(e)
        return None          




#u"将图片写入文件"
def write_into_files(number, url):
    print url
    conn = requests.get(url, timeout = 5)
    jpgname = str(number) + '+' + str(time.time()) + ".jpg"
    os.chdir("/home/evas/Downloads/ooxx/")
    f = open(jpgname,'wb')  
    f.write(conn.content)  
    f.close()  




def main():
    number = 1
    for i in range(0, 2320):
        try:
            target_url = URL + str(i) + '#comments' 
            print target_url
            renwu_url_list = get_hyper_links(target_url, 'sinaimg')
            for url in renwu_url_list:
                write_into_files(number, url)
        except Exception, e:
            print str(e)
        number += 1
        time.sleep(3)
        
            
                

        
if __name__ == "__main__":
    main()  
    
    