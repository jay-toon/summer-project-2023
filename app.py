import mysql.connector # Allows us to connect to the database

database = mysql.connector.connect(host='localhost', database='users', user='root', password='') # Connects to the database
mysql = database.cursor()

def checkUsername(username): # Strips username input, checks if the username exists in the database, and returns whether the username exists or not
    username = username.strip()
    selectQuery = "SELECT * FROM users.user WHERE username = %s" # Defines the query to be used in the following line
    mysql.execute(selectQuery, (username,)) # Executes the query
    usernameExists = mysql.fetchone()

    if usernameExists != None: # If the username does not exist in the database, returns False
        print("This username is already in use, please choose another username.")
        return False
    return True

def checkEmail(email): # Strips email input, checks if the email exists in the database, and returns whether the username exists or not
    email = email.strip()
    selectQuery = "SELECT * FROM users.user WHERE email = %s" # Defines the query to be used in the following line
    mysql.execute(selectQuery, (email,)) # Executes the query
    emailExists = mysql.fetchone()

    if emailExists != None: # If the emial does not exist in the database, returns False
        print("This email has already been registered, please contact support if this is an issue.")
        return False
    return True

def login(): # Takes in username and password input, checks with database, and informs the user whether the login was successful or not
    while (not database.is_connected()): # If the database is not connected, it will loop
        print("Type \"break\" to exit the login process")
        email = input("Email: ")
        password = input("Password: ")

        database = mysql.connector.connect(email=email, password=password, host='localhost', database='database') # Sends request to the database in the host machine
        if (database.is_connected()): # IF the user has submitted correct credentials, it will log them in
            return True # Logged In
        return False # Login Failed

def register(): # Allows the user to register a new user, checks if the username/email is already in use, and then allows the registration to follow through
    print("Type \"break\" to exit the registration process")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    while checkUsername(username) == False:
        username=input("Username: ")
        if username == "exit": break

    while checkEmail(email) == False:
        email=input("Email: ")
        if email == "exit": break
    
    password = input("Password: ")
    
    insert_query = "INSERT INTO users.user (username, password, email) VALUES (%s, %s, %s)" # Defines the query to be used in the following line
    mysql.execute(insert_query, (username, password, email)) # Inserts the username, password, and email into the database

selection = input("What would you like to do?\n1. Login\n2. Register\n")

if selection == "1":
    login()
elif selection == "2":
    register()
