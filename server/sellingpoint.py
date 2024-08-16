import tushare as ts
from server.baseservice import BaseService


class SellingPointService(BaseService):

    def __init__(self):
        super().__init__()
        self.pro = ts.pro_api(self.tushare_token)

    def exposed_my_selling_point(self, stock_symbol):
        df = self.pro.daily(ts_code=stock_symbol, start_date='20240101', end_date='20240801')
        return df
