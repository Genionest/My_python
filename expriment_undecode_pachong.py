from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.baidu.com/')

soup = BeautifulSoup(html,features = 'lxml')

href = soup.find('a')
print(href)
