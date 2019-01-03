with open('D:\python3.6.1\Zprogram3\day_done.txt','w') as f:
    f.write('http://www.kali.org.cn/'+'\n'+'https://www.icourse163.org/')
with open('D:\python3.6.1\Zprogram3\day_done.txt','r') as f:
    l = []
    r = f.readline().strip()
    l.append(r)
    r = f.readline().strip()
    l.append(r)
    print(l)
#'\n'要自己把他去掉
