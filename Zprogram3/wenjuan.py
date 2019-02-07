import random

#省区
print('a')
print('a')
#gender
ques3 = random.choice(['man','man','woman'])
print('3.',ques3)
#age
ques4 = random.choice(['<30','31-40','41-50','51-60','>61'])
print('4.',ques4)
#education
ques5 = random.choices(['primary','primary','middle'])
print('5.',ques5)
#area
ques6 = random.choices(['<3','3-10'])
print('6.',ques6)
#income
ques7 = random.randint(1,5)
if ques7 > 1:
    print('7.','<10000$')
else:
    print('7.','10000$-20000$')

#agriculture
print('8.','a,b,d')

#9
print('9.','b')
#11
print('11.','b')
#13
print('12.','b')
#15
print('15.','b')
#17
print('17.','d')
#18
ques18 = random.choices(['c','d'])
print('18.',ques18)
#19
ques19 = random.choices(['b','c','d'])
print('19.',ques19)
#20
ques20 = []
def multiple_choice(ques,num,n):
    for i in range(num):
        b=['yes','no']
        i = random.choices(b)
        ques.append(i)
    print(str(n))
    print(ques)
multiple_choice(ques20,6,20)
#21
ques21 = []
multiple_choice(ques21,7,21)
#22
ques22 = []
multiple_choice(ques22,3,22)
#23
ques23 = []
multiple_choice(ques23,6,23)
#24
ques24 = random.choices(['a','b','c','d'])
print('24.',ques24)
#25
ques25 = random.choices(['b','c'])
print('25.',ques25)
#26
ques26 = random.choices(['a','b','c'])
print('26.',ques26)
#27
ques27 = random.choices(['b','c'])
print('27.',ques27)
#28
ques28 = random.choices(['b','c'])
print('28.',ques28)
#29
ques29 = []
multiple_choice(ques29,7,29)
