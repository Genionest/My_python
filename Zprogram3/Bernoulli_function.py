def b(k,n,p):
    for i in range(k):
        a = n
        b = 1
        a *= n - 1
        b *= b + 1
    c = a / b
    d = pow(p,k)
    e = pow(1-p,n-k)
    return c*d*e
