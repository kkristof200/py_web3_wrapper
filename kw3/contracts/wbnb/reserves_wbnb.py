# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Local
from ..pancakeswap_liquidity_pool import Reserves

from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: ReservesWbnb ----------------------------------------------------- #

class ReservesWbnb(Reserves):

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def reserveToken(self) -> int:
        return self.reserve0

    @property
    def reserveWbnb(self) -> int:
        return self.reserve1

    @property
    def token_wbnb_rate(self) -> float:
        return self.token0_token1_rate

    @property
    def wbnb_token_rate(self) -> float:
        return self.token1_token0_rate


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def tokenPrice(
        self,
        token_decimals: int
    ) -> float:
        '''BNB for 1 Token'''
        return self.token0Price(token_decimals, Constants.WBNB.DECIMALS)

    def wbnbPrice(
        self,
        token_decimals: int
    ) -> float:
        '''Token for 1 BNB'''
        return self.token1Price(token_decimals, Constants.WBNB.DECIMALS)


# -------------------------------------------------------------------------------------------------------------------------------- #