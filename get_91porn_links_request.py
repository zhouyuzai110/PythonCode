#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
proxies = {'http': 'socks5://127.0.0.1:1080'}

raw_cookies = '__cfduid=de1d8545f55ead32d08ac2621c02320931495265581; evercookie_cache=<br/>; \
evercookie_png=<br/>; evercookie_etag=<br/>; l91lb91a=1; 91username=zyz110; _ga=GA1.2.1999180034.1495265586; \
CLIPSHARE=chl1g5bad552iee8hm8ajmt6v6; DUID=fed8f43EKjUKZYP%2Fqhc7O%2BVO7lyCTckDIcNH6eyZHd3iiLoc; \
USERNAME=1b112mG7A6sthz27zpTWFUWdHqhT3QwxImlyQCqFvmoX7JM; user_level=1; EMAILVERIFIED=no; level=1; \
__utma=50351329.1999180034.1495265586.1505564162.1505905167.24; __utmb=50351329.34.10.1505905167; __utmc=50351329; \
__utmz=50351329.1496750605.3.2.utmcsr=t.co|utmccn=(referral)|utmcmd=referral|utmcct=/bOL5FLj6iy; \
AJSTAT_ok_pages=33; AJSTAT_ok_times=22; __dtsu=1EE7044501C9D3587E14AC6702941105; watch_times=21'

cookies={}  
for line in raw_cookies.split(';'):  
    key,value = line.split('=',1)#1代表只分一次，得到两个数据  
    cookies[key]=value  

#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
        r = requests.get(url, headers = headers, proxies = proxies, cookies = cookies)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('source')
        for i in p:
            target_link = i.get('src')
            print target_link
    except Exception,e:
        print str(e)
        return None          



def main():

    while True:
        url = raw_input("the url is : ")
        get_hyper_links(url)
        

        
if __name__ == "__main__":
    main()  
    
    