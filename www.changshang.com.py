#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        


def get_content(url):

    content_list = []
    try:
        r = requests.get(url, timeout = 5, headers = headers)
        soup = BeautifulSoup(r.content, "html.parser", from_encoding = 'utf8')
        content = soup.find_all('td')
        for i in content:
            target_text = i.get_text().replace('\t', '').replace(' ', '')
            content_list.append(target_text)

        mysql_data = '-'.join(set(content_list))  
        print mysql_data
    except Exception,e:
        print str(e)
        return None          

def mysql_con():
    pass


def main():
    url = 'http://www.changshang.com/member/web/contactus.aspx?id=29094'
    get_content(url)
    

        
if __name__ == "__main__":

    main()  
	
	