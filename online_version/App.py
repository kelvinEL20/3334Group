import mysql.connector
import hashlib
import requests
import base64
import string
import random
from datetime import datetime
from PIL import Image
from io import BytesIO
from General import *

# Upload artwork details to artwork_table
def uploadToArtworkListTable(artName, artUrl):
    db = mysql.connector.connect(
    host = "database-1.cxdirld1qchg.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "12345678",
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
    host = "database-1.cxdirld1qchg.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "12345678",
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
    
    # Check existing chain
    db = mysql.connector.connect(
    host = "database-1.cxdirld1qchg.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "12345678",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "SELECT * FROM the_chain ORDER BY nonce"
    cur.execute(sql)
    chainContent = cur.fetchall()
    nonce = 1
    for tup in chainContent:
        if nonce > 1 and tup[1] != lastHash:
            showAlert("Error on current chain (Blocks not connected)")
            return
        if not isCurrentHashCorrect(tup):
            showAlert("Invalid hash on block number:" + str(nonce))
            return
        if not isSignCorrect(tup):
            showAlert("Invalid sign on block number:" + str(nonce))
            return
        lastHash = tup[8]
        nonce += 1
    db.close()
    
    db = mysql.connector.connect(
    host = "database-1.cxdirld1qchg.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "12345678",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "INSERT INTO the_chain (previous_hash, user_name, user_sign, art_name, base64_art_hash, tran_from_to, upload_owner, current_hash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (prevHash, userName, sign, artName, artHash, "", userName, currentHash)
    cur.execute(sql, val)
    db.commit()
    db.close()
