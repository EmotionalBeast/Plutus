from rpyc import Service

from client.util import Config
import qstock as qs


class BaseService(Service):
    config = Config()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qs = qs

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass


