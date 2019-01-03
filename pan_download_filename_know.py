#获取当前目录下的所有子目录和文件名
import os

def file_name(file_dirs):
    
    with open('C:\\Users\\wargon\\Desktop\\duqu.txt','w') as f:
        for root,dirs,files in os.walk(file_dirs):
            for d in dirs:
                f.write(d+'\n')
            for file in files:
                f.write(file+'\n')
            break

    
