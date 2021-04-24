from kw3 import *


token_address = '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3'
# token_address = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'

w3 = Web3Wrapper()

print(w3.is_connected)

wbnb_busd = w3.pancakeswap_wbnb_busd_liquidity_pool()
wbnb = wbnb_busd.wbnb()
busd = wbnb_busd.busd()


busd_per_wbnb = wbnb_busd.busdPrice()
wbnb_per_busd = wbnb_busd.wbnbPrice()
print('busd_per_wbnb', busd_per_wbnb)
print('wbnb_per_busd', wbnb_per_busd)


pair = w3.pancakeswap_wbnb_liquidity_pool_for_token(token_address)
reserves = pair.getReserves()

wbnb_per_token = pair.wbnbPrice()
print('wbnb_per_token', wbnb_per_token)

busd_per_token = wbnb_per_token / busd_per_wbnb
print('busd_per_token', busd_per_token)