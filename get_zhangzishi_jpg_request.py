# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import urllib
import requests
import codecs

import time, os



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
        r = requests.get(url)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('img')
        for i in p:
            target_link = i.get('src')
            if target_link is not None :
                if target_link.find(key_word) > 0:
                    if "imageView" not in target_link and "weixin" not in target_link\
                    and "330x200" not in target_link and "600x120" not in target_link\
                    and "footer" not in target_link:
                    	links.append(target_link) 
        return links
    except Exception,e:
        print str(e)
        return None          

def write_into_files(url):

    conn = urllib.urlopen(url) 
    jpgname = str(time.time()) + ".jpg"
    f = open(jpgname,'wb')  
    f.write(conn.read())  
    f.close()  


def main():

    while True:
        os.chdir("/home/evas/")
        url = raw_input("the url is :")
        links = get_hyper_links(url,"jpg")
        for link in links:
            try:
                write_into_files(link)
                print('Pic Saved!') 
            except Exception, e:
                print str(e)

        



if __name__ == "__main__":

    main()  
	
	