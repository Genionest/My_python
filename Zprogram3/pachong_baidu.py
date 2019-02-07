from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"
his = ["/item/%E8%9C%98%E8%9B%9B/8135707"]




for i in range(20):
    url = base_url+ his[-1]

    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html,features = 'lxml')

    print(i,soup.find('h1').get_text(),'  url:',his[-1])

    #find valid urls
    sub_urls = soup.find_all('a',{'target':'_blank',"href":re.compile("/item/(%.{2})+$")})
    #这里(%.{2})+$是为了匹配很多个%E3这样的数据，故将其括号在一起
    
    if len(sub_urls)>0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        #no valid sub link found
        his.pop()
#    print(his)
