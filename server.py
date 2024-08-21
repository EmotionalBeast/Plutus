import logging.config
import os

from rpyc import ThreadedServer

from server.sellingpoint import SellingPointService

LOGGING_FILE = os.path.join(os.path.dirname(__file__), "logging.conf")
logging.config.fileConfig(LOGGING_FILE)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Starting server')
    s = ThreadedServer(service=SellingPointService, port=9981, auto_register=False)
    s.start()
    logger.info('Server started')
