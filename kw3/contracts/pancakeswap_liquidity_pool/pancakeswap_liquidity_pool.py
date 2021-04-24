# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Union, Tuple

# Pip
from web3 import Web3

# Local
from ._abi import pancakeswap_liquidity_pool_abi

from .reserves import Reserves
from ..bep20 import Bep20
from ..core import WrappedContract

from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------ class: PancakeswapLiquidityPool ----------------------------------------------- #

class PancakeswapLiquidityPool(Bep20):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3,
        address: str
    ):
        super().__init__(
            web3=web3,
            address=address,
            abi=pancakeswap_liquidity_pool_abi
        )

        self.__token0_address = None
        self.__token0 = None
        self.__token1_address = None
        self.__token1 = None

        # self.__factory = None
        # self.factory = PancakeswapFactory(web3)


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    # Custom

    def token0Address(self) -> Optional[str]:
        if not self.__token0_address:
            self.__token0_address = self.functions.token0().call()

        return self.__token0_address

    def token0(self) -> Optional[Bep20]:
        token0Address = self.token0Address()

        return Bep20(self._web3, token0Address) if token0Address else None

    def token1Address(self) -> Optional[str]:
        if not self.__token1_address:
            self.__token1_address = self.functions.token1().call()

        return self.__token1_address

    def token1(self) -> Optional[Bep20]:
        token1Address = self.token1Address()

        return Bep20(self._web3, token1Address) if token1Address else None

    def token0Price(self) -> Optional[float]:
        reserves = self.getReserves()

        return reserves.token0Price(
            token_0_decimals=self.token0().decimals(),
            token_1_decimals=self.token1().decimals(),
        ) if reserves else None

    def token1Price(self) -> Optional[float]:
        reserves = self.getReserves()

        return reserves.token1Price(
            token_0_decimals=self.token0().decimals(),
            token_1_decimals=self.token1().decimals(),
        ) if reserves else None


    # Forwarders

    def price0CumulativeLast(self) -> int:
        return self.functions.price0CumulativeLast().call()

    def price1CumulativeLast(self) -> int:
        return self.functions.price1CumulativeLast().call()

    def getReserves(self) -> Optional[Reserves]:
        return self._getReserves(Reserves)


    # -------------------------------------------------- Private properties -------------------------------------------------- #

    def _getReserves(
        self,
        _type
    ) -> Optional[Reserves]:
        res = self.functions.getReserves().call()

        return _type(
            reserve0=res[0],
            reserve1=res[1],
            blockTimestampLast=res[2]
        ) if res else None


# -------------------------------------------------------------------------------------------------------------------------------- #