from cgi import print_environ_usage
import mysql.connector
import hashlib
import requests
import base64
import string
import random
from datetime import datetime
from PIL import Image
from io import BytesIO

# Upload artwork details to artwork_table
def uploadToArtworkListTable(artName, artUrl):
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "INSERT INTO artwork_table (artwork_name, upload_datetime, artwork_url) VALUES (%s, %s, %s)"
    now = datetime.now()
    currentDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    val = (artName, currentDatetime, artUrl)
    cur.execute(sql, val)
    db.commit()
    db.close()
    
# Upload ownership of artwork to table the_chain
def uploadToChain_Own(userName, artName, artUrl):
    req = requests.get(artUrl)
    img = Image.open(BytesIO(req.content))
    buffer = BytesIO()
    img.save(buffer ,format="png") # jpeg and jpg can be saved as png, but png cannot be saved as jpeg
    base64Art = str(base64.b64encode(buffer.getvalue()))
    artHash = hashlib.sha256(base64Art.encode('utf-8')).hexdigest()
    
    # Get previous block's hash and nonce for current block
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "SELECT * FROM the_chain ORDER BY nonce DESC LIMIT 1"
    cur.execute(sql)
    latestBlock = cur.fetchall()
    if len(latestBlock) == 0: # First block
        prevHash = ""
        nonce = 1
    else:
        prevHash = latestBlock[0][8]
        nonce = int(latestBlock[0][0]) + 1
    db.close()
    
    # Get salt for key
    sign = genSign(userName, nonce)
    
    # Calculate hash for curremt_hash col of current block
    currentHash = calHash(nonce, prevHash, userName, sign, artName, artHash, "", userName)
    
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "INSERT INTO the_chain (previous_hash, user_name, user_sign, art_name, base64_art_hash, tran_from_to, upload_owner, current_hash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (prevHash, userName, sign, artName, artHash, "", userName, currentHash)
    cur.execute(sql, val)
    db.commit()
    db.close()
    

# Generate sign from user name and nonce
def genSign(user, nonce):
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "SELECT salt FROM login_table WHERE username = %s"
    val = (user, )
    cur.execute(sql, val)
    salt = str(cur.fetchall()[0][0])
    key = user + salt
    forSign = key + str(nonce)
    db.close()
    return hashlib.sha256(forSign.encode('utf-8')).hexdigest()

# Calculate hash for current block
def calHash(nonce, prevHash, userName, sign, artName, bas64Hash, fromTo, owner):
    nonce = str(nonce)
    content = nonce + prevHash + userName + sign + artName + bas64Hash + fromTo + owner
    hashStr = ""
    allChar = string.ascii_letters + string.digits
    while not hashStr.startswith("000"):
        ans = ''.join(random.choice(allChar) for i in range(64))
        hashStr = hashStr + ans
        hashStr = hashlib.sha256(hashStr.encode('utf-8')).hexdigest()
    return ans

# For testing
if __name__ == "__main__":
    uploadToChain_Own("user", "Fish", "https://i.imgur.com/EjOJYmu.jpeg")