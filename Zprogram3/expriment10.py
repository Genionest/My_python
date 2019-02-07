def caculate(total):
    one = total*0.4-2
    two = 16
    three = (one+two)/3
    can = False
    if total == one + two + three:
        can = True
    if one.is_integer() and three.is_integer() and can:
        return one,two,three,total

for i in range(100):
    n = caculate(i)
    if n != None:
        print(n)
    
