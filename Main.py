import tushare as ts
from util.bark import Bark

from util.config import Config

if __name__ == '__main__':
    config = Config()

    ts.set_token(config.tushare_token)
    pro = ts.pro_api()
    df = pro.daily(ts_code='600183.SH', start_date='20240101', end_date='20240801')
    print(df)

    title = 'Stock Analysis'
    content = '生益科技（600183）达到卖点，请尽快处理。'

    bark = Bark(config.bark_host, config.bark_device_key, config.bark_icon)
    if bark.send_message(title, content):
        print('send success')




