import socket

def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #可以操作套接字

    while(True):
        print("----------run----------")
    #发送数据sendto(send_data, dest_addr)
    #send_data必须是bytes, dest_addr是个数组
        send_data = input("请输入内容:\n")
        if send_data == "exit":
            break
        dest_addr = ('192.168.43.168', 8000)
        udp_socket.sendto(send_data.encode("utf-8"), dest_addr )
    #关闭套接字
    udp_socket.close()
    print("----------done---------")

if __name__ == "__main__":
    main()
