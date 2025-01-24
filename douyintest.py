# 读取文本文件 把每一行的代码后面的注释对齐，注释以#开头
def read_file():
    with open('douyintest.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                line = line.replace('#', '')
                line = line.replace(' ', '')
                line = line.replace('\n', '')
                print(line)
