import os

def file_name(file_dirs):
    for root,dirs,files in os.walk(file_dirs):
        print(root)
        print(dirs)
        print(files)
        break
    
