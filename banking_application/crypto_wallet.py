import database
import string
import random
from flask import jsonify


client = database.connect()
crypto_wallets = client["bank"]["crypto_wallets"]


class CryptoWallet:
    """ A class used to represent a cryptocurrency wallet.
    
    Args:
        coin: type of the cryptocurrency - Bitcoin, Ethereum.
        balance: initial balance that the user will be provided with (in case of promotions)
        transactions: list of transactions that the wallet has (not implemented). 
    """

    def __init__(self, coin, balance):
        self.coin = coin
        self.address = self.generate_address()
        self.balance = balance
        self.transactions = []

    def store_account(self):
        """ Inserts the newly created crypto wallet into the crypto_wallets collection.  """
        return crypto_wallets.insert_one(self.create_account_object())

    def create_account_object(self):
        """ Creates a new account object, will be user to store this into the crypto_wallets collection.  """
        return {"coin_id": self.coin, "address": self.address, "balance": self.balance, "transactions": self.transactions}


    @staticmethod
    def generate_address():
        """ Proof of concept function, in reality an actual wallet will be created for the user. """
        return "".join((random.choice(string.ascii_lowercase) for _ in range(34)))

 