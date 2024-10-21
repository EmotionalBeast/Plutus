# 选择一个基础镜像，例如 Python 3
FROM python:3.10.11

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到容器中
COPY .. /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# server
#EXPOSE 9981
#CMD ["python", "server.py"]

# client
EXPOSE 5000
CMD ["python", "client.py"]