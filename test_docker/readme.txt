# 在项目目录执行 (注意最后的点表示当前目录)
docker build -t my-python-app:latest .

# 运行容器
docker run -d -p 5000:5000 --name my-app my-python-app
-d detached 后台运行 
-p 端口映射 (主机端口：容器端口)
--name 为容器指定名称 

curl http://localhost:5000
# 输出: Hello World

# 查看容器状态
docker ps