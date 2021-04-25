# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional
import random

# Pip
from web3 import Web3

# Local
from .constants import Constants

from .contracts import *

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: Web3Wrapper ------------------------------------------------------ #

class Web3Wrapper:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        endpoint_uri: Optional[str] = None
    ):
        self.__web3 = Web3(Web3.HTTPProvider(endpoint_uri or random.choice(Constants.BSC_ENDPOINT_URIS)))


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def is_connected(self) -> bool:
        return self.__web3.isConnected()

    @property
    def web3(self) -> Web3:
        return self.__web3


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def balance(
        self,
        address: str
    ) -> int:
        return self.__web3.eth.get_balance(address)

    def bep20(
        self,
        address: str
    ) -> Bep20:
        return Bep20(self.__web3, address)

    def wbnb(self) -> Wbnb:
        return Wbnb(self.__web3)

    def busd(self) -> Wbnb:
        return Busd(self.__web3)


# -------------------------------------------------------------------------------------------------------------------------------- #