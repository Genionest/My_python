import requests
import webbrowser

#param = {"wd":"莫凡Python"} #搜索信息
r = requests.get('http://www.kali.org.cn/')
r = requests.get('')
#print(r.url)
webbrowser.open(r.url) #打开这个网页
