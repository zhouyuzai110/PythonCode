# from turtle import title
import os
from typing import List

import requests
from bs4 import BeautifulSoup

cookie = 'acw_tc=ac11000117480554457588212e007b928291258dd9fb00f6caccc9d1847a8c; JSESSIONID=2AEE9074CBFDCA83D7E424E516CF7D2A; SERVERID=b6e8b125b75f5dba425d2c6ba8a9a6c1|1748055548|1748055446; Hm_lvt_ea8e1f649766983f7078bdf6db3e61da=1748055551; Hm_lpvt_ea8e1f649766983f7078bdf6db3e61da=1748055551; HMACCOUNT=1A0A8E190BB1F97C; ssxmod_itna=eqGxRiDtqmqiq0IxYjKBK4xQqqWqijtDRDl4BtGR/DITe7=GFQDCrLUC0RohAuyh2qqm7iGnDDl=AqoDSxD=7DK4GTmG6uBDY7SQAhbqF7QGmhtiYAnhqcdM7Yl7mfastZS9mni40aDbqDyn7AxK4GGA4GwDGoD34DiDDPfD03Db4D+UliD7xbdcmTYaePDQ4GyDitDKqPbxG3D04bKbkb4DDXQR7G9KDGWGQuVWPPFxGt=RldYx0UaDBLt+IDYxDtEEIGNuCgXDKoPrPaDtqD9zZRDO1Ioq1uqx9Q5iRD5Y2YqbGmtWbwxmG5jxYGN5WDGmwZ2N2DhG7Yz0GwmXo8eDDcrYiO0vrtYeY2BQHSGnS85oByb/5ej5b7D1tRxVb5+GeObtR+NiTiDbV4bx60OK+/7GDD; ssxmod_itna2=eqGxRiDtqmqiq0IxYjKBK4xQqqWqijtDRDl4BtGR/DITe7=GFQDCrLUC0RohAuyh2qqm7iGeDAYg75ExYYD7pxP7DpwK=DBq4WOC1iYMnU1bDc2GjIhx22g0PS4o3BjUhE2RMjRStiuz0A5Q2hKsq8iGgDa+cr7aDSBs1PO80CHmhh5OvOoGjOPqlZgD1Rysa=iOxUwOCivI8Q9DinAIUxI+W3pev8xmaOAPDIi5ipi6+Phs2ExeOOi5o3wqKHvTa1omimGPwRrHdE75CxT5p3E2RDMFCFHWrrk8rrYw8exnhk3ZoIHFnH3RoKVDptBGVriqt0SEh00NAnIPIAtAp5fhtG0Sgm39poS=D4P1j0DSi48YcOQvpP0rYLx5q92XeK=7GRxmZWuN26Z7hR6Yh2YMpGT=6oc0r2Qz9PZlt48xqm2bhDA4b3UbV0pd3Ib1oH3KSgDIII++UggUbzEiPaYR2/0Gvp=u7Dr2RKjv9BvGPKdjIxGLnmdi16tzKLt=ZCW1+up8fMDjQIEjlGulWEQGPjFYY3UKEv=6/xcNXBnF5Q2n0nyTdIRP=T=QVitE7a7m6f7G1jRMBHLeK3bEt7MMo34EOADo=cGcDAw3q7bCzuv8RaqB3=agIOZuWiWuBwUk4gKq0CjeUpwC=jIk9i+mGkymB1rdV8Kn/qtLBNpHHGOKNq7hbhxChnmD8hjYP/5DbDChTQemGrlGmi5neSDNBqmTiDetAKteqGq3DD'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # "Referer": 'https://www.cicc.com',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'Host': 'www.cicc.com',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'cookie': cookie,
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows"
}
down_load_path = "E:/PythonCode/futures/"
# page_baseurl = 'https://www.cicc.com/comp/xibDkContent/row?compId=xibDkContent_row-15447668695597004&columnId=833&xibcommonId=833&pageSize=12&currentPage='
page_baseurl = 'https://www.cicc.com/business/list_214_223_'
download_baseurl = 'https://www.cicc.com'


def write_into_file(path, target_content):
    with open(path, 'wb') as write_file:
        write_file.write(target_content)


def get_link_list(url: str) -> list:
    """
    从给定的URL获取链接列表
    
    参数：
    url: str，要获取链接列表的URL
    
    返回值：
    id_title_map: list，包含链接和标题的字典列表
    """
    # 发送GET请求获取网页内容
    r = requests.get(url, headers=headers)

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup)

    # 查找所有class为“item”的div标签
    content = soup.find_all('div', {'class': 'item'})

    # 处理每个content元素，将其转换为字典并存入id_title_map列表中
    id_title_map = list(map(proc_dict, content))

    # 返回id_title_map列表
    return id_title_map


def proc_dict(one: BeautifulSoup):  # 定义一个函数proc_dict，接收一个BeautifulSoup类型的参数one
    item: List[str] = []  # 定义一个空的字符串列表item
    link: str = one.find('a').get('href')  # 获取参数one中标签a的属性href的值，并将其赋给str类型的变量link
    if 'cicc' not in link:  # 如果变量link中不包含字符串'cicc'
        link = download_baseurl + link  # 将变量link赋值为变量download_baseurl与link的拼接字符串
    title: str = one.find('a').get_text() + '-' + one.find(
        'p').get_text() + '.pdf'  # 获取参数one中标签a和标签p的文本内容，分别拼接字符串 '-'，然后将结果赋给str类型的变量title
    item.append(link)  # 将变量link添加到列表item中
    item.append(title)  # 将变量title添加到列表item中
    return item  # 返回列表item作为函数的输出结果


# 注：这里假设导入了，并且`download_baseurl`是一个已定义好的全局字符串变量


def get_pdf(url, title):
    """
    从给定的URL下载PDF文件，并将其写入给定的文件路径

    参数：
        url (str): 下载PDF文件的URL
        title (str): 文件的标题，将用于文件路径的生成

    返回：
        无
    """
    PDF = requests.get(url=url, headers=headers).content
    write_into_file(down_load_path + title, PDF)


def check_uniq(name, name_list):
    if name not in name_list:
        return True


def main():
    # 获取下载路径下的所有文件名 (类型：list[str])
    name_list = os.listdir(down_load_path)
    # 循环遍历指定页面的链接 (范围：1到2)
    for i in range(1, 2):
        # 构建页面链接 (类型：str)
        page_link = page_baseurl + str(i) + '.html'
        print(page_link)
        # 获取页面中的链接列表 (类型：list[tuple])
        link_list = get_link_list(page_link)
        print(link_list)
        # 遍历链接列表中的元组
        for link in link_list:
            # 构建下载链接 (类型：str)
            url, title = link
            # str(link[0])
            # 构建文件名 (类型：str)
            # title = link[1] + '.pdf'
            # 检查文件名是否唯一 (返回类型：bool)
            if check_uniq(title, name_list):
                print(url)
                # 下载文件 (参数类型：str, str)
                get_pdf(url, title)


if __name__ == '__main__':
    main()
