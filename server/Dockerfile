# server
FROM python:3.10.11
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 9981
CMD ["python", "server.py"]

