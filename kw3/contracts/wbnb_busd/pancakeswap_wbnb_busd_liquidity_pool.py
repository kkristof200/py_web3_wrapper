# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3

# Local
from .busd import Busd
from .reserves_wbnb_busd import ReservesWbnbBusd

from ..wbnb import PancakeswapWbnbLiquidityPool
from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------- class: PancakeswapWbnbBusdLiquidityPool ------------------------------------------- #

class PancakeswapWbnbBusdLiquidityPool(PancakeswapWbnbLiquidityPool):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3
    ):
        super().__init__(
            web3=web3,
            address=Constants.ADDRESS_LIQUIDITY_POOL_WBNB_BUSD
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Custom

    def busdAddress(self) -> Optional[str]:
        return super().tokenAddress()

    def busd(self) -> Optional[Busd]:
        return super().token()

    def priceBusdCumulativeLast(self) -> int:
        return self.price0CumulativeLast()

    def getReserves(self) -> Optional[ReservesWbnbBusd]:
        return self._getReserves(ReservesWbnbBusd)

    def busdPrice(self) -> Optional[float]:
        '''BNB for 1 BUSD'''
        return self.tokenPrice()


# -------------------------------------------------------------------------------------------------------------------------------- #