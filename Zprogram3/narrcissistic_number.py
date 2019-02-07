#输入一个数，这个数将视为位数，返回这个位数的水仙花数
print("请输入一个数:")
n = int(input())
for i in range(10**(n-1), 10**n):
    #取出i的各个位数，然后n次幂加总
    s = 0
    # while( i > 0 ): #进入条件
    #    t = i // 10
    #    s += t**n
    #    i /= 10
    #    print(t)
    p = i
    while(p>0):
        t = p % 10
        s += t ** n
        p = p // 10
        #6print("t = %d,s = %d,i = %d" % (t,s,i))
    #判断结果
    if(s == i):
        print(i, "是水仙花数")
#特例
if n == 1:
    print(1)

print("计算完毕")
