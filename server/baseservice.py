import tushare as ts
from rpyc import Service

from util.bark import Bark
from util.config import Config


class BaseService(Service):
    config = Config()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tushare_token = BaseService.config.tushare_token
        self.bark = Bark(BaseService.config.bark_host, BaseService.config.bark_device_key, BaseService.config.bark_icon)
        self.pro = ts.pro_api(self.tushare_token)

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def send_notification(self, title, message):
        self.bark.send(title, message)


