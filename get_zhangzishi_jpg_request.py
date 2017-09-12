#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os



   

#u"获取源码中得超链接"
def get_hyper_links(url, key_word):

    try:
        links = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('img')
        for i in p:
            target_link = i.get('src')
            if target_link is not None :
                if target_link.find(key_word) > 0:
                    if "imageView" not in target_link and "weixin" not in target_link\
                    and "330x200" not in target_link and "600x120" not in target_link\
                    and "footer" not in target_link and '&w=240&h=180' not in target_link\
                    and '&w=120&h=120' not in target_link and '&w=100&h=75' not in target_link\
                    and 'qrcode_for_gh' not in target_link:
                        links.append(target_link) 
        return links
    except Exception,e:
        print str(e)
        return None          

def get_title(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    title = soup.find('h1', {'class':"article-title"}).get_text()
    return title


#u"将图片写入文件"
def write_into_files(jpgname,url):

    conn = requests.get(url, stream = True, timeout = 5)
    f = open(jpgname,'wb')  
    f.write(conn.raw.read())  
    f.close()  



def main():

    while True:
        os.chdir("/home/evas/Dropbox/Photo/")
        url = raw_input("the url is : ")
        links = get_hyper_links(url,"jpg")
        title = get_title(url)
        for link in links:
            try:
                jpgname = title + str(time.time()) + ".jpg"
                write_into_files(jpgname,link)
                print('Pic Saved!') 
            except Exception, e:
                print str(e)

        
if __name__ == "__main__":
    main()  
    
    