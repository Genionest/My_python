import random
a = random.randint(0,256)
ha = hex(a)
ra = str(ha).lstrip('0x') #删除左边的
if len(ra)<2:
    ra = '0'+ra
if a == 0:
    ra = '00'
print(ra)
