#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

URL = 'https://wanqu.co/issues/'
URL_BASE = 'https://wanqu.co'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
   

#u"获取源码中得信息"
def get_content(url):
    try:
        r = requests.get(url, headers = headers)
        print url
        soup = BeautifulSoup(r.content,"lxml")
        title = soup.find('title')
        title_text = title.get_text()
        f = codecs.open('wanqu.txt', 'a', 'utf-8')
        f.write('******' + title_text + '******' + '\n')
        print title_text
        article_list = soup.find_all('h2')
        for article in article_list:
            article_title = article.get_text()
            article_url = URL_BASE + article.find('a').get('href')
            write_content = article_title + '\t' + article_url + '\n'
            print write_content
            f = codecs.open('wanqu.txt', 'a', 'utf-8')
            f.write(write_content)
            f.close()

    except Exception,e:
        print str(e)
        return None          


def get_max_day(url='https://wanqu.co'):
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content,"lxml")
    max_day = soup.find(style=u"margin-top: 25px; font-size: 12px").find('a')\
              .get('href').replace('/issues/', '').replace('?s=home', '')
    return max_day


def main():
    list = [x for x in range(1,int(get_max_day()) + 1)]
    while len(list) > 0:
        day = list.pop()
        target_url = URL + str(day) + '?s=/issues'
        get_content(target_url)
        time.sleep(1)
        
    
if __name__ == "__main__":
    main()  