#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

URL = 'http://www.tuicool.com'
URL_MAGS = 'http://www.tuicool.com/mags'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
url = '/mags/58772dc0a8d90d792c03c6d2'


def get_mags_links():
    links = []
    try:
        r = requests.get(URL_MAGS, headers = headers)
        soup = BeautifulSoup(r.content, "html.parser")
        link_all = soup.find_all('a')
        for i in link_all:
            one_match = i.get('href')
            if 'mags' in str(one_match) and '5' in str(one_match):
                # print one_match
                links.append(one_match)
        return links    

    except Exception, e:
        print str(e)
        return None



#u"获取源码中得信息"
def get_content(url):
    link = URL + url
    print link
    write_list=[]
    try:
        r = requests.get(link, headers = headers)
        soup = BeautifulSoup(r.content,"html.parser")
        title = soup.find('title').get_text() 
        article_list = soup.find_all(attrs={"class": "title"})
        for i in article_list:
            write_title = i.get('title')
            write_link = i.get('href')
            write_author = i.get_text()
            write_content = write_title + '\t' + write_link + '\t' + '\n'
            write_list.append(write_content)
        
        f = codecs.open('tuicool_weekly.txt', 'a', 'utf-8')
        f.write('--------' + title + '******' + link + '----------' + '\n')
        for article in write_list:
            f.write(article)
        f.close() 

    except Exception,e:
        print str(e)
        return None          


def main():
    for url in get_mags_links():
        get_content(url)
        time.sleep(5)
        
    
if __name__ == "__main__":
    main()  
    
