import win32api
import win32con

#不知道为什么前面要+r
proxy_path = r'HARDWARE\DESCRIPTION\System\CentralProcessor\0'
value = 'Intel(R) Core(TM) i7-7700M CPU @ 3.50GHz'
value_name = 'ProcessorNameString'
#必须要以管理员身份运行python才有权限打开
key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,proxy_path,0,
                          win32con.KEY_ALL_ACCESS)

win32api.RegSetValueEx(key,value_name,0,win32con.REG_SZ,value)
win32api.RegCloseKey(key) #打开的文件记得关闭才能完全修改


#import winreg
#root = winreg.HKEY_LOCAL_MACHINE
#proxy_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
#hkey = winreg.OpenKey(root,proxy_path)
#winreg.setValue(hkey,"ProcessorNameString",0,winreg.REG_SZ,hvalue)
