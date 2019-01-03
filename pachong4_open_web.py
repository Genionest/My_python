#打开网页，get和post方法的不同，session亮相
import requests
import webbrowser

param = {"wd":"莫凡Python"} #搜索信息
r = requests.get('http://www.baidu.com/s',params = param)
#print(r.url)
webbrowser.open(r.url) #打开这个网页

data= {'firstname':'Morvan','lastname':'Zhou'}
r = requests.post('http://pythonscraping.com/files/processing.php',data= data)
#print(r.text)
#webbrowser.open(r.url)

file= {'urloadFile':open('./image.png','rb')}
r  = requests.post('http://pythonscraping.com/files/processing2.php',files=file)
#print(r.text)

payload= {'username':'Morvan','password':'password'}


r  = requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
#print(r.text)
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
print(r.cookies.get_dict())
#webbrowser.open(r.url)

session = requests.Session()
payload = {'username':'Morvan','password':'password'}
r  = session.post('http://pythonscraping.com/pages/cookies/welcome.php',data = payload)
print(r.cookies.get_dict())

r = session.get('http://pythonscraping.com/pages/cookies/profile.php')
#print(r.text)
