FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt # 太大了，容易超时
RUN pip install --no-cache-dir -r requirements.txt \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/
# 使用国内的镜像pypi源

COPY . .

CMD ["python", "app.py"]