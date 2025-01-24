from bs4 import BeautifulSoup
import requests
import sys
import time

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

BASEURL = 'http://paper.people.com.cn/rmrb/html/'
OUT_FILE_NAME = 'rmrb.html'


def get_title():
    riqi = make_riqi()
    # with open(OUT_FILE_NAME, "r+") as f:
    #     f.truncate()
    write_into_file('''<link rel="stylesheet" type="text/css"\\
        href="https://weekly.manong.io/asset/mweekly.css"/>''')
    for i in range(1, 21):
        if i < 10:
            target_link = BASEURL + riqi + \
                'nbs.D110000renmrb_' + '0' + str(i) + '.htm'
        else:
            target_link = BASEURL + riqi + \
                'nbs.D110000renmrb_' + str(i) + '.htm'
        try:
            get_origin(target_link, riqi, i)
        except Exception as e:
            pass


def make_riqi():
    if len(sys.argv) < 2:
        a = str(time.strftime("%Y%m%d", time.localtime()))
    else:
        a = str(sys.argv[1])
    riqi = a[0:4] + '-' + a[4:6] + '/' + a[6:] + '/'
    return riqi


def get_origin(url, riqi, banci):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    left_ban = soup.find('p', {'class': "left ban"}).get_text()
    remark_riqi = riqi[0:4] + riqi[5:7] + riqi[8:10]
    all_a = soup.find_all('a')
    for i in all_a:
        if 'nw' in i.get('href') and len(i.get_text()) > 1:
            # write_into_db_list = []
            i_text = '[' + remark_riqi + left_ban + '] ' + i.get_text()
            i_url = BASEURL + riqi + i.get('href')
            # write_into_db_list.append(i_url)
            # write_into_db_list.append(i_text)
            nian_yue_ri = riqi[0:4] + '\t' + riqi[5:7] + \
                '\t' + riqi[8:10] + '\t' + str(banci)
            target_text = i_text + '\t' + i_url + '\t' + url + '\t' + nian_yue_ri
            # target_text_html = '<li><a href="' + i_url + '">' + i_text + '</a></li>'
            target_text_html = '<h4><a href="' + i_url + '">' + i_text + '</a></h4><p></p>'
            # print(target_text)
            write_into_file(target_text_html)
            # write_into_db(write_into_db_list)


def write_into_file(target_text):

    with open(OUT_FILE_NAME, 'a', encoding='utf-8') as write_file:
        write_file.write(target_text + '\n')


# def write_into_db(target_text):
#     conn = sqlite3.connect('rmrb.db')
#     print("Opened database successfully")
#     cursor = conn.cursor()
# # 插入数据
#     sql = "INSERT INTO rmrb_links(link_url, link_title) VALUES(?, ?)"
#     cursor.execute(sql, target_text)
#     conn.commit()
#     conn.close()

# def create_db():
#     conn = sqlite3.connect('rmrb.db')
#     print("Opened database successfully")
#     cursor = conn.cursor()
#     sql = 'CREATE TABLE rmrb_links(id integer PRIMARY KEY autoincrement, link_url varchar(200), link_title varchar(200))'
#     cursor.execute(sql)
#     conn.commit()

# def select_db():
#     conn = sqlite3.connect('rmrb.db')
#     print("Opened database successfully")
#     cursor = conn.cursor()
#     sql = "select * from rmrb_links"
#     values = cursor.execute(sql)
#     for i in values:
#         print(i)

get_title()
# select_db()
# create_db()
