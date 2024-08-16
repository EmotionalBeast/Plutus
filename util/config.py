import json


class Config(object):
    def __init__(self):
        with open('../config.json') as config_file:
            self.config = json.load(config_file)

    @property
    def tushare_token(self):
        return self.config['Tushare']['token']

    @property
    def bark_host(self):
        return self.config['Bark']['host']

    @property
    def bark_icon(self):
        return self.config['Bark']['icon']

    @property
    def bark_device_key(self):
        return self.config['Bark']['device_key']
