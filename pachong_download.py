import os
from urllib.request import urlretrieve

os.makedirs('./img/',exist_ok=True)#建立一个文件夹

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

#使用urlretrieve方法下载
#urlretrieve(IMAGE_URL,'./img/image1.png')

import requests
#使用requests下载，原理为将源文件的内容全部读取然后写入，所有文件本身只是字符
#r = requests.get(IMAGE_URL)
#with open('./img/image2.png','wb') as f:
#    f.write(r.content)

#写入较大文件时，边下载，边写入
r = requests.get(IMAGE_URL,stream=True)

with open('./img/image3.png','wb') as f:
    for chunk in r.iter_content(chunk_size=32):#32个字节为一个单位，边下边写
        f.write(chunk)
