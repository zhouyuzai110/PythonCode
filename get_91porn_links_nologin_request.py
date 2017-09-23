#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
proxies = {'http': 'socks5://127.0.0.1:1080'}



#u"获取源码中得超链接"
def get_hyper_links(url):

    try:
        r = requests.get(url, headers = headers, proxies = proxies)
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
    
    