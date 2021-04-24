# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System


# Pip
from web3 import Web3

# Local
from ..bep20 import Bep20
from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------------- class: Wbnb --------------------------------------------------------- #

class Wbnb(Bep20):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3
    ):
        super().__init__(
            web3=web3,
            address=Constants.WBNB.ADDRESS
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def name(self) -> int:
        return Constants.WBNB.NAME

    def symbol(self) -> int:
        return Constants.WBNB.SYMBOL

    def decimals(self) -> int:
        return Constants.WBNB.DECIMALS


# -------------------------------------------------------------------------------------------------------------------------------- #