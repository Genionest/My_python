def get_web_list():
    with open('D:\python3.6.1\Zprogram3\day_done.txt','r') as f:
        i=0
        rlist=[]
        while(i!=''):
            i=f.readline().strip()
            rlist.append(i)
        rlist.pop()
    return rlist
def awrite():
    with open('D:\python3.6.1\Zprogram3\day_done.txt','a') as f:
        f.write('http://www.baidu.com/\n')
    return
