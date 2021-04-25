# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3

# Local
from .pancakeswap_busd_liquidity_pool import PancakeswapBusdLiquidityPool

from ..pancakeswap_factory import PancakeswapFactory

from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------- class: PancakeswapBusdFactory ------------------------------------------------ #

class PancakeswapBusdFactory(PancakeswapFactory):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def getPairAddress(
        self,
        address: str,
    ) -> Optional[str]:
        return super().getPairAddress(Constants.BUSD.ADDRESS, address)

    def getPair(
        self,
        address: str,
    ) -> Optional[PancakeswapBusdLiquidityPool]:
        pair_address = self.getPairAddress(address)

        return PancakeswapBusdLiquidityPool(
            web3=self._web3,
            address=pair_address
        ) if pair_address else None


# -------------------------------------------------------------------------------------------------------------------------------- #