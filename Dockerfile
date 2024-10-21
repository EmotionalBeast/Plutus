# 选择一个基础镜像，例如 Python 3
FROM python:3.10.11

#WORKDIR /app
#COPY .. /app

# 设置工作目录
WORKDIR /app_client
COPY .. /app_client

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# server
#EXPOSE 9981
#CMD ["python", "server.py"]

# client
EXPOSE 5000
CMD ["python", "client.py"]