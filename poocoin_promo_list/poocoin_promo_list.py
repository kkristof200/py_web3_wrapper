# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Pip
from web3 import Web3
from kw3 import WrappedContract

# Local
from ._abi import poocoin_promo_list_abi
from  .poocoin_promoted_unvetted_token import PoocoinPromotedUnvettedToken

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------- class: PoocoinPromoList --------------------------------------------------- #

class PoocoinPromoList(WrappedContract):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        web3: Web3
    ):
        super().__init__(
            web3=web3,
            address='0x3a05d30f7428fe2333fb23afa9a2bf2dc012316b',
            abi=poocoin_promo_list_abi
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def promotedTokenCount(self) -> int:
        return self.functions.messageLength().call()

    def promotedTokenAtIndex(
        self,
        index: int
    ) -> PoocoinPromotedUnvettedToken:
        res = self.functions.messages(index).call()

        return PoocoinPromotedUnvettedToken(
            address=res[0],
            telegram_url=res[1]
        )


# -------------------------------------------------------------------------------------------------------------------------------- #