from General_online import *
import mysql.connector
import random
import hashlib

# Add user credentials into database, retun True if success
def register(username, password):
    db = mysql.connector.connect(
    host = "database-1.cxdirld1qchg.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "12345678",
    database = "3334group"
    )
    
    cur = db.cursor()
    
    username = str(username)
    password = str(password)
    salt = str(random.randint(1, 9999))
    forHash = password + salt
    hash = hashlib.sha256(forHash.encode('utf-8')).hexdigest()
    
    sql = "SELECT username FROM login_table WHERE username = %s"
    val = (username, )
    cur.execute(sql, val)
    allUsername = cur.fetchall()
    
    if not allUsername:
        sql = "INSERT INTO login_table (username, salt, pw_hash) VALUES (%s, %s, %s)"
        val = (username, salt, hash)
        cur.execute(sql, val)
        db.commit()
        db.close()
        return True
    else:
        showAlert("Username have already been used")
        db.close()
        return False
    