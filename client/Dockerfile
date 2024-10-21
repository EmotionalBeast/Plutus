# client
FROM python:3.10.11
WORKDIR /app_client
COPY .. /app_client
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 9982
CMD ["python", "client.py"]

