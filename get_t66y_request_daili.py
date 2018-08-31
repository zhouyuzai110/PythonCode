#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
 

#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
        links = []
        origin = requests.get(url, timeout = 5, headers = headers)
        soup = BeautifulSoup(origin.content, "html.parser")
        
        p = soup.find_all('input')
        for i in p:
            target_link = i.get('src')
            if target_link is not None and 'sinaimg.cn' not in target_link:
                print target_link
                links.append(target_link) 
        return links

    except Exception,e:
        print str(e)
        return None          

def get_title(url):
    origin = requests.get(url, timeout = 5, headers = headers)
    soup = BeautifulSoup(origin.content, "html.parser")
    
    title = soup.find('h4').get_text()    
    return title


#u"将图片写入文件"
def write_into_files(jpgname,url):

    conn = requests.get(url, stream = True, timeout = 5, headers = headers)
    f = open(jpgname,'wb')  
    f.write(conn.content)  
    f.close()  



def main():

    os.chdir("/home/evas/Desktop/scripts/photo")
    while True:
        url = raw_input('The URL is : ')
        links = get_hyper_links(url)
        title = get_title(url)
        for link in links:
            try:
                time.sleep(1)
                jpgname = title + str(time.time()) + ".jpg"
                write_into_files(jpgname,link)
                print('Pic Saved!') 
            except Exception, e:
                print str(e)

        
if __name__ == "__main__":
    main()  
    
    