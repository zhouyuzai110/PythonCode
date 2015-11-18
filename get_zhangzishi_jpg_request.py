# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import urllib
import requests
import codecs

import time, os

url = raw_input("the url is :")
zi_fu_chuan = ["imageView", "weixin", "330x200", "600x120", "footer"]
r = requests.get(url)

# #u"获取源码中得超链接"
# def get_hyper_links(url, key_word):
#     try:
#     	links = []
#         soup = BeautifulSoup(r.content)
#         a = soup.find_all('a')
#         for i in a:
#             target_link = i.get('href')
#             if target_link is not None :
#                 if target_link.find(key_word) > 0:
#                     links.append(target_link) 
#         return links
#     except Exception,e:
#         print str(e)
#         return None          

#u"获取源码中得超链接"
def get_hyper_links(url, key_word):
    try:
    	links = []
        soup = BeautifulSoup(r.content)
        p = soup.find_all('img')
        for i in p:
            target_link = i.get('src')
            if target_link is not None :
                if target_link.find(key_word) > 0:
                    if "imageView" not in target_link and "weixin" not in target_link\
                    and "330x200" not in target_link and "600x120" not in target_link \
                    and "footer" not in target_link:
                    	links.append(target_link) 
        return links
    except Exception,e:
        print str(e)
        return None          


if __name__ == "__main__":
	os.chdir(u"D:\我的文档\Dropbox\Photo")  
	for jpg_links in get_hyper_links(url, "jpg"):
		conn = urllib.urlopen(jpg_links) 
		jpgname = str(time.time()) + ".jpg"
		f = open(jpgname,'wb')  
		f.write(conn.read())  
		f.close()  
		print('Pic Saved!')         
