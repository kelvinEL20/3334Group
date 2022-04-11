import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
)

# Check if username and password are correct, return bool
def checkLogin(username, password):
    username = str(username)
    password = str(password)
    
    
    
    db.close()
    return

if __name__ == "__main__":
    checkLogin("aaa", "bbb")
