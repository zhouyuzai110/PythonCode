# from dataclasses import replace
import os
from PyPDF2 import PdfMerger

target_path = 'C:/Users/saber/Desktop/pythonscript/futures2/'  ## pdf目录文件
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfMerger(strict=False)
for pdf in pdf_lst:
    print(pdf)
    with open(pdf, 'rb') as input:
        # file_merger.append(input, import_bookmarks=False)  # 合并pdf文件
        file_merger.append(input)

with open('中信期货研报.pdf', 'wb+') as output:
    file_merger.write(output)
