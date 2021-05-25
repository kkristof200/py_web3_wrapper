from web3._utils.abi import abi_to_signature

from kw3 import KWeb3

w3 = KWeb3('https://bsc-dataseed.binance.org/')

busd = w3.busd()
method = busd.balance_of_method('0xA426d6e651aAFcd6e26865d65286c64f34714428')

# print(method.abi)
print(busd.method_signature(method))