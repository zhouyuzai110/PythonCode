#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs
from htmllib import HTMLParser 
import HTMLParser
import time, os
import re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

pattern = re.compile(r'http://.{2,3}.pstatp.com/large/.{20}')
pattern_tu = re.compile(r'http:\\\\/\\\\/.{2,3}.pstatp.com\\\\/origin\\\\/.{20}')
pattern_tu1 = re.compile(r'http:\\\\/\\\\/.{2,3}.pstatp.com\\\\/origin\\\\/pgc-image\\\\/.{32}')
pattern_tu2 = re.compile(r'http://.{2,3}.pstatp.com/large/pgc-image/.{23}')
pattern_tu3 = re.compile(r'http://.{2,3}.pstatp.com/large/dfic-imagehandler/.{36}')
pattern_tu4 = re.compile(r'http:\\\\/\\\\/.{2,3}.pstatp.com\\\\/origin\\\\/pgc-image\\\\/.{23}')
pattern_tu5 = re.compile(r'http://.{2,3}.pstatp.com/large/pgc-image/.{32}')
link_long = 45

#u"获取源码中得超链接"
def get_hyper_links_toutiao(url):

    try:
        r = requests.get(url, headers = headers)
        html_parser = HTMLParser.HTMLParser()
        txt = html_parser.unescape(r.content.decode('utf-8'))
        soup = BeautifulSoup(r.content, "html.parser")
        p = soup.find_all('script')
        links = []
        for i in p:
            if "articleInfo:" in i.get_text():
                links_articleInfo_1 = re.findall(pattern, i.get_text())
                links.extend(links_articleInfo_1)

                links_articleInfo_2 = re.findall(pattern_tu2, i.get_text())
                links.extend(links_articleInfo_2)

                links_articleInfo_3 = re.findall(pattern_tu3, i.get_text())
                links.extend(links_articleInfo_3)

                links_articleInfo_5 = re.findall(pattern_tu5, i.get_text())
                links.extend(links_articleInfo_5)

                links = [x for x in links if len(x) > link_long]
                return list(set(links))

            elif "galleryInfo" in i.get_text():
                target_links_tu4 = re.findall(pattern_tu4, i.get_text())
                for j in target_links_tu4:
                    target_link_tu4 = j.replace('\\\\/','/')
                    links.append(target_link_tu4)

                target_links_tu = re.findall(pattern_tu, i.get_text())
                for jj in target_links_tu:
                    target_link_tu = jj.replace('\\\\/','/')
                    links.append(target_link_tu)

                target_links_tu1 = re.findall(pattern_tu1, i.get_text())
                for jjj in target_links_tu1:
                    target_link_tu1 = jjj.replace('\\\\/','/')
                    links.append(target_link_tu1)
                       
                links = [x for x in links if len(x) > link_long]                   
                return list(set(links))
    except Exception,e:
        print str(e)
        return None          


def get_hyper_links_snssdk(url):

    try:
        links = []
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('img')
        for i in p:
            target_link = i.get('alt-src')
            if target_link is not None :
                links.append(target_link) 

        return links
    except Exception,e:
        print str(e)
        return None 


def get_title(url):
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content,"html.parser")
    title = soup.find('title').get_text()
    return title


#u"将图片写入文件"
def write_into_files(jpgname,url):

    conn = requests.get(url, stream = True, timeout = 5, headers = headers)
    f = open(jpgname,'wb')  
    f.write(conn.raw.read())  
    f.close()  



def main():

    while True:
        os.chdir("/home/evas/Dropbox/Photo/")
        url = raw_input("the url is : ")
        if 'toutiao' in url:
            links = get_hyper_links_toutiao(url)
        elif 'snssdk' in url:
            links = get_hyper_links_snssdk(url)
        title = get_title(url)
        total_num = len(links)
        num = 1
        print title
        for link in links:
            try:
                # jpgname = title + str(time.time()) + ".jpg"
                jpgname = title + str(time.time())
                write_into_files(jpgname,link)
                print('%s of %s Pic Saved!') %(num, total_num)
                num += 1
            except Exception, e:
                print str(e)

        
if __name__ == "__main__":
    main()  
    
    