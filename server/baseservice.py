from rpyc import Service

from util.config import Config


class BaseService(Service):
    config = Config()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tushare_token = BaseService.config.tushare_token
        self.bark_host = BaseService.config.bark_host
        self.bark_device_key = BaseService.config.bark_device_key
        self.bark_icon = BaseService.config.bark_icon

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

