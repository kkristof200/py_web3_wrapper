# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System


# Pip
from web3 import Web3

# Local
from ._abi import bep20_abi

from ..core import WrappedContract

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: Bep20 --------------------------------------------------------- #

class Bep20(WrappedContract):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3,
        address: str,
        abi: str = bep20_abi
    ):
        super().__init__(
            web3=web3,
            address=address,
            abi=abi
        )

        self.__name = None
        self.__symbol = None
        self.__total_supply = None
        self.__decimals = None


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def name(self) -> str:
        if not self.__name:
            self.__name = self.functions.name().call()

        return self.__name

    def symbol(self) -> str:
        if not self.__symbol:
            self.__symbol = self.functions.symbol().call()

        return self.__symbol

    def totalSupply(self) -> int:
        if not self.__total_supply:
            self.__total_supply = self.functions.totalSupply().call()

        return self.__total_supply

    def decimals(self) -> int:
        if not self.__decimals:
            self.__decimals = self.functions.decimals().call()

        return self.__decimals

    def balanceOf(
        self,
        address: str
    ) -> int:
        return self.functions.balanceOf(address).call()


    # Custom

    def toWei(
        self,
        amount: int
    ) -> float:
        return amount * pow(10, self.decimals()) if self.decimals() > 0 else amount

    def toEth(
        self,
        amount: int
    ) -> float:
        return amount / pow(10, self.decimals()) if self.decimals() > 0 else amount

    def market_cap(
        self,
        price_per_token: int
    ) -> int:
        return price_per_token * self.totalSupply()


# -------------------------------------------------------------------------------------------------------------------------------- #