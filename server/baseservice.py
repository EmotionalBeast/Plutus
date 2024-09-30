from rpyc import Service

import qstock as qs


class BaseService(Service):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qs = qs

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass


