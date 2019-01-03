import shutil,os
#
name_list = ["WangYang","ChengShuling","Shiren","Malzahar","Renekton","Maokai","Kassadin","Sion","Azir","Draven","Jax","Kaisa","Lux","Nasus","newGaren","newJarvanIV","newTryndamere","newYi","Ornn","Sejuani","Skarner","Soroka","Twisted","Udyr","Vladimir","Wukong","Yasuo"]

path = "H:\\QSanguosha-v2-20150926\\image\\generals\\card\\"

path2 = "C:\\Users\\wargon\\Desktop\\lol"

isExists = os.path.exists(path2)
    #os.mkdir(path2)
print(isExists)

count = 0

for i in name_list:
    shutil.copy(path+i+".jpg",path2)
    print(count+1)
    print(i)
