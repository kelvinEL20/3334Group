from General import *
import mysql.connector

# Check if the user own the artwork
def checkOwnership(artName, username):
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "SELECT * FROM the_chain"
    cur.execute(sql)
    theChain = cur.fetchall()
    nonce = 1
    lastHash = ""
    currentOwner = ""
    for tup in theChain:
        if nonce > 1 and tup[1] != lastHash:
            showAlert("Error on current chain (Blocks not connected)")
            return
        if not isCurrentHashCorrect(tup):
            showAlert("Invalid hash on block number:" + str(nonce))
            return
        if not isSignCorrect(tup):
            showAlert("Invalid sign on block number:" + str(nonce))
            return
        if str(tup[4]) == artName and str(tup[7]) != "":
            currentOwner = str(tup[7])
        if str(tup[4]) == artName and str(tup[6]) != "":
            currentOwner = str(tup[6])
        lastHash = tup[8]
        nonce += 1
    db.close()
    return currentOwner == username
    
# Return if the username exists
def userExist(username):
    db = mysql.connector.connect(
    host = "localhost",
    user = "kelvin",
    password = "kelvin",
    database = "3334group"
    )
    cur = db.cursor()
    sql = "SELECT * FROM login_table WHERE username = %s"
    val = (username, )
    cur.execute(sql, val)
    output = cur.fetchall()
    db.close()
    return len(output) > 0

# Generate preview of block in string
def generateBlockPreview(fromUser, toUser, artName):
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
    lastHash = ""
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
        if str(tup[4]) == artName:
            base64Art = str(tup[5])
        lastHash = tup[8]
        nonce += 1
    db.close()
    sign = genSign(fromUser, nonce)
    fromTo = toUser
    currentHash = calHash(nonce, lastHash, fromUser, sign, artName, base64Art, fromTo, "")
    outStr = "nonce: " + str(nonce) + "\n\nprevious_hash: " + lastHash + "\n\nuser_name: " + fromUser + "\n\nuser_sign: " + sign + "\n\nart_name: " + artName + "\n\nbase64_art_hash: " + base64Art + "\n\ntran_from_to: " + toUser + "\n\nupload_owner: " + "" + "\n\ncurrent_hash: " + currentHash
    return outStr

def appendToChain():
    return