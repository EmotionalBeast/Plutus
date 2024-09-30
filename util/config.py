import json
import os

CONFIG_FILE = os.path.join(os.path.split(os.path.dirname(__file__))[0], "config.json")


class Config(object):
    def __init__(self):
        with open(CONFIG_FILE) as config_file:
            self.config = json.load(config_file)

    @property
    def bark_host(self):
        return self.config['Bark']['host']

    @property
    def bark_icon(self):
        return self.config['Bark']['icon']

    @property
    def bark_device_key(self):
        return self.config['Bark']['device_key']
