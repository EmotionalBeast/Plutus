# client
FROM python:3.10.11
WORKDIR /app_client
COPY . /app_client
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "client.py"]

# server
#FROM python:3.10.11
#WORKDIR /app
#COPY . /app
#RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 9981
#CMD ["python", "server.py"]

