with open('C:\\Users\Wargon\Desktop\kuaiji.txt','r') as f:
    i = 0
    lst = []
    while(i!=''):
        i = f.readline().strip()
        lst.append(i)
    lst.pop()
    print(lst)
