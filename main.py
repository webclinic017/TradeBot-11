import alpaca_trade_api as tradeapi
import numpy as np
import time


SEC_KEY = 'QzEjCqivJgBpqKwMIbwCFvi6UJfJFLQFnet1Z3z2'  # Secret key here
PUB_KEY = 'PKRJ0ZV37O592S4C5LLK'  # public key here
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
api = tradeapi.REST(key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) # For real trading, don't enter a base_url




# buy

api.submit_order(
    symbol='SPY',
    qty=100,
    side='buy',
    type='market',
    time_in_force='gtc'  # good till cancelled
)

