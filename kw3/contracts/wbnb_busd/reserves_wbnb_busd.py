# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Local
from ..wbnb import ReservesWbnb
from ...constants import Constants

# -------------------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------------- class: ReservesWbnbBusd --------------------------------------------------- #

class ReservesWbnbBusd(ReservesWbnb):

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def reservesBusd(self) -> int:
        return self.reserveToken

    @property
    def busd_wbnb_rate(self) -> float:
        return self.token_wbnb_rate

    @property
    def wbnb_busd_rate(self) -> float:
        return self.wbnb_token_rate


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def busdPrice(self) -> float:
        '''BNB for 1 BUSD'''
        return self.token0Price(Constants.BUSD.DECIMALS, Constants.WBNB.DECIMALS)

    def wbnbPrice(self) -> float:
        '''BUSD for 1 BNB'''
        return self.token1Price(Constants.BUSD.DECIMALS, Constants.WBNB.DECIMALS)


# -------------------------------------------------------------------------------------------------------------------------------- #