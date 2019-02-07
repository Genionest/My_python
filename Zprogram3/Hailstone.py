#值弹上弹下的函数
def hailstone(n):
    length = 1;
    while 1 < n :
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        length += 1
    return length
