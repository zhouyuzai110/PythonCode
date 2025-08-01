import os
from typing import List
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests

down_load_path = "E:/PythonCode/futures/"
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
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 创建WebDriver实例
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        '''
    })
    
    try:
        # 访问页面
        print(f"正在访问页面: {url}")
        driver.get(url)
        
        # 等待页面加载
        time.sleep(random.uniform(5, 10))
        
        # 获取页面源码
        page_source = driver.page_source
        
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(page_source, "html.parser")
        print(f"页面标题: {soup.title.string if soup.title else '无标题'}")

        # 查找所有class为"item"的div标签
        content = soup.find_all('div', {'class': 'item'})

        # 处理每个content元素，将其转换为字典并存入id_title_map列表中
        id_title_map = list(map(proc_dict, content))

        # 返回id_title_map列表
        return id_title_map
    except Exception as e:
        print(f"请求异常: {e}")
        return []
    finally:
        driver.quit()


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
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    
    # 创建WebDriver实例
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # 添加随机延迟避免请求过于频繁
        time.sleep(random.uniform(2, 5))
        
        print(f"正在下载: {title}")
        print(f"URL: {url}")
        driver.get(url)
        
        # 等待文件下载或重定向
        time.sleep(5)
        
        # 获取页面内容
        pdf_content = driver.page_source.encode('utf-8')
        write_into_file(down_load_path + title, pdf_content)
    except Exception as e:
        print(f"下载文件失败 {title}: {e}")
    finally:
        driver.quit()


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
        print(f"正在访问页面: {page_link}")
        # 获取页面中的链接列表 (类型：list[tuple])
        link_list = get_link_list(page_link)
        print(f"找到 {len(link_list)} 个链接")
        # 遍历链接列表中的元组
        for link in link_list:
            # 构建下载链接 (类型：str)
            url, title = link
            # 检查文件名是否唯一 (返回类型：bool)
            if check_uniq(title, name_list):
                print(f"正在下载: {title}")
                print(f"URL: {url}")
                # 下载文件 (参数类型：str, str)
                get_pdf(url, title)
            else:
                print(f"文件已存在，跳过: {title}")


if __name__ == '__main__':
    main()