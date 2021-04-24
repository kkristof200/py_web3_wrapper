# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3

# Local
from .pancakeswap_wbnb_liquidity_pool import PancakeswapWbnbLiquidityPool

from ..pancakeswap_factory import PancakeswapFactory

from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------- class: PancakeswapWbnbFactory ------------------------------------------------ #

class PancakeswapWbnbFactory(PancakeswapFactory):

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def getPairAddress(
        self,
        address: str,
    ) -> Optional[str]:
        return super().getPairAddress(Constants.ADDRESS_WBNB, address)

    def getPair(
        self,
        address: str,
    ) -> Optional[PancakeswapWbnbLiquidityPool]:
        pair_address = self.getPairAddress(address)

        return PancakeswapWbnbLiquidityPool(
            web3=self._web3,
            address=pair_address
        ) if pair_address else None


# -------------------------------------------------------------------------------------------------------------------------------- #