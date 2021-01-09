
import shutil
import os
import re

def one_line(src, dst, is_test=False):
    f = open(src, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    f = open(dst, "w+", encoding="utf-8")
    for line in lines:
        # 去除整行的注释
        if re.match("\s*--", line):
            # print(re.match("\s*--", line).span())
            pass
        else:
            # 去除写在后面的注释，截取前面部分，自然就舍弃了最后的换行符
            ret0 = re.search("\s*--", line)
            ret = re.search("\n$", line)
            if ret0:
                result = re.split("\s*--", line)
                if len(result)>0:
                    # 加上空格
                    txt = result[0]+" "
                    f.writelines(txt)
                    if is_test:
                        print(txt)
            # 去掉最后的换行符
            elif ret:
                # print(type(line), type(ret.span()))
                txt = line[:ret.span()[0]]
                if txt:
                    ret_2 = re.match("\s*", txt)
                    if ret_2:
                        txt2 = txt[ret_2.span()[1]:]
                        if txt2:
                            # 加上空格
                            txt2 += " "
                            f.writelines(txt2)
                            if is_test:
                                print(txt2)
                    else:
                        # 加上空格
                        txt += " "
                        f.writelines(txt)
                        if is_test:
                            print(txt)
            # 没有注释，也没有换行符
            else:
                f.writelines(line)
                if is_test:
                    print(line)
    f.close()

def publish(src, dst):
    file_list = os.listdir(src)
    for ff in file_list:
        ret = os.path.splitext(ff)
        f_name = ret[0]
        f_type = ret[1]
        if f_type == ".lua":
            print(src+"/"+ff)
            one_line(src+"/"+ff, dst+"/"+ff)
        else:
            publish(src+"/"+ff, dst+"/"+ff)


def publish_tech_prince():
    src = "D://steam/steamapps/common/dont_starve/mods/tech_prince_publish/"
    dst = "D://steam/steamapps/common/dont_starve/mods/tech_prince_publish/"
    files = ["main", "modimport", "scripts"]
    lua_files = ["modmain", "modworldgenmain"]
    for f in files:
        publish(src+f, dst+f)
    for f in lua_files:
        print(src+f+".lua")
        one_line(src+f+".lua", dst+f+".lua")

def lock(src, dst):
    file_list = os.listdir(src)
    for ff in file_list:
        ret = os.path.splitext(ff)
        f_name = ret[0]
        f_type = ret[1]
        if f_type == ".lua":
            print(src+"/"+ff)
            os.system("luac -o "+src+"/"+ff+" "+dst+"/"+ff)
        else:
            lock(src+"/"+ff, dst+"/"+ff)

def lock_tech_prince():
    src = "D://steam/steamapps/common/dont_starve/mods/tech_prince_publish/"
    dst = "D://steam/steamapps/common/dont_starve/mods/tech_prince_publish/"
    files = ["main", "modimport", "scripts"]
    lua_files = ["modmain", "modworldgenmain"]
    for f in files:
        lock(src+f, dst+f)
    for f in lua_files:
        print(src+f+".lua")
        os.system("luac -o "+src+f+".lua"+" "+dst+f+".lua")

# 复制文件夹下的所有文件
def move_folder_file(src, dst, include_folder=False):
    file_list = os.listdir(src)

    if not os.path.exists(dst):
        os.mkdir(dst)

    for file in file_list:
        ret = os.path.splitext(file)
        file_name = ret[0]
        file_type = ret[1]
        if file_type != "":
            src_path = os.path.join(src, file)
            dst_path = os.path.join(dst, file)
            shutil.copy(src_path, dst_path)
        elif include_folder:
            move_folder_file(src+"/"+file, dst+"/"+file)

def replace_word(src, old, new):
    f = open(src, "r")
    lines = f.readlines()
    f.close()
    f = open(src, "w+")
    for line in lines:
        new_line = re.sub(old, new, line)
        f.writelines(new_line)
    f.close()

def step(form, name, style):
    path = "D://jhkf//ModPictures/tech_prince/"+form+"/"
    src = path+style
    dst = path+name
    move_folder_file(src, dst)
    # 重命名要在inven的图片
    img_src = dst+"/"+style+".png"
    dst_src = dst+"/"+name+".png"
    os.rename(img_src, dst_src)

#从ModPictures/spears下copy出一个folder1
def spear_step(name, style):
    step("spears", name, style)

def hat_step(name, style):
    step("hats", name, style)

def potion_step(name, style):
    step("potions", name, style)

def step2(form, name, style):
    path = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/"+form+"/"
    src = path+style
    dst = path+name
    move_folder_file(src, dst, True)
    # 重命名scml文件
    os.rename(dst+"/"+style+".scml", dst+"/"+name+".scml")
    # 修改scml文件
    replace_word(dst+"/"+name+".scml", style, name)

#从zitem/spears下copy出一个folder2（记得修改scml文件）
def spear_step2(name, style):
    step2("spears", name, style)

def hat_step2(name, style):
    step2("hats", name, style)

def potion_step2(name, style):
    step2("potions", name, style)

#将folder1的文件copy到folder2/inven的对应位置
def spear_step3(name, style=None):
    path1 = "D://jhkf//ModPictures/tech_prince/spears/"
    path2 = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/spears/"
    src = path1+name+"/"
    dst = path2+name+"/"
    s = [
        src+"item-0.png",
        src+"item_water-0.png",
        src+"swap_object-0.png",
        src+name+".png",
    ]
    d = [
        dst+"item/item-0.png",
        dst+"item_water/item_water-0.png",
        dst+"swap_object/swap_object-0.png",
        path1+"inven/"+name+".png",
    ]
    for i in range(len(s)):
        shutil.copy(s[i], d[i])

def hat_step3(name, style=None):
    path1 = "D://jhkf//ModPictures/tech_prince/hats/"
    path2 = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/hats/"
    src = path1+name+"/"
    dst = path2+name+"/"
    s = src+"swap_hat"
    s2 = src+"swap_hat_water-0.png"
    s3 = src+name+".png"
    d =  dst+"swap_hat/swap_hat"
    d2 = dst+"swap_hat_water/swap_hat_water-0.png"
    d3 = path1+"inven/"+name+".png"
    for i in range(4):
        shutil.copy(s+"-"+str(i)+".png", d+"-"+str(i)+".png")
    shutil.copy(s2, d2)
    shutil.copy(s3, d3)

def potion_step3(name, style):
    path1 = "D://jhkf//ModPictures/tech_prince/potions/"
    path2 = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/potions/"
    src = path1+name+"/"
    dst = path2+name+"/"
    s = src+"potion.png"
    s2 = src+name+".png"
    d = dst+"potion.png"
    d2 = path1+"inven/"+name+".png"
    shutil.copy(s, d)
    shutil.copy(s2, d2)    

def step4(form, name, style=None):
    path1 = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/"+form+"/"
    path2 = "D://steam/steamapps/common/dont_starve/mods/tech_prince/exported/"
    path3 = "D://jhkf//ModPictures/tech_prince/"+form+"/inven/"
    path4 = "D://steam/steamapps/common/dont_starve/mods/tech_prince/images/inventoryimages/"
    src = path1+name
    dst = path2+name
    img_src = path3+name+".png"
    img_dst = path4+name+".png"
    shutil.copy(img_src, img_dst)
    move_folder_file(src, dst, True)

#从完成的folder2和inven里的文件复制到mod里
def spear_step4(name, style=None):
    step4("spears", name, style)

def hat_step4(name, style=None):
    step4("hats", name, style)

def potion_step4(name, style=None):
    step4("potions", name, style)

# 清除exported下所有文件
def step5(name=None, style=None):
    path = "D://steam/steamapps/common/dont_starve/mods/tech_prince/exported"
    file_list = os.listdir(path)
    for file in file_list:
        ret = os.path.splitext(file)
        file_name = ret[0]
        file_type = ret[1]
        print(file)
        shutil.rmtree(path+"/"+file, True)

# 清楚inventoryimages下所有png文件
def step6(name=None, style=None):
    path = "D://steam/steamapps/common/dont_starve/mods/tech_prince/images/inventoryimages"
    file_list = os.listdir(path)

    for file in file_list:
        ret = os.path.splitext(file)
        file_name = ret[0]
        file_type = ret[1]
        if file_type == ".png":
            print(file)
            os.remove(path+"/"+file)

if __name__ == "__main__":
    #从ModPictures/spears下copy出一个folder1
    #从zitem/spears下copy出一个folder2（记得修改scml文件）
    #PS好图片
    #将folder1的文件移动到folder2和inven的对应位置
    #从完成的folder2和inven里的文件复制到mod里
    # 清除exported下所有文件
    # 清楚inventoryimages下所有png文件

    # publish_tech_prince()