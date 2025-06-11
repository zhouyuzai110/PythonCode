import os
import re

from PyPDF2 import PdfMerger, PdfReader, PdfWriter


def merge_pdfs() -> None:
    target_path = 'E:/PythonCode/futures/'  ## pdf目录文件
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


def delete_legal_page(input_path, output_path, keyword="法律声明"):

    with open(input_path, 'rb') as input_file:
        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page_num in range(len(reader.pages)):
            print(f"处理第 {page_num + 1} 页")
            page = reader.pages[page_num]
            text = page.extract_text()

            # 检查是否包含关键词
            if keyword not in text:
                writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print(f"处理完成，已保存到 {output_path}")


# 使用示例
input_pdf = "中金公司每周研报精选合集.pdf"
output_pdf = "delete_legal_page.pdf"
delete_legal_page(input_pdf, output_pdf)
