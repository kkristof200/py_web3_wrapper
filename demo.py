from kw3 import KWeb3
from web3 import Web3

endpoint_uri = 'https://bsc-dataseed.binance.org'

_w3 = Web3(Web3.HTTPProvider(endpoint_uri))
print('_w3', _w3)
w3 = KWeb3(endpoint_uri)
print('w3', w3)