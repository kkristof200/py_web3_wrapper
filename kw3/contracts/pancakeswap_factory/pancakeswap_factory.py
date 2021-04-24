# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3

# Local
from ._abi import pancakeswap_factory_abi

from ..core import WrappedContract
from ..pancakeswap_liquidity_pool import PancakeswapLiquidityPool
from ..wbnb import PancakeswapWbnbLiquidityPool

from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------- class: PancakeswapFactory -------------------------------------------------- #

class PancakeswapFactory(WrappedContract):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3
    ):
        super().__init__(
            web3=web3,
            address=Constants.ADDRESS_PANCAKESWAP_FACTORY,
            abi=pancakeswap_factory_abi
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Forwarders

    def allPairsLength(self) -> int:
        return self.functions.allPairsLength().call()


    # Custom

    def getPairAddress(
        self,
        address0: str,
        address1: str
    ) -> Optional[str]:
        return self.functions.getPair(
            Web3.toChecksumAddress(address0),
            Web3.toChecksumAddress(address1)
        ).call()

    def getPair(
        self,
        address0: str,
        address1: str
    ) -> Optional[PancakeswapLiquidityPool]:
        pair_address = self.getPairAddress(address0, address1)

        return PancakeswapLiquidityPool(
            self._web3,
            pair_address
        ) if pair_address else None

    def getWBNBPair(
        self,
        address: str
    ) -> Optional[PancakeswapWbnbLiquidityPool]:
        return self.getPair(Constants.ADDRESS_WBNB, address)


# -------------------------------------------------------------------------------------------------------------------------------- #