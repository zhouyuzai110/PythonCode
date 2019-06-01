#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os, re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
proxies = {'http': 'socks5://127.0.0.1:1080'}

raw_cookies = 'evercookie_cache=<br/>; evercookie_png=<br/>; evercookie_etag=<br/>; l91lb91a=1; _ga=GA1.2.1999180034.1495265586; \
__utmz=50351329.1496750605.3.2.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/bOL5FLj6iy; __dtsu=1EE704455AC3165A675F5A5402C8FAEB; \
AJSTAT_ok_times=42; __cfduid=dd62c082ed82e3b0ea9f63f314b026e641526913323; 91username=fe1fccKc2Q%2BvIEc7xuOICsrmeW%2BCnkh94jcs8pZo9bRQPE0; \
CLIPSHARE=7od9k2abaktlg31mhpgk3lvhf5; __51cke__=; __utmc=50351329; user_level=1; EMAILVERIFIED=no; level=1; \
_gid=GA1.2.1763159004.1547994881; DUID=0ec4ECIaFZ2RUkOKBlD8%2BUAd1ZOWIsiEJisn1ch3PA0lXNDb; \
USERNAME=3a21VCxTN%2B4KjlPDPenGoKZumcBgxB3YKOmKHwM9gv4%2FEfU; __utma=50351329.1999180034.1495265586.1547994880.1547999423.180; \
__utmt=1; watch_times=10; __utmb=50351329.3.10.1547999423; \
__tins__3878067=%7B%22sid%22%3A%201547999425621%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201548001328800%7D; \
__51laig__=130; _gat=1'

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
    os.chdir("/home/evas/负阴抱阳/新建文件夹/")
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
    
    