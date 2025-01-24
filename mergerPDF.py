import os
import re
from PyPDF2 import PdfMerger

target_path = 'C:/Users/saber/Desktop/pythonscript/futures/'  ## pdf目录文件
pattern = r'第\d+期'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
# pdf_lst.sort(key=lambda x: int(x.split('）')[0].replace('每周研报精选（第', '').replace('期', '')))
pdf_lst.sort(key=lambda x: int(re.findall(pattern, x)[0].replace('第', '').replace('期', '')))
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfMerger(strict=False)
for pdf in pdf_lst:
    print(pdf)
    with open(pdf, 'rb') as input:
        # file_merger.append(input, import_bookmarks=False)  # 合并pdf文件
        file_merger.append(input)

with open('中金公司每周研报精选合集.pdf', 'wb+') as output:
    file_merger.write(output)
