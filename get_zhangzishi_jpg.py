# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import socket
import urllib
import urllib2
import codecs

import time, os

url = raw_input("the url is :")

#u"获取网页源码"
def get_page_source(url, timeout = 100, coding = None):
    try:
        socket.setdefaulttimeout(timeout)
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
        response = urllib2.urlopen(req)
        if coding is None:
            coding= response.headers.getparam("charset")
        if coding is None:
            page=response.read()
        else:
            page=response.read()
            page=page.decode(coding).encode('utf-8')
        return ["200",page]
    except Exception,e:
        print str(e)
        return [str(e),None]

#u"获取源码中得超链接"
def get_hyper_links(url, key_word):
    try:
        links = []
        data = get_page_source(url)
        if data[0] == "200":
            soup = BeautifulSoup(data[1])
            a = soup.find_all('a')
            for i in a:
                target_link = i.get('href')
                if target_link is not None :
                    if target_link.find(key_word) > 0:
                        links.append(target_link) 
                                   
        return links
    except Exception,e:
        print str(e)
        return None          


# if __name__ == "__main__":
# 	jpg_file = open("jpg.txt","a")
# 	for jpg_links in get_hyper_links(url, "jpg"):
# 		jpg_file.write(jpg_links)
# 		jpg_file.write("\n")
# 	jpg_file.close()

if __name__ == "__main__":
	os.chdir(u"D:\我的文档\Dropbox\Photo")  
	for jpg_links in get_hyper_links(url, "jpg"):
		conn = urllib.urlopen(jpg_links) 
		jpgname = str(time.time()) + ".jpg"
		f = open(jpgname,'wb')  
		f.write(conn.read())  
		f.close()  
		print('Pic Saved!') 
