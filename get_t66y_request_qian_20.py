#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

source_page_url = 'http://cl.yxoi.org/thread0806.php?fid=16&search=&page='
source_link = 'http://cl.yxoi.org/'
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
    try:
        origin = requests.get(url, timeout = 5, headers = headers)
        soup = BeautifulSoup(origin.content, "html.parser")
        title = soup.find('h4').get_text()    
        return title
    except Exception,e:
        print str(e)
        return None  
        

#u"将图片写入文件"
def write_into_files(jpgname,url):
    try:
        conn = requests.get(url, stream = True, timeout = 5, headers = headers)
        f = open(jpgname,'wb')  
        f.write(conn.content)  
        f.close()  
    except Exception,e:
        print str(e)
        return None  


def get_page(num):
    try:
        links = []
        url = source_page_url + str(num)
        origin = requests.get(url, timeout = 5, headers = headers)
        soup = BeautifulSoup(origin.content, "html.parser")
        p = soup.find_all('a')
        for i in p:
            target_link = i.get('href')
            if check_target_link(target_link):
                target_link = source_link + target_link
                links.append(target_link)
        target_links = list(set(links)) 
        target_links.sort(key = links.index)
        return target_links   
    except Exception,e:
        print str(e)
        return None  
        

def check_target_link(target_link):
    if target_link is not None and 'htm_data' in target_link:
        if '1402' in target_link or '1110' in target_link or \
        '1109' in target_link or '1106' in target_link or \
        '0907' in target_link or '0805' in target_link:
            return False
        else:
            return True


def main():

    # os.chdir("/home/evas/Desktop/scripts/photo")
    os.chdir("/home/evas/Desktop/scripts/")

    for num in range(1,21):
        for url in get_page(num):
            print url
            links = get_hyper_links(url)
            title = get_title(url)
            try:
                for link in links:
                    print link
                    time.sleep(1)
                    jpgname = title + str(time.time()) + ".jpg"
                    write_into_files(jpgname,link)
                    print('Pic Saved!') 
            except Exception, e:
                    print str(e)

        
if __name__ == "__main__":
    main()  
    
