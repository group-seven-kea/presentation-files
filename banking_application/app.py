from exchange import Exchange
import database
from cryptocurrency import Cryptocurrency
from flask import Flask, render_template, request, redirect, session
from bson.objectid import ObjectId
from os.path import abspath
from account import Account
from functools import wraps

app = Flask(__name__, template_folder=abspath("ui/templates"))
app.static_url_path = "/ui/static"
app.static_folder = app.root_path + app.static_url_path
app.secret_key = b"\xc4\xf8\x9d\xa8\xf7\xbc\t \x8f\xb6l\xea\xc5H\xfet"

user_accounts = database.connect()["bank"]["customers"]

def login_required(f):
    """ Make sure that user is logged in before proceeding. """
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        return redirect("/user/login")
    return wrap

@app.route('/', methods=["GET"])
def index_page():
    return redirect("/user/login")

@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    bank_account = database.connect()["bank"]["bank_accounts"].find_one({"_id": ObjectId(session["user"]["bank_account"])})
    crypto_wallet = database.connect()["bank"]["crypto_wallets"].find_one({"_id": ObjectId(session["user"]["crypto_wallet"])})
    return render_template("home.html", bank_account=bank_account, crypto_wallet=crypto_wallet)

@app.route('/user/login', methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template("login.html")
    return Account().login()

@app.route('/user/register', methods=["GET", "POST"])
def user_register():
    if request.method == "GET":
        return render_template("register.html")
    return Account().register()

@app.route('/user/logout')
def user_logout():
    return Account().logout()


@app.route('/dashboard/cryptocurrency', methods=["GET", "POST"])
@login_required
def cryptocurrency():
    crypto_wallet = database.connect()["bank"]["crypto_wallets"].find_one({"_id": ObjectId(session["user"]["crypto_wallet"])})
    bank_account = database.connect()["bank"]["bank_accounts"].find_one({"_id": ObjectId(session["user"]["bank_account"])})
    priceData = Cryptocurrency().get_data()
    return render_template("cryptocurrency.html", priceData=priceData, crypto_wallet=crypto_wallet, bank_account=bank_account)

@app.route('/dashboard/cryptocurrency/buy', methods=["POST"])
@login_required
def cryptocurrency_buy():
    return Exchange.buy(ObjectId(session["user"]["bank_account"]), ObjectId(session["user"]["crypto_wallet"]), session["user"]["phone_number"])

@app.route('/dashboard/cryptocurrency/sell', methods=["POST"])
@login_required
def cryptocurrency_sell():
    return Exchange.sell(ObjectId(session["user"]["bank_account"]), ObjectId(session["user"]["crypto_wallet"]), session["user"]["phone_number"])

@app.route('/dashboard/loans', methods=["GET", "POST"])
@login_required
def not_implemented():
    return render_template("coming_soon.html")

