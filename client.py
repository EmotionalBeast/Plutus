import os

import rpyc
import logging.config

LOGGING_FILE = os.path.join(os.path.dirname(__file__), "logging.conf")
logging.config.fileConfig(LOGGING_FILE)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    conn = rpyc.connect('172.16.0.103', 9981)
    result = conn.root.my_selling_point('600183')
    logger.info(result)





