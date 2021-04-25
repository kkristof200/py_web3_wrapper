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

    # alias
    baseTokenAddreess = token0Address


    def token0(self) -> Optional[Bep20]:
        if not self.__token0:
            token0Address = self.token0Address()

            self.__token0 = Bep20(self._web3, token0Address)

        return self.__token0

    # alias
    baseToken = token0


    def token1Address(self) -> Optional[str]:
        if not self.__token1_address:
            self.__token1_address = self.functions.token1().call()

        return self.__token1_address

    # alias
    quoteTokenAddreess = token1Address


    def token1(self) -> Optional[Bep20]:
        if not self.__token1:
            token1Address = self.token1Address()

            self.__token1 = Bep20(self._web3, token1Address)

        return self.__token1

    # alias
    quoteToken = token1


    def token0Price(self) -> Optional[float]:
        '''token1 for 1 token0'''
        reserves = self.getReserves()

        return reserves.token0Price(
            token_0_decimals=self.token0().decimals(),
            token_1_decimals=self.token1().decimals(),
        ) if reserves else None

    # alias
    baseTokenPrice = token0Price


    def token1Price(self) -> Optional[float]:
        '''token0 for 1 token1'''
        reserves = self.getReserves()

        return reserves.token1Price(
            token_0_decimals=self.token0().decimals(),
            token_1_decimals=self.token1().decimals(),
        ) if reserves else None

    # alias
    quoteTokenPrice = token1Price


    def toToken0(
        self,
        token1Amount: int
    ) -> Optional[float]:
        '''How much token0 for "token1Amount" token1'''
        token1Price = self.token1Price()

        return token1Amount * token1Price if token1Price else None

    # alias
    toBaseToken = toToken0


    def toToken1(
        self,
        token1Amount: int
    ) -> Optional[float]:
        '''How much token1 for "token0Amount" token0'''
        token0Price = self.token0Price()

        return token1Amount * token0Price if token0Price else None

    # alias
    toQuoteToken = toToken1


    # Forwarders

    def price0CumulativeLast(self) -> int:
        return self.functions.price0CumulativeLast().call()

    # alias
    baseTokenPriceCumulativeLast = price0CumulativeLast


    def price1CumulativeLast(self) -> int:
        return self.functions.price1CumulativeLast().call()

    # alias
    quoteTokenPriceCumulativeLast = price1CumulativeLast


    def getReserves(self) -> Optional[Reserves]:
        return self._getReserves(Reserves)


    # -------------------------------------------------- Private properties -------------------------------------------------- #

    def _getReserves(
        self,
        _type,
        **extra_args
    ) -> Optional[Reserves]:
        res = self.functions.getReserves().call()

        return _type(
            reserve0=res[0],
            reserve1=res[1],
            blockTimestampLast=res[2],
            **extra_args
        ) if res else None


# -------------------------------------------------------------------------------------------------------------------------------- #