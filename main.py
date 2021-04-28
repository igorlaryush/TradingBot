import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient
from interface.root_component import Root

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    binance = BinanceFuturesClient('ab83af351da6fe25c83d5fa06d4ced6772f2ec3c3b74950c64ce98ab7d94c2f3',
                                   '059317a743f4da70e55ad5b30db1a110a276886c76d67e40b28fb10fdaa4ef97', True)
    #bitmex = BitmexClient("uXr1T711wD-", "", True)
    print(binance.get_balances()['BNB'].wallet_balance)

    root = Root()
    root.mainloop()
