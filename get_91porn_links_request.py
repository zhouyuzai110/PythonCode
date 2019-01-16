#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os, re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
proxies = {'http': 'socks5://127.0.0.1:1080'}

raw_cookies = 'evercookie_cache=<br/>; evercookie_png=<br/>; evercookie_etag=<br/>; \
l91lb91a=1; _ga=GA1.2.1999180034.1495265586; __utmz=50351329.1496750605.3.2.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/bOL5FLj6iy;\
 __dtsu=1EE704455AC3165A675F5A5402C8FAEB; AJSTAT_ok_times=42; __cfduid=dd62c082ed82e3b0ea9f63f314b026e641526913323;\
  91username=fe1fccKc2Q%2BvIEc7xuOICsrmeW%2BCnkh94jcs8pZo9bRQPE0; CLIPSHARE=7od9k2abaktlg31mhpgk3lvhf5; __51cke__=;\
   _gid=GA1.2.288998344.1547554232; __utmc=50351329; __utma=50351329.1999180034.1495265586.1547554285.1547638808.175; \
   watch_times=4; __tins__3878067=%7B%22sid%22%3A%201547638808309%2C%20%22vd%22%3A%2010%2C%20%22expires%22%3A%201547640902661%7D; \
   __51laig__=25'

cookies={}  
for line in raw_cookies.split(';'):  
    key,value = line.split('=',1)#1代表只分一次，得到两个数据  
    cookies[key]=value  

pattern = re.compile(r'.{6}.mp4')

#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
        r = requests.get(url, headers = headers, proxies = proxies, cookies = cookies)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('source')
        for i in p:
            target_link = i.get('src')
            print target_link
            return target_link
    except Exception,e:
        print str(e)
        return None          


def write_into_files(url):
    filename = re.findall(pattern, str(url))[-1]
    print filename
    if os.path.exists(filename):
        print 'Already Exists'
    else:
        conn = requests.get(url, stream = True, timeout = 5, headers = headers, proxies = proxies)
        f = open(filename,'wb')  
        f.write(conn.raw.read())  
        f.close()  


def main():
    os.chdir("/home/evas/Downloads/")
    while True:
        try:
            url = raw_input("the url is : ")
            target_link = get_hyper_links(url)
            write_into_files(target_link)
        except Exception,e:
            print str(e)
            return None    
        

        
if __name__ == "__main__":
    main()  
    
    