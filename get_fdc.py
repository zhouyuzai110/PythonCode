#!/usr/bin/env python2
# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import codecs

import time, os, sys

# URL = 'http://zjjg.0557fdc.com:9555/xiaoqu/roominfo.aspx?dongid=4953&roomid=103'
dongid = sys.argv[1]
roomid_max = sys.argv[2]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
   

#u"获取源码中得信息"
def get_content(dongid, roomid):
    try:
        url = 'http://zjjg.0557fdc.com:9555/xiaoqu/roominfo.aspx\?dongid=%s&roomid=%s' %(dongid, roomid)
        r = requests.get(url, headers = headers)
        print url
        soup = BeautifulSoup(r.content, "html.parser")
        Labelxqmc = u'小区名称:' + soup.find(id = 'Labelxqmc').get_text()  
        Labelxzq = u'所属区域:' + soup.find(id = 'Labelxzq').get_text()
        Labeldongmc = u'栋名称:' + soup.find(id = 'Labeldongmc').get_text()
        Labelroommc = u'房号:' + soup.find(id = 'Labelroommc').get_text()
        Labelstatus = u'销售状态:' + soup.find(id = 'Labelstatus').get_text()
        Labeldong = u'栋住宅均价（元）:' + soup.find(id = 'Labeldong').get_text()
        Labellx = u'类型:' + soup.find(id = 'Labellx').get_text()
        Labelyxyongtu = u'房屋用途:' + soup.find(id = 'Labelyxyongtu').get_text()
        Labelhscs = u'换手次数:' + soup.find(id = 'Labelhscs').get_text()
        Labeljzmianji = u'建筑面积(平方米):' + soup.find(id = 'Labeljzmianji').get_text()
        Labelgongtan = u'公摊面积(平方米):' + soup.find(id = 'Labelgongtan').get_text()
        Labeltaonei = u'套内面积(平方米):' + soup.find(id = 'Labeltaonei').get_text()
        Labelckdj = u'参考单价(元/平方米):' + soup.find(id = 'Labelckdj').get_text()
        Labelckzj = u'参考总价(元):' + soup.find(id = 'Labelckzj').get_text()
        Labelbeiandate = u'备案时间:' + soup.find(id = 'Labelbeiandate').get_text()
        write_text = Labelxqmc + '\t' + Labelxzq + '\t' + Labeldongmc + '\t' + Labelroommc \
+ '\t' + Labelstatus + '\t' + Labeldong + '\t' + Labellx + '\t' + Labelyxyongtu \
+ '\t' + Labelhscs + '\t' + Labeljzmianji + '\t' + Labelgongtan + '\t' + Labeltaonei \
+ '\t' + Labelckdj + '\t' + Labelckzj + '\t' + Labelbeiandate + '\n'
        print write_text
        f = codecs.open('fdc.txt', 'a', 'utf-8')
        f.write(write_text)
        f.close()

def get_content_header(dongid, roomid):
    try:
        url = 'http://zjjg.0557fdc.com:9555/xiaoqu/roominfo.aspx\?dongid=%s&roomid=%s' %(dongid, roomid)
        r = requests.get(url, headers = headers)
        print url
        soup = BeautifulSoup(r.content, "html.parser")
        Labelxqmc = soup.find(id = 'Labelxqmc').get_text()  
        Labelxzq = soup.find(id = 'Labelxzq').get_text()
        Labeldongmc = soup.find(id = 'Labeldongmc').get_text()
        Labelroommc = soup.find(id = 'Labelroommc').get_text()
        Labelstatus = soup.find(id = 'Labelstatus').get_text()
        Labeldong = soup.find(id = 'Labeldong').get_text()
        Labellx = soup.find(id = 'Labellx').get_text()
        Labelyxyongtu = soup.find(id = 'Labelyxyongtu').get_text()
        Labelhscs = soup.find(id = 'Labelhscs').get_text()
        Labeljzmianji = soup.find(id = 'Labeljzmianji').get_text()
        Labelgongtan = soup.find(id = 'Labelgongtan').get_text()
        Labeltaonei = soup.find(id = 'Labeltaonei').get_text()
        Labelckdj = soup.find(id = 'Labelckdj').get_text()
        Labelckzj = soup.find(id = 'Labelckzj').get_text()
        Labelbeiandate = soup.find(id = 'Labelbeiandate').get_text()
        write_text_header = u'小区名称:' + '\t' + u'所属区域:' + '\t' + u'栋名称:' + '\t' + u'房号:' + '\t' + \
        u'销售状态:' + '\t' + u'栋住宅均价（元）:' + '\t' + u'类型:' + '\t' + u'房屋用途:' + '\t' + \
        u'换手次数:' + '\t' + u'建筑面积(平方米):' + '\t' + u'公摊面积(平方米):' + '\t' + u'套内面积(平方米):' + '\t' + \
        u'参考单价(元/平方米):' + '\t' + u'参考总价(元):' + '\t' + u'备案时间:' + '\n'
        write_text = Labelxqmc + '\t' + Labelxzq + '\t' + Labeldongmc + '\t' + Labelroommc \
+ '\t' + Labelstatus + '\t' + Labeldong + '\t' + Labellx + '\t' + Labelyxyongtu \
+ '\t' + Labelhscs + '\t' + Labeljzmianji + '\t' + Labelgongtan + '\t' + Labeltaonei \
+ '\t' + Labelckdj + '\t' + Labelckzj + '\t' + Labelbeiandate + '\n'
        f = codecs.open('fdc.txt', 'a', 'utf-8')
        f.write(write_text_header)
        f.write(write_text)

        f.close()
    except Exception,e:
        print str(e)
        return None          





def main():
    for i in range(1, int(roomid_max) + 1):
        get_content_header(dongid, i)
        
        
    
if __name__ == "__main__":
    main()  
