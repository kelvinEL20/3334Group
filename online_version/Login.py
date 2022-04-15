import mysql.connector
import hashlib

# Check if username and password are correct, return bool
def checkLogin(username, password):
    username = str(username)
    password = str(password)
    
    db = mysql.connector.connect(
    host = "database-1.cxdirld1qchg.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "12345678",
    database = "3334group"
    )
    
    cur = db.cursor()
    
    sql = "SELECT username, salt, pw_hash FROM login_table WHERE username = %s"
    val = (username, )
    cur.execute(sql, val)
    credentials = cur.fetchall()
    if not credentials: # Username not found
        db.close()
        return False
    else:
        salt = credentials[0][1]
        hash = credentials[0][2]
        tempStr = password + salt
        newHash = hashlib.sha256(tempStr.encode('utf-8')).hexdigest()
        return newHash == hash
