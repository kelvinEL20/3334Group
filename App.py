from cgi import print_environ_usage
import mysql.connector
import hashlib
import requests
import base64
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
def uploadToChain_Own(user, artName, artUrl):
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
        prevHash = latestBlock[0][1]
        nonce = int(latestBlock[0][0]) + 1
    db.close()
    
# For testing
if __name__ == "__main__":
    uploadToChain_Own("user", "Fish", "https://i.imgur.com/EjOJYmu.jpeg")