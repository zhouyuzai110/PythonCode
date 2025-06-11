import os

local_path = 'E:/PythonCode/formatmd'
for root, dirs, files in os.walk(local_path):
    for file_name in files:
        print(root, dirs, file_name)
        # print(os.path.join(root, file_name).replace('\\', '/'))
        print(os.path.relpath(os.path.join(root, file_name), start=local_path))
