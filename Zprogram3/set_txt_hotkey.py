#为新建文本文档添加快捷键，请确定你有管理员权限
import win32api
import win32con
# 打开HKEY_CLASSES_ROOT\Local Settings\MuiCache\a7\AAF68885
#                                               a7会重置
def hot_key_set(aa):
    try:
        key_pre = "Local Settings\\MuiCache\\"
        key_back = r"\AAF68885"
        key_path = key_pre + aa + key_back
        print(key_path)
        key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT,
        key_path,0,win32con.KEY_ALL_ACCESS)

        win32api.RegSetValueEx(key,r'@C:\WINDOWS\system32\notepad.exe,-469',
        0,win32con.REG_SZ,'文本文档(&T)')

        value = win32api.RegQueryValueEx(key,r'@C:\WINDOWS\system32\notepad.exe,-469')
        print(value)
        return 0
        
    except Exception as e:
        print(e)


#key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,  
#'SOFTWARE\\Microsoft\\Internet Explorer',0, win32con.KEY_ALL_ACCESS)  
#value = win32api.RegQueryValueEx(key,'Build')   
#print(value)

if __name__ == '__main__':
    for i in range(26):
        for j in range(26):
            aa = chr(i+ord('a')) + chr(j+ord('a'))
            hot_key_set(aa)
