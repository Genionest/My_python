#斐波那契数列，非递归正解算法
print("请输入一个数：")
n = int(input())
Fib = []
for i in range(0,n):
    Fib.append(0)
    if i < 2:
        Fib[i] = 1
    else:
        Fib[i] = Fib[i-1] + Fib[i-2]

print(Fib)
