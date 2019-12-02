import os

path = "html/111"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件名称
os.chdir(path)
for file in files:  # 遍历文件夹
    new_file_name = file.replace(" Presidential Race - 2012 ElectionCenter - Elections & Politics from CNN.com", "")
    os.rename(file, new_file_name)

