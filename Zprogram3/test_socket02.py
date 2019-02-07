import socket

# 1. 创建socket
def main():
    while(True):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2. 绑定一个port
        local_addr = ("", 8000)
        udp_socket.bind(local_addr)
# 3. 接受数据
        recv_data = udp_socket.recvfrom(1024)
    #recvfrom返回的是(byte数据, (src_ip, src_port))
# 4. 解析数据
        recv_addr = recv_data[1]  # 存储地址
        recv_msg = recv_data[0]  # 存储数据
# 5. 退出控制
        if recv_msg == b'exit':
            break
# 6. 打印数据
        print(recv_addr,": ",recv_msg.decode('utf-8'))
# 7. 关闭socket
    udp_socket.close()

if __name__ == "__main__":
    main()
