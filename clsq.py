# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        

#u"获取源码中得超链接"
def get_hyper_links(url, key_words):

    try:
    	links = []
        r = requests.post(url, timeout = 5, headers = headers)
        time.sleep(1)
        soup = BeautifulSoup(r.content,"html.parser")
        p = soup.find_all('input')
        for i in p:
            target_link = i.get('src')
            if target_link is not None :
                if target_link.find(key_words[0]) or target_link.find(key_words[1]) > 0:
                    if "imageView" not in target_link and "weixin" not in target_link\
                    and "330x200" not in target_link and "600x120" not in target_link\
                    and "footer" not in target_link:
                    	links.append(target_link) 
        return links
    except Exception,e:
        print str(e)
        return None          

# def write_into_files(url):

#     conn = urllib.urlopen(url) 

#     jpgname = str(time.time()) + ".jpg"
#     f = open(jpgname,'wb')  
#     f.write(conn.read())  

#     f.close()  

def write_into_files(url):

    conn = requests.post(url, stream = True, headers = headers, timeout = 5) 
    time.sleep(1)
    jpgname = str(time.time()) + ".jpg"
    f = open(jpgname,'wb')  
    f.write(conn.raw.read())  

    f.close()  




def main():

    while True:
        os.chdir("/home/evas/")
        url = raw_input("the url is :")
        links = get_hyper_links(url,["jpg","jpeg"])
        if links is not None:
            for link in links:
                try:
                    write_into_files(link)
                    print('Pic Saved!') 
                except Exception, e:
                    print str(e)

        
if __name__ == "__main__":

    main()  
	
	