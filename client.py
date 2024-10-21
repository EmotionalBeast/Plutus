import os

import logging.config

from flask import Flask
from flask_apscheduler import APScheduler
from client.config import Config

LOGGING_FILE = os.path.join(os.path.dirname(__file__), "logging.conf")
logging.config.fileConfig(LOGGING_FILE)
logger = logging.getLogger(__name__)



if __name__ == '__main__':
    app = Flask(__name__)
    scheduler = APScheduler()
    app.config.from_object(Config)
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', port=9982)





