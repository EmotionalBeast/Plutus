from rpyc import ThreadedServer

from server.sellingpoint import SellingPointService

if __name__ == '__main__':
    s = ThreadedServer(service=SellingPointService, port=9988, auto_register=False)
    s.start()
