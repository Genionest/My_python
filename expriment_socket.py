#导入socket库
import socket
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80)) #里面的参数是一个tuple

#接收数据
buffer = []
while True:
    #每次最多接收1k字节
    d= s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer) #把分段的字节连接在一起

#关闭连接
s.close()

#接收到的数据包括http头和网页本身
#将http头打印出来，网页内容保存到文件
#t = type(data.split('\r\n\r\n',1)) #t是type对象，具体点就是<class 'list'>
print(data)
#header,html = data.split('\r\n\r\n',1)
#print(header)
#把接收的数据写入文件
#with open('sina.html','wb') as f:
#    f.write(html)
