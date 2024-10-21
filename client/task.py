import rpyc

from util.config import BarkConfig
from client.sqlhelper import SQLHelper
from util.bark import Bark


bark_config = BarkConfig()
bark = Bark(bark_config.bark_host, bark_config.bark_device_key, bark_config.bark_icon)


def volume_monitor():
    rpc_conn = rpyc.connect('172.16.0.103', 9981)
    try:
        db = SQLHelper()
        with db as (conn, cursor):
            cursor.execute('SELECT * FROM hold')
            rows = cursor.fetchall()
            for row in rows:
                ticker_symbol = row[0]
                ticker_name = row[1]
                res = rpc_conn.root.my_selling_point(ticker_symbol)
                if res['sell']:
                    title = 'Stock Analysis'
                    msg = ticker_name + '(' + ticker_symbol +')' + '达到卖点，请尽快处理!'
                    bark.send(title, msg)
    except Exception as e:
        print(e)
    finally:
        rpc_conn.close()
