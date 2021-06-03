# Live demo

    1. Live demo can be accessed here: http://keabank.tech/
    2. SMS microservice has been excluded from the live demo, as the balance from our sms provider is limited.
    3. It is still functional, so feel free to test it locally.
    4. First page load time can slightly longer as heroku after 30 mins of no traffic will go to "sleep mode".


# Banking application requirements

    1. Download the required files and extract them from github or the uploadded .zip file.
    2. Navigate to the top-level folder that contains requirements.txt.
    3. Open terminal, run "pip install -r requirements.txt" to install all of the requirements.

# Environmental variables

    1. Depending on the operating system, set up the necessary environmental variables.
    2. MONGODB_CONNECTION_STRING (MongoDB SRV string): mongodb+srv://tom:parole123@banking-app-python.zfwkg.mongodb.net/
    3. COIN_API_KEY (coinapi.io api key): 0C261169-D7AA-4B12-A252-78D3C7F3B83D
    4. FLASK_APP (name of the main file): app.py
    5. Alternatively insert those values in database.py, and cryptocurrency.py respectively.

# Running the application

    1. Ensure that you have restarted your terminal after setting the environmental variables.
    2. Type "flask run" to start the banking application
    3. An IP will be displayed to which you will be able to connect to.
    4. Register or Login with our test account, assuming that you are connecting to our database:
        CPR: 2710001234
        Password: 123
    5. Home page - Overview of the accounts, balances in crypto wallet and bank account
    6. Loans page - Another context, has not been implemented due to the time constraints.
    7. Cyptocurrency - Trading of the cryptocurrency, can buy and sell cryptocurrency with the balance in bank account.

# Setting up the SMS microservice

    1. Install the RabbitMQ server, or connect to one remotely. (localhost works fine as proof of concept)
    2. Start your RabbitMQ service either locally or on a remote server.
    3. In notifications/send_sms set up your public/private keys. 
    ("AC34d49b3064b283478371ff8859b8c819", "03e6dfcfd06969c1b53f2d5c5de9ab9f")
    4. Open terminal and write "python send_sms.py" to start the microservice.


