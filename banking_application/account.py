from flask import request, jsonify, session, redirect
from bank_account import BankAccount
from crypto_wallet import CryptoWallet
from argon2 import PasswordHasher


import database

db = database.connect()["bank"]["customers"]

class Account:
    """
    A class used to represent an user account for our bank.
    """
    def start_session(self, user):
        """ Start a session with user (password and id fields removed) and returns a JSON response. 

        Args:
            user: the user account that was either created or fetched from the database.
        """
        del user["password"], user["_id"]
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200

    def login(self):
        """ Finds an user account by the CPR number and validates password. """
        user_account = db.find_one({"cpr_number": request.form.get("CPR")})
        if user_account is not None:
            if self.verify_password(user_account["password"], request.form.get("password")):
                return self.start_session(user_account)
        return jsonify({"error": "Invalid login credentials"}), 401

    def logout(self):
        """ Clears the session and redirects the user to login page. """
        session.clear()
        return redirect("/user/login")

    def register(self):
        """ Creates an user object, and inserts the account into the database and starts a new session. """
        if self.fields_not_empty(request, ["first_name", "last_name", "age", "CPR", "email", "phone_number", "password", "confirm_password"]):
            return jsonify({"error": "Some fields are empty"}), 400
        user = self.create_user_object(request)
        if request.form.get("password") != request.form.get("confirm_password"):
            return jsonify({"error": "Passwords did not match"}), 400
        db.insert_one(user)
        return self.start_session(user)

    def create_user_object(self, request):

        """ Method returns a new user object that will be later used for registration function.  
        
        Args:
            request: the data from the form the user filled out, used to create a new user.
        """
        user = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "age": request.form.get("age"),
            "cpr_number": request.form.get("CPR"),
            "email": request.form.get("email"),
            "phone_number": request.form.get("phone_number"),
            "password": PasswordHasher().hash(request.form.get("password")),
            "bank_account": str(BankAccount("Savings", 1000.00).store_account().inserted_id),
            "crypto_wallet": str(CryptoWallet("Bitcoin", 0.0045).store_account().inserted_id)
        }
        return user

    def verify_password(self, hash, password):
        """ Verify the provided password and compare it with the stored hash of the password.  
        
        Args:
            hash: hashed password for the account in the database.
            password: the password user provided in the login form.
        """
        try:
            PasswordHasher().verify(hash, password)
            return True
        except:
            return False
        
    def fields_not_empty(self, request, fields):
        """ Validate that the input fields are not empty  
        
        Args:
            request: GET request from the form.
            fields: List of fields.
        """
        for field in fields:
            if request.form.get(field) == "":
                return True
