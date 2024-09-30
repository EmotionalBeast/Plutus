
from server.baseservice import BaseService
import pandas as pd


class SellingPointService(BaseService):

    def exposed_my_selling_point(self, stock_symbol):
        limit = 60
        df = self.qs.get_data(stock_symbol, freq='d').tail(15)
        df_vol = pd.DataFrame(df['volume'], columns=['volume'])
        mean_vol = pd.DataFrame(df['volume'].rolling(window=10).mean())
        row_num = df_vol.shape[0]
        current_day_vol = df_vol.iloc[-1, -1]
        previous_day_mean_vol = mean_vol.iloc[row_num-2, -1]
        growth_rate = (current_day_vol - previous_day_mean_vol) / previous_day_mean_vol * 100
        if growth_rate >= limit:
            return {'sell': True, 'data': {'growth_rate': growth_rate}}
        return {'sell': False, 'data': {'growth_rate': growth_rate}}
