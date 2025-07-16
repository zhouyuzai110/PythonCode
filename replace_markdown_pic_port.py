import argparse
import os
import re


def replace_in_markdown_files(root_dir):
    """
    遍历目录及子目录中的所有Markdown文件，替换指定内容
    :param root_dir: 要遍历的根目录
    """
    # 编译正则表达式，提高匹配效率
    pattern = re.compile(r'lskypro\.ttnas\.site:88')

    # 计数器
    files_processed = 0
    replacements_made = 0

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            # 检查是否为Markdown文件
            if filename.lower().endswith(('.md', '.markdown')):
                filepath = os.path.join(foldername, filename)
                files_processed += 1

                try:
                    # 读取文件内容
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()

                    # 执行替换
                    new_content, num_replacements = pattern.subn('lskypro.ttnas.site:8443', content)

                    if num_replacements > 0:
                        # 如果有替换发生，写回文件
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        replacements_made += num_replacements
                        print(f"✓ 已更新: {filepath} ({num_replacements}处替换)")
                    else:
                        print(f"○ 无更改: {filepath}")

                except Exception as e:
                    print(f"✗ 错误处理文件 {filepath}: {str(e)}")

    print(f"\n处理完成！共扫描 {files_processed} 个Markdown文件，完成 {replacements_made} 处替换。")


if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='批量替换Markdown文件中的特定字符串')
    parser.add_argument('directory', nargs='?', default='.', help='要处理的目录 (默认为当前目录)')
    args = parser.parse_args()

    # 检查目录是否存在
    if not os.path.isdir(args.directory):
        print(f"错误: 目录 '{args.directory}' 不存在!")
        exit(1)

    print(f"开始处理目录: {os.path.abspath(args.directory)}")
    replace_in_markdown_files(args.directory)
