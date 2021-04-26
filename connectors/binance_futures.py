import logging
from pprint import pprint

import requests

logger = logging.getLogger()


class BinanceFuturesClient:
    def __init__(self, testnet):
        if testnet:
            self.base_url = 'https://testnet.binancefuture.com'
        else:
            self.base_url = 'http://api.binance.com'

        logger.info("Binance Futures Client successfully initialized")

        self.prices = dict()

    def make_request(self, method, endpoint, data):
        if method == 'GET':
            response_object = requests.get(self.base_url + endpoint, params=data)
        else:
            raise ValueError()

        if response_object ==  200:
            return response_object.json()
        else:
            logger.error('Error while %s making request to %s:', method, endpoint, response_object.json())
            return None

    def get_contracts(self):
        exchange_info = self.make_request('GET', '/api/v3/exchangeInfo', None)

        contracts = dict()

        if exchange_info is not  None:
            for contract_data in exchange_info['symbols']:
                contracts[contract_data['symbol']] = contract_data

        return contracts

    def get_historical_candles(self, symbol, interval):
        data = dict()
        data['symdol'] = symbol
        data['interval'] = interval
        data['limit'] = 1000

        raw_candles = self.make_request('GET', '/api/v3/klines', data)

        candles = []

        if raw_candles is not None:
            for c in raw_candles:
                candles.append([c[0], float(c[1]), float(c[2]), float(c[4]), float(c[5])])
        return

    def get_bid_ask(self, symbol):
        data = dict()
        data['symbol'] = symbol
        ob_data = self.make_request('GET', '/api/v3/ticker/bookTicker', data)

        if ob_data is not None:
            if symbol not in self.prices:
                self.prices[symbol] = {'bid': float(ob_data['bidPrice']), 'ask': float(ob_data['askPrice'])}
            else:
                self.prices[symbol]['bid'] = float(ob_data['bidPrice'])
                self.prices[symbol]['ask'] = float(ob_data['askPrice'])

        return self.prices[symbol]
