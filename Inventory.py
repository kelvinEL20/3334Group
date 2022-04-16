from turtle import update
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

def checkUploadedFile(path):
    file = open(path)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    lastHash = ""
    index = 1
    rows = []
    for row in csvreader:
        if not isSignCorrect(row):
            return ""
        if not isCurrentHashCorrect(row):
            return ""
        if row[0] != '1' and row[1] != lastHash:
            return ""
        rows.append(row)
        lastHash = row[8]
        index += 1
    return rows

def updateChain(rows):
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
    db.close()
    rowsLen = len(rows)
    
    # Remove column 0 as it will be auto filled by database
    for row in rows:
        row.pop(0)
    
    # Convert list of list to list of tuple
    listOfTup = []
    for row in rows:
        listOfTup.append(tuple(row))
    
    if len(latestBlock) == 0: # Empty at chain in database
        db = mysql.connector.connect(
        host = "localhost",
        user = "kelvin",
        password = "kelvin",
        database = "3334group"
        )
        cur = db.cursor()
        sql = "INSERT INTO the_chain (previous_hash, user_name, user_sign, art_name, base64_art_hash, tran_from_to, upload_owner, current_hash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = listOfTup
        cur.executemany(sql, val)
        db.commit()
        db.close()
    elif rowsLen > int(latestBlock[0][0]): # Uploaed chain is longer than old one
        # Delete old chain
        db = mysql.connector.connect(
        host = "localhost",
        user = "kelvin",
        password = "kelvin",
        database = "3334group"
        )
        cur = db.cursor()
        sql = "DROP TABLE IF EXISTS the_chain"
        cur.execute(sql)
        db.commit()
        db.close()
        
        # Create new table the_chain
        db = mysql.connector.connect(
        host = "localhost",
        user = "kelvin",
        password = "kelvin",
        database = "3334group"
        )
        cur = db.cursor()
        sql = "CREATE TABLE the_chain ( nonce INT AUTO_INCREMENT PRIMARY KEY, previous_hash varchar(64), user_name varchar(20), user_sign varchar(64), art_name varchar(20), base64_art_hash varchar(64), tran_from_to varchar(100) DEFAULT '', upload_owner varchar(75) DEFAULT '', current_hash varchar(64) )"
        cur.execute(sql)
        db.commit()
        db.close()
        
        # Create new chian
        db = mysql.connector.connect(
        host = "localhost",
        user = "kelvin",
        password = "kelvin",
        database = "3334group"
        )
        cur = db.cursor()
        sql = "INSERT INTO the_chain (previous_hash, user_name, user_sign, art_name, base64_art_hash, tran_from_to, upload_owner, current_hash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = listOfTup
        cur.executemany(sql, val)
        db.commit()
        db.close() 
    else:
        return "Uploaded chain is not longer than the old one, upload aborted"
    return "Chain updated"
