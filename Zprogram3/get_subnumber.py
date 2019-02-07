#输入一个数，取出这个数每一位的数
print("请输入一个数：")
n = int(input())
while(n > 0):
    #取余10
    a = n % 10
    print(a,"")
    n = n // 10
