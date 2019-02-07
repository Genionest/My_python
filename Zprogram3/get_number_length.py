#输入一个数，输出这个数的位数
#0和1都的结果都是1
print("请输入一个数：")
n = int(input())

t = 1
p = n // 10
while(p>0):
    t += 1
    p = p // 10

print(n,"的位数是",t)
