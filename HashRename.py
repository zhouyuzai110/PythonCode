import os
import sys
import hashlib

path = "C:/Users/saber/Desktop/pythonscript/rename/"
files = os.listdir(path)
hash_list = []


def get_file_sha1(file_path):
    with open(file_path, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        file_sha1 = sha1obj.hexdigest()
    return file_sha1


os.chdir(path)
# print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.realpath(__file__))

for item in files:
    hash_code = get_file_sha1(item)
    print(hash_code, item)
    # name_list = item.split('.')
    if hash_code in hash_list or hash_code + '.mp4' in files:
        continue
    elif len(item) > 20:
        continue
    else:
        os.rename(item, hash_code + '.mp4')
        hash_list.append(hash_code)
