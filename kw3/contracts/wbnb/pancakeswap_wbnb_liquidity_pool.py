# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3

# Local
from .wbnb import Wbnb
from .reserves_wbnb import ReservesWbnb

from ..pancakeswap_liquidity_pool import PancakeswapLiquidityPool
from ..bep20 import Bep20

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- class: PancakeswapWbnbLiquidityPool --------------------------------------------- #

class PancakeswapWbnbLiquidityPool(PancakeswapLiquidityPool):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Proxies

    def tokenAddress(self) -> Optional[str]:
        return super().token0Address()

    def token(self) -> Optional[Bep20]:
        return super().token0()

    def wbnbAddress(self) -> Optional[str]:
        return super().token1Address()

    def wbnb(self) -> Optional[Wbnb]:
        return super().token1()

    def priceTokenCumulativeLast(self) -> int:
        return self.price0CumulativeLast()

    def priceWbnbCumulativeLast(self) -> int:
        return self.price1CumulativeLast()

    def getReserves(self) -> Optional[ReservesWbnb]:
        return self._getReserves(ReservesWbnb)

    def tokenPrice(self) -> Optional[float]:
        '''BNB for 1 Token'''
        return self.token0Price()

    def wbnbPrice(self) -> Optional[float]:
        '''Token for 1 BNB'''
        return self.token1Price()

# -------------------------------------------------------------------------------------------------------------------------------- #