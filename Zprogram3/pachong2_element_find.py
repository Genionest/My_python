#爬取网页元素的属性查找（通过字典）
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')

soup = BeautifulSoup(html,features='lxml')

month = soup.find_all('li',{'class':'month'})
for m in month:
    print(m.get_text())
    
jan = soup.find('ul',{'class':'jan'})
d_jan = jan.find_all('li')
for j in d_jan:
    print(j.get_text())
