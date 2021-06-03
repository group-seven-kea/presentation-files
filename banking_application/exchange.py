import database
from cryptocurrency import Cryptocurrency
from flask import request, jsonify
from sms_notify import send_sms

client = database.connect()
crypto_wallets = client["bank"]["crypto_wallets"]

class Exchange:
    @staticmethod
    def buy(account_id, wallet_id, phone_nr):
        """ Exchanges balance in user's bank account to the equivalent in the selected cryptocurrency.  
        
        Args:
            account_id: ID of the bank account for the user.
            wallet_id: ID of the cryptocurrency wallet for the user.
        """
        if request.form.get("amount") == "":
            return jsonify({"error": "Quantity not provided"}), 400
        coins = float(request.form.get("amount"))
        bank_account = client["bank"]["bank_accounts"].find_one({"_id": account_id})
        crypto_wallet = crypto_wallets.find_one({"_id": wallet_id})
        value_in_dkk = Cryptocurrency.present_value("BTC") * coins
        if bank_account["balance"] >= value_in_dkk:
            client["bank"]["bank_accounts"].update_one(bank_account, 
            {
                "$set": {
                    "balance": float(round(bank_account["balance"] - value_in_dkk, 2))
                }
            })
            crypto_wallets.update_one(crypto_wallet, {
                "$set": {
                    "balance": crypto_wallet["balance"] + coins
                }
            })
            send_sms(phone_nr, f"You have succesfully purchased BTC {coins} for DKK {round(value_in_dkk, 2)}")
            return jsonify({"success": "Succesfully purchased coins"}), 200
        return jsonify({"error": f"Insufficient balance. \nYou tried to purchase DKK {round(value_in_dkk,2)} worth of BTC when you only have DKK {bank_account['balance']}"}), 400
        
            
    @staticmethod
    def sell(account_id, wallet_id, phone_nr):
        """ Exchanges the selected cryptocurrency to the equivalent in DKK in user's bank account. 
        
        Args:
            account_id: ID of the bank account for the user.
            wallet_id: ID of the cryptocurrency wallet for the user.
        """
        if request.form.get("amount") == "":
            return jsonify({"error": "Quantity not provided"}), 400
        coins = float(request.form.get("amount"))
        bank_account = client["bank"]["bank_accounts"].find_one({"_id": account_id})
        crypto_wallet = crypto_wallets.find_one({"_id": wallet_id})
        value_in_dkk = Cryptocurrency.present_value("BTC") * coins
        if crypto_wallet["balance"] >= coins:
            client["bank"]["bank_accounts"].update_one(bank_account, 
            {
                "$set": {
                    "balance": float(round(bank_account["balance"] + value_in_dkk, 2))
                }
            })
            crypto_wallets.update_one(crypto_wallet, {
                "$set": {
                    "balance": crypto_wallet["balance"] - coins
                }
            })
            send_sms(phone_nr, f"You have succesfully sold BTC {coins} for DKK {round(value_in_dkk, 2)}")
            return jsonify({"success": "Succesfully sold coins"}), 200
        return jsonify({"error": f"Insufficient balance. \nYou tried to sell BTC {coins} when you only have BTC{round(crypto_wallet['balance'], 5)}"}), 400