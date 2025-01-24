import os

win_path = "\\ttnas\电子书\复兴之路\国民党研究"
path = "//ttnas/电子书" + win_path.replace('\\ttnas\电子书', '').replace('\\', '/')
print(path)
files = os.listdir(path)

os.chdir(path)
for item in files:
    if os.path.isfile(item):
        if '《' in item or '》' in item:
            new_file_name = item.replace('《', '').replace('》', '')
            if new_file_name in files:
                continue
            os.rename(item, new_file_name)
            print(item, new_file_name)
