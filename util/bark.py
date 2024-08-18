import requests
from urllib.parse import urljoin


class Bark:
    def __init__(self, host, key, icon):
        self.host = host
        self.key = key
        self.icon = icon

    def send(self, title, message):
        url = urljoin(self.host, 'push')
        data = {
            'title': title,
            'body': message,
            'icon': self.icon,
            'device_key': self.key
        }
        response = requests.post(url=url, json=data)
        if response.status_code == 200:
            return True
        return False
