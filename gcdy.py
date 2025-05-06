import json
import re

import requests
from bs4 import BeautifulSoup

re_words = ['.*摄$', '.*摄）$', '.*供图$', '\n', '\u3000', '^△.*', ' ', '.*来源：.*作者：.*', '.*新华社发$', ' ', '新华社.*电.*']

key_words = ['点击观看视频', '共产党员网分享打印', '2020年全国两会', '2020全国两会', '决胜全面建成小康社会', '坚决打赢疫情防控阻击战', '党的二十大报告学习辅导百问']

biaodian = '。；;a\n…”!！—？：）'
origin_list = []

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

url = 'http://www.pbc.gov.cn'

# url = 'https://www.12371.cn/2023/10/09/ARTI1696813769083107.shtml'


def get_content(url, headers):
    try:
        if '12371' in url:
            get_12371(url, headers)
        elif 'qstheory' in url:
            get_qiushi(url, headers)
        elif 'xuexi' in url:
            get_xxqg(url, headers)
        elif 'news.cn' in url:
            get_news_cn(url, headers)
        elif 'www.gov.cn' in url:
            get_gwy(url, headers)
        elif 'www.ah.gov.cn' in url:
            get_szf(url, headers)
        elif 'www.wuhu.gov.cn' in url:
            get_whzf(url, headers)
        elif 'paper.people.com.cn/rmrb' in url:
            get_rmrb(url, headers)
        elif 'people.com.cn' in url:
            get_rmw(url, headers)
        elif 'ccdi' in url:
            get_ccdi(url, headers)
        elif 'ccps' in url:
            get_ccps(url, headers)
        elif 'blog.sina' in url:
            get_sina_blog(url, headers)
        elif 'pbc.gov.cn' in url:
            get_pbc(url, headers)

    except Exception as e:
        print(str(e))
        return None


