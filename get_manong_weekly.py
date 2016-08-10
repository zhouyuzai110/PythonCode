#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

URL = 'http://weekly.manong.io/issues/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
   

#u"获取源码中得信息"
def get_content(url):
    try:
        r = requests.get(url, headers = headers)
        print url
        soup = BeautifulSoup(r.content,"html.parser")
        qishu = soup.find('h1').get_text() + soup.find('h2').get_text()
        p = soup.find_all('h4')
        f = codecs.open('manong_weekly.txt', 'a', 'utf-8')
        f.write('-------------------' + qishu + '******' + url + '-------------------' + '\n')
        for i in p:
            i_text = i.find('a').get_text().replace(' ','').replace('\n','')
            i_href = i.find('a').get('href').replace('http://weekly.manong.io/bounce?url=','').replace(' ','')\
                      .replace('\n','').replace('%3A%2F%2F','://').replace('%2F','/')\
                      .replace('&itemId=','\t').replace('%3F','?').replace('%3D','=')\
                      .replace('%26','&').replace('%2B','+').replace('%25','%')
            # print qishu, i_text, i_href
            write_content = qishu + '\t' + i_text + '\t' + i_href + '\n'
            print write_content
            f.write(write_content)
        f.close() 

    except Exception,e:
        print str(e)
        return None          


def main():
    for i in range(90,131):
        url = URL + str(i)
        get_content(url)
        time.sleep(3)
        
    
if __name__ == "__main__":
    main()  
    
