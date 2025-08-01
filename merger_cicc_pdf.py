import os
import re

from PyPDF2 import PdfMerger, PdfReader, PdfWriter


def merge_pdfs(target_path='E:/PythonCode/futures/', output_filename='中金公司每周研报精选合集.pdf') -> str:
    """
    合并指定目录下的所有PDF文件
    
    参数:
        target_path: PDF文件所在目录
        output_filename: 合并后输出的文件名
    
    返回:
        输出文件的路径
    """
    pattern = r'第\d+期'
    pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
    
    if not pdf_lst:
        print("未找到任何PDF文件")
        return ""
    
    # 按期数排序
    pdf_lst.sort(key=lambda x: int(re.findall(pattern, x)[0].replace('第', '').replace('期', '')))
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    file_merger = PdfMerger(strict=False)
    for pdf in pdf_lst:
        print(f"正在合并: {pdf}")
        with open(pdf, 'rb') as input:
            file_merger.append(input)

    output_path = output_filename
    with open(output_path, 'wb+') as output:
        file_merger.write(output)
    
    print(f"PDF合并完成，已保存到: {output_path}")
    return output_path


def delete_legal_page(input_path, output_path, keyword="法律声明"):
    """
    删除PDF文件中包含特定关键词的页面
    
    参数:
        input_path: 输入PDF文件路径
        output_path: 输出PDF文件路径
        keyword: 要检测的关键词
    """
    if not os.path.exists(input_path):
        print(f"输入文件不存在: {input_path}")
        return False

    with open(input_path, 'rb') as input_file:
        reader = PdfReader(input_file)
        writer = PdfWriter()
        
        deleted_pages = 0
        for page_num in range(len(reader.pages)):
            print(f"处理第 {page_num + 1} 页")
            page = reader.pages[page_num]
            text = page.extract_text()

            # 检查是否包含关键词
            if keyword not in text:
                writer.add_page(page)
            else:
                deleted_pages += 1
                print(f"删除包含'{keyword}'关键词的第 {page_num + 1} 页")

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print(f"处理完成，共删除 {deleted_pages} 页，已保存到 {output_path}")
        return True


def main():
    """
    主函数：一键合并PDF文件并删除包含法律声明的页面
    """
    # 第一步：合并所有PDF文件
    print("开始合并PDF文件...")
    merged_file = merge_pdfs()
    
    if not merged_file:
        print("合并失败，程序退出")
        return
    
    # 第二步：删除包含法律声明的页面
    print("\n开始删除包含法律声明的页面...")
    output_file = "中金公司每周研报精选合集_无法律声明版.pdf"
    success = delete_legal_page(merged_file, output_file, "法律声明")
    
    if success:
        print(f"\n所有操作已完成！")
        print(f"合并后的文件: {merged_file}")
        print(f"删除法律声明页后的文件: {output_file}")
    else:
        print("处理过程中出现错误")


if __name__ == '__main__':
    main()