def get_12371(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        print(soup)
        title = soup.find('title').get_text().replace('_共产党员网', '').replace(' ', '').replace('\r\n', '')
        # h2 = soup.find('h2').get_text().replace('\t', '').replace('\r\n', '')

        author = soup.find('h2', {
            'class': "zz_title"
        }).get_text().replace('\t', '').replace('\r\n', '').replace('\n', '').replace(' ', '') + soup.find(
            'h2', {
                'class': "small_title"
            }).get_text().replace('\t', '').replace('\r\n', '').replace('\n', '').replace(' ', '')
        if len(author) > 1:
            origin_list.append('aaa' + author + '：' + title)
            # print('aaa' + author + '：' + title)
        else:
            origin_list.append('aaa' + title)
            # print('aaa' + title)
        # print(title)
        # print('author：' + author + '：author')
        # main_content = soup.find('div', {'id': "font_area"}).find_all('p')
        main_content = soup.find_all('p')
        print(main_content)
        for i in main_content:
            print(i)
            if len(i.get_text()) > 0:
                i_text = i.get_text()
            else:
                i_text = i.find('img').get('alt')
            if i_text == '　　延伸阅读':
                break
            print(i_text)
            origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_pbc(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        print(soup)
        # title = soup.find('title').get_text().replace(' ', '').replace('\r\n', '')
        # origin_list.append('aaa' + title)

        main_content = soup.find('td', {'class': "content"}).find_all('p')
        print(main_content)
        for i in main_content:
            print(i)
            if len(i.get_text()) > 0:
                i_text = i.get_text()
            else:
                i_text = i.find('img').get('alt')
            if i_text == '　　延伸阅读':
                break
            print(i_text)
            origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_news_cn(url, headers):

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    title = soup.find('span', {'class': "title"}).get_text().replace(' ', '').replace('\r\n', '')
    origin_list.append('aaa' + title)
    print(title)
    try:
        main_content = soup.find('div', id="detail").find_all('p')
        print(main_content)
        for i in main_content:
            if len(i.get_text()) > 0:
                i_text = i.get_text()

            print(i_text)
            origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_qiushi(url, headers):

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    title = get_qiushi_title(url, soup)
    origin_list.append(title)
    print(title)
    try:
        main_content = soup.find_all('p')
        for i in main_content:
            if len(i.get_text()) > 0:
                i_text = i.get_text()
                print(i_text)
                origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_qiushi_title(url, soup):

    if 'dukan' in url or 'wp' in url or 'yaowen' in url or 'laigao' in url:
        title = soup.find('title').get_text().replace(' - 求是网', '').replace(' ', '').replace('\r\n', '')
        h2 = soup.find('h2').get_text().replace('\r\n', '').replace(' ', '')
        author = soup.find_all('span', {'class': "appellation"})
        target_author = ''
        for item in author:
            if '作者：' in item.get_text():
                target_author = item.get_text().replace(' ', '').replace('作者：', '').replace('\r\n', '')
        title = 'aaa' + target_author + '：' + title + h2

    if 'llwx' in url or 'zhuanqu' in url or 'zdwz' in url or 'qshyjx' in url:
        title = soup.find('title').get_text().replace(' - 求是网', '').replace(' ', '').replace('\r\n', '')
        div_author = soup.find('div', {'class': "headtitle"}).stripped_strings
        div_author = [text for text in div_author][-1]
        target_author = div_author.replace('来源： ', '').replace('　作者', '').replace('： ', '')
        title = 'aaa' + target_author + '：' + title

    if 'qstheory' in url:
        title = soup.find('title').get_text().replace(' - 求是网', '').replace(' ', '').replace('\r\n', '')
        h2 = soup.find('h2').get_text().replace('\r\n', '').replace(' ', '')
        author = soup.find_all('span', {'class': "appellation"})
        target_author = ''
        for item in author:
            if '作者：' in item.get_text():
                target_author = item.get_text().replace(' ', '').replace('作者：', '').replace('\r\n', '')
        title = 'aaa' + target_author + '：' + title + h2

    return title


def get_rmw(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        target_tag_text = ''
        if soup.find('p', {'class': 'sou1'}) is not None:
            sou1 = soup.find('p', {'class': 'sou1'}).get_text() + '：'
        else:
            sou1 = ''
        for tag in ['h1', 'h2', 'h3', 'h4']:
            if soup.find(tag) is not None:
                tag_text = soup.find(tag).get_text()
                if len(tag_text) > 1:
                    target_tag_text = target_tag_text + tag_text + '+'

        if len(sou1) > 1:
            title = sou1 + target_tag_text
        else:
            title = target_tag_text
        origin_list.append('aaa' + title)
        print(title)
        main_content = soup.find_all('p', {'style': "text-indent: 2em;"})
        if main_content is not None:
            for i in main_content:
                if len(i.get_text()) > 0:
                    i_text = i.get_text().replace('\t', '')
                    print(i_text)
                    origin_list.append(i_text)
        main_content_new = soup.find('div', {'id': "rwb_zw"}).find_all('p')
        if main_content_new is not None:
            for j in main_content_new:
                if len(j.get_text()) > 0:
                    j_text = j.get_text().replace('\t', '')
                    print(j_text)
                    origin_list.append(j_text)

    except Exception as e:
        print(str(e))
        return None


def get_rmrb(url, headers):

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('h1').get_text()
        author = soup.find('p', {'class': "sec"}).get_text().split('\r\n')[1]
        origin_list.append('aaa' + title)
        if '人民日报' not in author:
            origin_list.append(author)
        main_content = soup.find('div', {'id': "articleContent"}).find_all('p')
        if main_content is not None:
            for i in main_content:
                if len(i.get_text()) > 0:
                    i_text = i.get_text()
                    print(i_text)
                    origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_ccdi(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('h2', {'class': "tit"}).get_text().replace('\n', '')
        print(title)
        origin_list.append('aaa' + title)
        main_content = soup.find_all('p')
        for i in main_content:
            if len(i.get_text()) > 0:
                i_text = i.get_text()
                print(i_text)
                origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_gwy(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('title').get_text().replace('_总理_中国政府网', '')
        print(title)
        origin_list.append('aaa' + title)
        main_content = soup.find_all('p', {"style": "text-indent: 2em; font-family: 宋体; font-size: 12pt;"})
        for i in main_content:
            if len(i.get_text()) > 0:
                i_text = i.get_text()
                print(i_text)
                origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_szf(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('title').get_text().replace('_安徽省人民政府', '')
        print(title)
        origin_list.append('aaa' + title)
        main_content = soup.find_all('p', {"align": ""})
        for i in main_content:
            i_text = i.get_text()
            if '精心设计了一个小型数据库' not in i_text and '更是老百姓的会' not in i_text:
                i_text = re.sub(r'（.*）', '', i_text)
                i_text = re.sub(r'\(.*\)', '', i_text)
                print(i_text)
                origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_whzf(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('title').get_text().replace('_芜湖市政务公开网', '')
        print(title)
        origin_list.append('aaa' + title)
        main_content = soup.find_all('p', {"align": ""})
        for i in main_content:
            i_text = i.get_text()
            i_text = re.sub(r'（.*）', '', i_text)
            i_text = re.sub(r'\(.*\)', '', i_text)
            print(i_text)
            origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def get_ccps(url, headers):
    links = creat_ccps_link(url)
    print(links[0])
    origin_list.append(links[0])
    for target_link in links[1:]:
        r = requests.get(target_link, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        # main_content = soup.find_all('p', {"align": "justify"})
        main_content = soup.find('div', {"class": "Custom_UnionStyle"}).find_all(['div', 'p'])
        for i in main_content:
            i_text = i.get_text()
            print(i_text)
            origin_list.append(i_text)


def get_sina_blog(url, headers):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.find('h2').get_text()
        print(title)
        origin_list.append('aaa' + title)
        main_content = soup.find('div', {"id": "sina_keyword_ad_area2"}).find_all(['span', 'p'])
        for i in main_content:
            i_text = i.get_text()
            print(i_text)
            origin_list.append(i_text)

    except Exception as e:
        print(str(e))
        return None


def creat_ccps_link(url, headers):
    """
    创建链接列表，针对给定的URL生成相关页面链接。
    
    参数:
    url: 字符串，目标网页的URL。
    headers: 字典，HTTP请求头信息。
    
    返回:
    list: 包含生成的链接的列表。
    """
    # 初始化链接列表
    target_links = []

    # 分割URL以重构页面路径
    url_content = url.split('/')
    url_remake = '/'.join(url_content[0:-1]) + '/'

    # 发送GET请求获取网页内容
    r = requests.get(url, headers=headers)

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(r.content, "html.parser")

    # 提取网页标题，并生成第一个链接
    title = soup.find('title').get_text()
    target_links.append('aaa' + title)

    # 查找页面中的“内容页”div，以确定是否需要生成分页链接
    div_content_page = soup.find('div', {'class': "content-page"})

    # 如果内容页文本长度小于2，说明没有分页，直接返回当前URL
    if len(div_content_page.get_text()) < 2:
        target_links.append(url)
        return target_links

    else:
        # 找到所有a标签，筛选出分页链接
        a_list = soup.find_all('a')
        for i in a_list:
            # 如果a标签文本包含“页”，但不包含“首页”，则认为是分页链接
            if '页' in i.get_text() and '首页' not in i.get_text():
                sub_link = i.get('href')
                # 将分页链接添加到目标链接列表中
                target_links.append(url_remake + sub_link)

        return target_links


def get_xxqg(url, headers):
    """
    从指定的URL获取学习强国文章的标题和内容。
    
    :param url: 文章的URL地址
    :param headers: 请求头部信息，用于模拟浏览器访问
    :return: None
    """
    try:
        # 创建学习强国文章链接
        link = creat_xxqg_link(url)
        # 发送GET请求获取文章页面内容
        r = requests.get(link, headers=headers)
        # 处理返回的JSON数据，去除回调函数名称
        json_data = r.text.replace('callback(', '').replace('})', '}')
        # 解析处理后的JSON数据
        xuexi_json = json.loads(json_data)
        # 提取文章标题
        title = xuexi_json["title"]
        print(title)
        # 将标题添加到origin_list列表中
        origin_list.append('aaa' + title)
        # 提取并分割文章的规范化内容，形成单词列表
        content_list = xuexi_json['normalized_content'].split(' ')
        print(content_list)
        # 将内容单词列表追加到origin_list中
        origin_list.extend(content_list)

    except Exception as e:
        # 打印异常信息
        print(str(e))
        # 出现异常时返回None
        return None


def creat_xxqg_link(url):
    """
    根据给定的URL生成一个特定格式的链接。

    该函数通过正则表达式从URL中提取一个数字，然后将这个数字用于构建一个新的链接。
    这个新的链接是学习平台“学习强国”的数据应用链接，用于获取特定数据应用的JavaScript文件。

    参数:
    url (str): 需要处理的原始URL，这个URL应该包含一个数字，该数字代表了学习平台上的数据应用ID。

    返回:
    str: 生成的链接，格式为'https://boot-source.xuexi.cn/data/app/数字.js'，其中数字是从原始URL中提取的。
    """
    # 使用正则表达式从URL中提取数字
    result = re.search(r'(\d+)', url)
    # 获取正则表达式匹配的数字部分
    result_num = result.group(1)
    # 构建新的链接
    link = 'https://boot-source.xuexi.cn/data/app/' + str(result_num) + '.js'
    return link


def replace_str(item):
    for re_word in re_words:
        item = re.sub(re_word, "", item)
        for key_word in key_words:
            if item == key_word:
                item = re.sub(key_word, "", item)
    if 'aaa' in item:
        item = item.replace(item, "\n\n" + item + 'aaa' + '\n')
    if len(item) >= 1 and item[-1] not in biaodian:
        item = item.replace(item, 'bbb' + item + 'bbb')
    return item


def creat_out_list(origin_list):
    out_list = []
    for i in origin_list:
        return_item = replace_str(i)
        if return_item is not None and return_item != '':
            out_list.append(return_item)
    liebiao_quchong(out_list)
    return out_list


def liebiao_quchong(lists):
    for i in range(len(lists) + 1):
        if i < len(lists) - 1 and lists[i] == lists[i + 1]:
            lists[i] = re.sub('.*', "", lists[i])
            # lists[i + 1] = re.sub('.*', "", lists[i + 1])


def getGcdyZxfbContent(links, headers):

    for link in links:
        get_content(link, headers)
    out_list = creat_out_list(origin_list)
    return_out_list = [x for x in out_list if x != '']
    origin_list.clear()
    return return_out_list


if __name__ == '__main__':
    get_content(url, headers)
