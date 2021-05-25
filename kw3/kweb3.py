# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional
import time

# Pip
from web3 import Web3
from eth_account.signers.local import LocalAccount
from web3.middleware import geth_poa_middleware

from web3_erc20_predefined import *
from noraise import noraise

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: KWeb3 --------------------------------------------------------- #

class KWeb3(Web3):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        endpoint_uri: str,
        account_private_key: Optional[str] = None,
        use_poa_middleware: bool = False
    ):
        super().__init__(Web3.HTTPProvider(endpoint_uri))
        self.account = self.account_from_key(account_private_key) if account_private_key else None

        if use_poa_middleware:
            self.middleware_onion.inject(geth_poa_middleware, layer=0)


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def account_from_key(
        self,
        private_key: str
    ):
        return self.eth.account.from_key(private_key)

    @noraise()
    def is_transaction_validated(
        self,
        tx_hash: str
    ) -> Optional[bool]:
        ''' None means, the Transaction is not found'''
        return self.eth.getTransaction(tx_hash)['transactionIndex'] is not None

    def wait_till_transaction_is_validated(
        self,
        tx_hash: str,
        timeout_seconds: Optional[float] = None
    ) -> Optional[bool]:
        ''' None means, the Transaction is not found'''
        if timeout_seconds == 0:
            timeout_seconds = None

        start_ts = time.time()

        while timeout_seconds is None or time.time() - start_ts < timeout_seconds:
            is_valid = self.is_transaction_validated(tx_hash)

            if is_valid != False:
                return is_valid

        return is_valid

    def erc20(
        self,
        address: str,
        account: Optional[LocalAccount] = None
    ) -> ERC20:
        return ERC20(
            eth=self.eth,
            address=address,
            account=account or self.account
        )


    # Predefined - BSC

    def wbnb(
        self,
        account: Optional[LocalAccount] = None
    ) -> Wbnb:
        return Wbnb(
            eth=self.eth,
            account=account or self.account
        )

    def busd(
        self,
        account: Optional[LocalAccount] = None
    ) -> Busd:
        return Busd(
            eth=self.eth,
            account=account or self.account
        )

    # Predefined - BSC Testnet

    def wbnb_testnet(
        self,
        account: Optional[LocalAccount] = None
    ) -> TestWbnb:
        return TestWbnb(
            eth=self.eth,
            account=account or self.account
        )

    # Predefined - Eth

    def dai(
        self,
        account: Optional[LocalAccount] = None
    ) -> Dai:
        return Dai(
            eth=self.eth,
            account=account or self.account
        )

    def usdc(
        self,
        account: Optional[LocalAccount] = None
    ) -> USDC:
        return USDC(
            eth=self.eth,
            account=account or self.account
        )

    def usdt(
        self,
        account: Optional[LocalAccount] = None
    ) -> USDT:
        return USDT(
            eth=self.eth,
            account=account or self.account
        )

    def weth(
        self,
        account: Optional[LocalAccount] = None
    ) -> Weth:
        return Weth(
            eth=self.eth,
            account=account or self.account
        )


# -------------------------------------------------------------------------------------------------------------------------------- #