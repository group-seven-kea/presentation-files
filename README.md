# Live demo
    We also have hosted the banking application you can connect to it through domain "http://keabank.tech/"
    SMS microservice has been excluded from the live demo, as the balance from our sms provider is limited.
    It is still functional, so feel free to test it locally.
    First page load time can be a bitlonger as heroku after 30 mins of no traffic will go to "sleep mode"


# Banking application requirements

    1. Download the required files and extract them.
    2. Navigate to the top-level folder that contains requirements.txt
    3. Open terminal, run "pip install -r requirements.txt"

# Environmental variables

    1. Depending on the operating system, set up the necessary environmental variables.

    * MONGODB_CONNECTION_STRING: mongodb srv string. (mongodb+srv://tom:parole123@banking-app-python.zfwkg.mongodb.net/)
    * COIN_API_KEY: coinapi.io api key. (0C261169-D7AA-4B12-A252-78D3C7F3B83D)
    * FLASK_APP: name of the main file. (app.py)

    Alternatively insert those values in database.py, and cryptocurrency.py respectively.

# Running the application

    1. Ensure that you have restarted your terminal after setting the environmental variables.
    2. Type "flask run"
    3. An IP will be displayed to which you will be able to connect to.
    4. Register or Login with our test account:
        CPR: 2710001234
        Password: 123
    5. Home page - account overview
    6. Loans page - another context, not implemented.
    7. Cyptocurrency - main trading part of the bank.

# Setting up the SMS microservice

    1. Install RabbitMQ server, or connect to one remotely. (localhost works fine as proof of concept.)
    2. Start your RabbitMQ service.
    3. In notifications/send_sms set up your public/private keys 
    ("AC34d49b3064b283478371ff8859b8c819", "03e6dfcfd06969c1b53f2d5c5de9ab9f")
    4. Start send_sms.py microservice


