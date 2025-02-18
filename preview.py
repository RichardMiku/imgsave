import os
from datetime import datetime

# 定义图片插入模板
img_insert = """---
title: preview wall
date: {}
tags:
---

# imgList
{}
"""

pre_insert = """
## imgname: {}
<img src='/images/{}' alt='{}' width=30% height=30%>"""

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
previewmd_dir = 'source/preview/index.md'
directory_path = 'source/images'

# 列出指定目录中的文件
list_files_in_directory(directory_path)

# 生成图片预览内容
img_previews = "\n".join([pre_insert.format(img_name, img_name, img_name) for img_name in img_str_list])

# 将图片预览内容写入文件
with open(previewmd_dir, 'w') as f:
    f.write(img_insert.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), img_previews))