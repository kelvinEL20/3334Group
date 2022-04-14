from email import header
import mysql.connector
import hashlib
import csv
import os
from datetime import datetime
from General import *

def getOwnedArtworks(username):
    ownDict = {}
    ownedList = []
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
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
        if not isSignCorrect(tup):
            showAlert("Invalid sign on block number:" + str(nonce))
            return
        if not isCurrentHashCorrect(tup):
            showAlert("Invalid hash on block:" + str(nonce))
            return
        if tup[7] != "": # upload own
            ownDict[tup[4]] = tup[7]
        if tup[6] != "": # exchange
            ownDict[tup[4]] = tup[6]
        lastHash = tup[8]
        nonce += 1
    db.close()
    for key in ownDict:
        if ownDict[key] == username:
            ownedList.append(key)
    return "\n".join(ownedList)

def downloadChain():
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "SELECT * FROM the_chain ORDER BY nonce"
    cur.execute(sql)
    chainContent = cur.fetchall()
    now = datetime.now()
    if not os.path.exists("Records"):
        os.makedirs("Records")
    fileName = "Records/" + now.strftime("%d%m%Y_%H%M%S") + "_Chain.csv"
    header = ["nonce", "previous_hash", "user_name", "user_sign", "art_name", "base64_art_hash", "tran_from_to", "upload_owner", "current_hash"]
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(chainContent)
    db.close()
