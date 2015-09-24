# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib2
import MySQLdb


URLLINK = "http://trend.caipiao.163.com/11xuan5/?selectDate=7"


def get_pageage_source(URLLINK, coding = None):
    try:
        req = urllib2.Request(URLLINK)
        req.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
        response = urllib2.urlopen(req)
        if coding is None:
            coding = response.headers.getparam("charset")
        if coding is None:
            page = response.read()
        else:
            page = response.read()
            page = page.decode(coding).encode('utf-8')
        return ["200", page]
    except Exception,e:
        print str(e)
        return [str(e),None]

def get_source_number():
    try:
        data = get_pageage_source(URLLINK)
        if data[0] == "200":
            soup = BeautifulSoup(data[1])
            for line in soup.find_all("tr"):
                qi_hao = line.get("data-period")
                kai_jiang_hao = line.get("data-award")
                if qi_hao is not None and kai_jiang_hao is not None:
                    kjh_list = kai_jiang_hao.split()
                    prelist = [qi_hao, kjh_list]
                    insert_list = [prelist[0], prelist[1][0], prelist[1][1], prelist[1][2], prelist[1][3], prelist[1][4]]
                    mysql.dbconn()
                    print  "========== Conn To MySQL Database, Please Waiting =========="
                    sql = 'INSERT INTO `cpdata`(`orderid`, `one`, `two`, `three`, `four`, `five`) VALUES (%s,%s,%s,%s,%s,%s)'
                    mysql.cursor.execute(sql,insert_list)
                    mysql.conn.commit()
                    print "========== Success insert into cpdata %s==========" %qi_hao
                    mysql.dbClose()
    except Exception,e:
        print str(e)
        return None

class MySQLdb123:

    def __init__(self):
        self.host = 'localhost'
        self.user = "root"
        self.passwd = "zhouyuzai110"
        self.db = "cpdata"
        self.port = 3306

    def dbconn(self):
        try:
            self.conn = MySQLdb.connect(self.host, self.user, self.passwd, self.db, self.port)
        except MySQLdb.Error,e:
            errormsg = 'Cannot connect to server\nERROR (%s): %s' %(e.args[0],e.args[1])
            print errormsg
        self.cursor = self.conn.cursor()


    def dbClose(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    mysql = MySQLdb123()
    get_source_number()
