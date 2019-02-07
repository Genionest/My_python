def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        for i in range(len(L)):
            L[i] = L[i-1] + L[i]

if __name__ == '__main__':
    n = 0
    for t in triangles():
        print(t)
        n = n+1
        if n==10:
            break
