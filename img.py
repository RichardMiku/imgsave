import os
from datetime import datetime

img_insert = """
---
title: {}
date: {}
tags:
---
<!--more-->
<img src='source/images/{}' alt='{}' width=75% height=75%>"""

img_str_list = []
img_list = []

def list_files_in_directory(directory):
    global img_insert
    global img_str_list
    try:
        files = os.listdir(directory)
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for file in files:
            print(img_insert.format(file, current_date, file, file))
            img_str_list.append(file)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist")

# Specify the directory
post_dir = 'source/_posts'
directory_path = 'source/images'

list_files_in_directory(directory_path)

# Write the list of images to a file
for img_name in img_str_list:
    with open(f'{post_dir}/{img_name}.md', 'w') as f:
        f.write(img_insert.format(img_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), img_name, img_name))