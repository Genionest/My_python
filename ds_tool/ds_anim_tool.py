import shutil
import os

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

name = "tp_spear_hades"
#从Pictures/spears下copy出一个folder1
def step():
    path = "D://jhkf//Pictures/tech_prince/spears/"
    src = path+"tp_spear_valkyrie"
    dst = path+name
    # 创建目标文件夹
    # os.mkdir(dst)
    move_folder_file(src, dst)
    # 重命名要在inven的图片
    img_src = src+"/tp_spear_valkyrie.png"
    dst_src = dst+"/"+name+".png"
    os.rename(img_src, dst_src)

#从zitem/spears下copy出一个folder2（记得修改scml文件）
def step2():
    # name = "tp_spear_hades"
    path = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/spears/"
    src = path+"tp_spear_valkyrie"
    dst = path+name
    # 创建目标文件夹
    # os.mkdir(dst)
    move_folder_file(src, dst, True)
    # 重命名scml文件
    os.rename(dst+"/tp_spear_valkyrie.scml", dst+"/"+name+".scml")
    # folder = [
    #     "/item",
    #     "/item_water",
    #     "/swap_object",
    # ]
    # for i in folder:
    #     # 创建目标文件夹
    #     os.mkdir(dst+i)
    #     move_folder_file(src+i, dst+i)

#将folder1的文件移动到folder2/inven的对应位置
def step3():
    # name = "tp_spear_hades"
    path1 = "D://jhkf//Pictures/tech_prince/spears/"
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
    for i in range(4):
        shutil.copy(s[i], d[i])

#从完成的folder2和inven里的文件复制到mod里
def step4():
    # name = "tp_spear_hades"
    path1 = "D://steam/steamapps/common/Don't Starve Mod Tools/mod_tools/Spriter/zitem/spears/"
    path2 = "D://steam/steamapps/common/dont_starve/mods/tech_prince/exported/"
    path3 = "D://jhkf//Pictures/tech_prince/spears/inven/"
    path4 = "D://steam/steamapps/common/dont_starve/mods/tech_prince/images/inventoryimages/"
    src = path1+name
    dst = path2+name
    img_src = path3+name+".png"
    img_dst = path4+name+".png"
    shutil.copy(img_src, img_dst)
    # 创建目标文件夹
    # os.mkdir(dst)
    move_folder_file(src, dst, True)

# 清除exported下所有文件
def step5():
    path = "D://steam/steamapps/common/dont_starve/mods/tech_prince/exported"
    file_list = os.listdir(path)
    for file in file_list:
        ret = os.path.splitext(file)
        file_name = ret[0]
        file_type = ret[1]
        # print(file)
        shutil.rmtree(path+"/"+file, True)

# 清楚inventoryimages下所有png文件
def step6():
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
    #从Pictures/spears下copy出一个folder1
    #从zitem/spears下copy出一个folder2（记得修改scml文件）
    #将folder1的文件移动到folder2/inven的对应位置
    #从完成的folder2和inven里的文件复制到mod里
    # 清除exported下所有文件
    # 清楚inventoryimages下所有png文件
    step6()
