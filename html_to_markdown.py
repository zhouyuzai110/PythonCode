from bs4 import BeautifulSoup
import html

def html_to_markdown(html_content):
    """
    将包含知乎文章内容的HTML文件转换为Markdown格式。
    
    参数:
        html_content (str): HTML 文件的内容。
    
    返回:
        str: 转换后的 Markdown 内容。
    """
    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 尝试多种方式定位文章主体内容
    article_body = (
        soup.find('div', class_='RichText ztext Post-RichText css-1yl6ec1') or
        soup.find('span', class_='RichText ztext CopyrightRichText-richText css-1yl6ec1') or
        soup.find('div', {'itemprop': 'articleBody'})
    )

    if not article_body:
        return "未能找到文章主体内容"

    # 初始化 Markdown 内容
    markdown_content = ""

    # 遍历 article_body 下的所有后代元素并转换为 Markdown（支持嵌套结构）
    for element in article_body.descendants:
        if element.name == 'p':
            # 处理段落
            text = html.unescape(element.get_text()).strip()
            if text:
                markdown_content += f"{text}\n\n"
        elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            # 处理标题
            level = int(element.name[1])
            text = html.unescape(element.get_text()).strip()
            if text:
                markdown_content += f"{'#' * level} {text}\n\n"
        elif element.name == 'ul':
            # 处理无序列表
            for li in element.find_all('li', recursive=False):
                text = html.unescape(li.get_text()).strip()
                if text:
                    markdown_content += f"- {text}\n"
            markdown_content += "\n"
        elif element.name == 'ol':
            # 处理有序列表
            for idx, li in enumerate(element.find_all('li', recursive=False)):
                text = html.unescape(li.get_text()).strip()
                if text:
                    markdown_content += f"{idx + 1}. {text}\n"
            markdown_content += "\n"
        elif element.name == 'blockquote':
            # 处理引用块
            text = html.unescape(element.get_text()).strip()
            if text:
                markdown_content += f"> {text}\n\n"
        elif element.name == 'b' or (element.name == 'strong'):
            # 处理加粗文本
            text = html.unescape(element.get_text()).strip()
            if text:
                markdown_content += f"**{text}**\n\n"
        elif element.name == 'img':
            # 处理图片，增强采集能力
            # 优先使用 src 属性
            image_url = element.get('src') or element.get('data-src') or element.get('data-original') or element.get('data-lazy')

            # 如果成功提取到图片 URL，添加到 Markdown 内容
            if image_url:
                markdown_content += f"![]({image_url})\n\n"
            else:
                # 可选：记录未找到图片 URL 的情况
                print("警告：发现 <img> 标签，但未能找到有效的图片链接。")
        else:
            # 其他未处理的标签跳过
            continue

    return markdown_content

if __name__ == "__main__":
    # 读取 HTML 文件内容
    with open('zhihu1.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 调用函数将 HTML 内容转换为 Markdown 格式
    markdown_content = html_to_markdown(html_content)

    # 输出转换后的 Markdown 内容
    print(markdown_content)