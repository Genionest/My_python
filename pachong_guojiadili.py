from bs4 import BeautifulSoup
import requests
import os
os.makedirs('./img/',exist_ok=True) #创建文件夹

URL  = "http://www.nationalgeographic.com.cn/animals/" #url地址

html = requests.get(URL).text
soup = BeautifulSoup(html,'lxml')
img_ul = soup.find_all('ul',{'class':'img_list'})

for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url,stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' %image_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Save %s' %image_name)
