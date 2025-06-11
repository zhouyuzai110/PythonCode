import os
import re
from urllib.parse import urlparse

import requests

# 读取本地HTML文件
with open('cicc.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 定义正则表达式模式
pattern = re.compile(
    r'<div class="item">.*?<a.*?href="(https://www\.cicc\.com/upload/file/.*?\.pdf)".*?>(.*?)</a>.*?<p class="time">(.*?)</p>',
    re.DOTALL)

# 查找所有匹配项
matches = pattern.findall(html_content)

# 创建保存PDF文件的目录（如果不存在）
os.makedirs('pdfs', exist_ok=True)

# 遍历匹配项并下载PDF文件
for match in matches:
    pdf_url, title, date = match
    new_filename = f"{title}-{date}.pdf"
    save_path = os.path.join('pdfs', new_filename)

    response = requests.get(pdf_url)
    response.raise_for_status()  # 检查请求是否成功

    with open(save_path, 'wb') as file:
        file.write(response.content)

    print(f"Downloaded and saved: {save_path}")
