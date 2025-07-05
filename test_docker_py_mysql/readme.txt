# 构建并启动
docker compose up --build
# 启动所有在 docker compose.yml 中定义的服务
# --build：强制在启动前重建镜像（即使镜像已存在）

# 验证操作
docker ps
# 应看到mysql_db和py_app两个容器

# 查看Python应用输出：
py_app       | Database message: Initial test message
py_app       | Operation completed successfully!

# 验证数据库
docker exec -it mysql_db mysql -u user -p 
# 输入密码
USE mydb;
SELECT * FROM test_table;