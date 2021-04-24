# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import List

# Pip
from web3 import Web3
from web3.contract import ContractFunctions, Contract as Web3Contract

# Local
from .wrapped_function import WrappedFunction

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------- class: WrappedContract ---------------------------------------------------- #

class WrappedContract:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3,
        address: str,
        abi: List[dict]
    ):
        self.__web3 = web3
        self.__address = address
        self.__abi = abi

        self.__contract = web3.eth.contract(address=Web3.toChecksumAddress(address), abi=abi)


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def _web3(self) -> Web3:
        return self.__web3

    @property
    def address(self) -> str:
        return self.__address

    @property
    def abi(self) -> str:
        return self.__abi

    @property
    def contract(self) -> Web3Contract:
        return self.__contract

    @property
    def functions(self) -> ContractFunctions:
        return self.__contract.functions


# -------------------------------------------------------------------------------------------------------------------------------- #