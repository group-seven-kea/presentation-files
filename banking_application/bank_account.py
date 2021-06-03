import database

client = database.connect()["bank"]["bank_accounts"]

class BankAccount:
    """
    A class used to represent a traditional bank account.
    Attributes:
    ----------
    type (string): type of the account - Savings, Platinum Savings.
    balance (float): initial balance that the user will be provided with (in case of promotions)
    transactions (list): list of transactions that the banking account has (not implemented). 
    """
    def __init__(self, type, balance):
        self.type = type
        self.balance = balance
        self.transactions = []
    
    def store_account(self):
        """ Inserts the newly created bank account into the bank_accounts collection.  """
        return client.insert_one(self.create_account_object())

    def create_account_object(self):
        """ Creates a new account object, will be user to store this into the crypto_wallets collection.  """
        return {"account_type": self.type, "balance": self.balance, "transactions": self.transactions}
