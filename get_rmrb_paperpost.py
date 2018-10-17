#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs
import HTMLParser
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}

def create_hyper_links_rmrb():
    
    if len(sys.argv) < 2:
        ymd = time.localtime()
        rmrb_year = str(ymd[0])
        rmrb_month = str(ymd[1])
        rmrb_day = str(ymd[2])
        if len(rmrb_month) < 2:
            rmrb_month = "0" + rmrb_month
        if len(rmrb_day) < 2:
            rmrb_day = "0" + rmrb_day
        rmrb_date = rmrb_year + "-" + rmrb_month + "-" + rmrb_day
        rmrb_link = "http://paperpost.people.com.cn/all-rmrb-" + rmrb_date + ".html"
        print rmrb_link
        return rmrb_link
    else:
        rmrb_link = "http://paperpost.people.com.cn/all-rmrb-" + sys.argv[1] + ".html"
        return rmrb_link
   

#u"获取源码中得超链接"
def get_hyper_links_rmrb(url):

    try:
        r = requests.get(url, headers = headers)
        # html_parser = HTMLParser.HTMLParser()
        # txt = html_parser.unescape(r.content.decode('utf-8'))
        soup = BeautifulSoup(r.content, "html.parser")
        p = soup.find_all('a')
        links = []
        
        for i in p:
            rmrb_article = i.get_text()
            rmrb_link = i.get('href')
            rmrb_article_link = rmrb_article + '\n' + rmrb_link
            links.append(rmrb_article_link)
        return links
    except Exception, e:
            print str(e)


def write_into_files(url):
    
    try: 
        links = get_hyper_links_rmrb(url)
        for i in links:
            f = open("rmrb",'a')
            f.write("\n")  
            f.write(i) 
            f.close()  

    except Exception,e:
        print str(e)
        return None


def main():

    try:
        rmrb_url = create_hyper_links_rmrb()
        # rmrb_url = "http://paperpost.people.com.cn/all-rmrb-2018-10-17.html"
        write_into_files(rmrb_url)

    except Exception, e:
        print str(e)

if __name__ == "__main__":
    main()  