#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}


def write_into_files(url):

    conn = requests.get(url, timeout = 5, headers = headers)
    jpgname = str(time.time()) + ".mp4"
    f = open(jpgname,'wb')  
    f.write(conn.content)  

    f.close()  


def main():

    while True:
        os.chdir("/home/evas/")
        url = raw_input("the url is :")
        if url == '111':
        	break
        else:

	        try:
	            write_into_files(url)
	            print('Mp4 Saved!') 
	        except Exception, e:
	            print str(e)

        
if __name__ == "__main__":

    main()      