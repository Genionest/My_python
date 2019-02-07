low = lambda x:10000 if x>10000 else -10000 if x<-10000 else x

def f(x,y):
    a = ((x*0.05)**2 + (y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
    return a

for x in range(-30,30):
    for y in range(-30,30):
        if f(x,y)<=0:
            print(x,y)
