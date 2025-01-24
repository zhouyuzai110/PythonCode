from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}

BASEURL = 'http://www.scio.gov.cn/ztk/dtzt/47678/48355/index.htm'
ORIGIN_URL = 'http://www.scio.gov.cn/xwfbh/xwbfbh/wqfbh'
pattern_one = re.compile('/\d{5}/\d{5}/index\.htm')
pattern_two = re.compile('/\d{5}/\d{5}/Document/\d{7}/\d{7}\.htm')


def fetch_complete_links(target_url: str) -> list:
    """
    获取指定URL中的完整链接列表

    参数:
    target_url (str): 目标URL地址

    返回:
    list: 完整链接列表
    """
    response = requests.get(target_url, headers=headers)  # 发送GET请求获取页面内容（假设headers为字典类型）
    parsed_html = BeautifulSoup(response.content, "html.parser")  # 使用BeautifulSoup解析页面内容
    relevant_links = parsed_html.find('div', {'class': 'scroll-box'}).find_all('a')  # 查找div标签中class为'scroll-box'的所有a标签
    complete_link_list = [BASEURL.replace('index.htm', '') + link.get('href')
                          for link in relevant_links]  # 遍历a标签，将链接拼接成完整链接，并存储到列表中
    reversed_link_list = list(reversed(complete_link_list))  # 将完整链接列表进行反转
    return reversed_link_list  # 返回反转后的完整链接列表


# 定义一个函数，用于获取文章的真实URL
def get_article_true_url(url: str) -> str:
    # 打印原始URL
    response = requests.get(url, headers=headers)
    parsed_html = BeautifulSoup(response.content, "html.parser")

    # 如果在解析后的HTML中找到pattern_one的匹配项，则提取并构造真实URL，然后返回
    if len(pattern_one.findall(str(parsed_html))) > 0:
        true_url = ORIGIN_URL + pattern_one.findall(str(parsed_html))[0]
        return true_url

    # 如果未找到pattern_one的匹配项，则通过拼接'http://www.scio.gov.cn'和pattern_two在HTML中的匹配项，
    # 并递归调用该函数以继续查找真实URL
    recursion_url = 'http://www.scio.gov.cn' + pattern_two.findall(str(parsed_html))[0]
    return get_article_true_url(recursion_url)


def get_article_content(url: str) -> None:
    # 初始化存储文章内容的列表
    content_list: list[str] = []
    # 发送GET请求获取网页内容，headers参数根据实际情况填充
    response: requests.Response = requests.get(url, headers=headers)
    # 使用BeautifulSoup解析HTML内容
    soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
    # 获取网页标题
    title_element: BeautifulSoup.Tag = soup.find('title')
    # 将标题转换为字符串并添加换行符后存入内容列表
    content_list.append(str(title_element) + '\n\n')
    # 获取摘要内容
    summary_text: str = soup.find('div', {'class': 'box'}).get_text()
    # 将摘要内容加入到内容列表中
    content_list.append(summary_text)
    # 获取正文段落元素
    paragraph_elements: list[BeautifulSoup.Tag] = soup.find('div', {'class': 'textlive'}).find_all('p')
    # 将所有段落文本提取出来并存入内容列表
    content_list.extend([paragraph.get_text() for paragraph in paragraph_elements])
    # 清洗并处理内容列表
    cleaned_content: list[str] = clean_list(content_list)
    # 打开文件'zgzsn.txt'，以追加模式写入清洗后的内容
    with open('zgzsn.txt', 'a', encoding='utf-8', errors='ignore') as file:
        # 将清洗后的文本内容以换行符分隔后写入文件
        file.write('\n'.join(cleaned_content))
        # 添加三个换行符作为间隔
        file.write('\n\n\n')


def clean_list(list):
    return [
        x.replace('\u3000', '').replace('<br/>', '').replace(' ', '').replace('\n', '').replace('\r', '') for x in list
        if len(x) > 0 and '摄）' not in x
    ]


def main():
    for url in fetch_complete_links(BASEURL):
        true_url = get_article_true_url(url)
        print(true_url)
        get_article_content(true_url)


if __name__ == '__main__':
    main()
