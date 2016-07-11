#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        

#u"获取源码中得超链接"
def get_bbs_text(url):

    re_text = []
    try:
        r = requests.post(url, timeout = 5, headers = headers)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('td',{"class":"t_f"})
        for i in p:
            target_text = i.get_text()
            print target_text
            re_text.append(target_text)
        return re_text    
    except Exception,e:
        print str(e)
        return None          



def write_into_files(url):

    conn = get_bbs_text(url) 
    for text in conn:
        with open ("cd",'a') as f:
            text = text.encode("UTF-8")
            f.write(text)
            f.write("\n")


def main():

    os.chdir("/home/evas/")
    url = raw_input("the url is :")
    write_into_files(url)
    

        
if __name__ == "__main__":

    main()  
	
	