import os
from datetime import datetime

# 定义图片插入模板
img_insert = """
---
title: {}
date: {}
tags:
---
imgname: {}
<!--more-->
<img src='/images/{}' alt='{}' width=75% height=75%>"""

img_str_list = []  # 存储图片文件名的列表
img_list = []  # 备用的图片列表

def list_files_in_directory(directory):
    global img_insert
    global img_str_list
    try:
        # 列出目录中的所有文件
        files = os.listdir(directory)
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for file in files:
            # print(f"Processing file {file}")  # 打印正在处理的文件名
            img_str_list.append(file)  # 将文件名添加到列表中
    except FileNotFoundError:
        print(f"The directory {directory} does not exist")  # 目录不存在时打印错误信息

# 指定目录
post_dir = 'source/_posts'
directory_path = 'source/images'

# 列出指定目录中的文件
list_files_in_directory(directory_path)

# 将图片列表写入文件
for img_name in img_str_list:
    file_path = f'{post_dir}/{img_name}.md'
    print(f"Processing file {img_name}")
    if not os.path.exists(file_path):  # 判断文件是否已存在
        with open(file_path, 'w') as f:
            f.write(img_insert.format(img_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), img_name, img_name, img_name))  # 写入模板内容
    else:
        print(f"File {img_name} already exists. Skipping...")  # 文件已存在则跳过