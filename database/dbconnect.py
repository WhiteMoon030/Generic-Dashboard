import sqlite3
import hashlib

# relative path to database
database_path = "database/dashboard.db"
# get salt string
salt_file = open("database/salt","r")
salt = salt_file.readline()
salt_file.close()

# function to check if a username already exists
def exist_user(username: str) -> bool:
    # connect to database and execute query
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    sql_query = "SELECT * FROM users WHERE username = ?"
    arguments = (username, )
    result = cur.execute(sql_query, arguments)
    result = result.fetchone()
    con.close()
    # If entry with username exists => True
    if result:
        return True
    # Otherwise => False
    return False

# function to add a user
def add_user(username: str, password: str) -> None:
    # hash password string
    passwordhash = password + salt
    passwordhash = hashlib.sha256(passwordhash.encode("UTF-8")).hexdigest()

    # connect to database and execute query
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    sql_query = "INSERT INTO users (username, password) VALUES(?,?)"
    arguments = (username, passwordhash)
    cur.execute(sql_query, arguments)
    con.commit()
    con.close()
    return


# function to validate user login
def login_successfull(username: str, password: str) -> int:
    # hash password string
    passwordhash = password + salt
    passwordhash = hashlib.sha256(passwordhash.encode("UTF-8")).hexdigest()

    # connect to database and execute query
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    sql_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    arguments = (username, passwordhash)
    result = cur.execute(sql_query, arguments)
    result = result.fetchone()
    con.close()

    # if query find a user => return userId
    if result:
        return result[0]
    # if not return zero
    return 0
