import os
import re


def extract_network_config(input_file):
    output_dir = r'D:\OneDrive\矩阵幽谧\配置文件\quadlet'  # 目标输出目录

    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_title = None
    in_code_block = False
    code_content = []

    for line in lines:
        line = line.rstrip('\n')  # 保留原始行，但去掉换行符

        # 处理三级标题
        if line.startswith('### '):
            title = line[4:].strip()
            # 检查标题是否包含任意一个关键词（network, volume, container）
            keywords = ['network', 'volume', 'container', 'configuration', 'timer']
            if any(keyword in title.lower() for keyword in keywords):
                current_title = title
                # 生成合法的文件名（不加 .txt）
                safe_title = re.sub(r'[^\w\-_\. ]', '', title).strip()
                filename = os.path.join(output_dir, safe_title)  # 添加目录路径
                code_content = []  # 重置代码内容
                in_code_block = False
        # 开始代码块
        elif line == '```ini':
            in_code_block = True
            code_content = []  # 清空之前的代码内容
        # 结束代码块
        elif line == '```':
            if in_code_block and current_title:
                # 写入文件（不加 .txt）
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(code_content))
                print(f"已保存文件：{filename}")
                current_title = None
                in_code_block = False
        # 收集代码内容
        elif in_code_block and current_title:
            code_content.append(line)


# 示例调用
extract_network_config(r'E:\KnowledgeBase\src\KnowledgeBase\操作系统\Linux\服务器及系统管理\FedoraCoreOS安装及配置.md')
