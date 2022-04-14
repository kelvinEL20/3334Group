import mysql.connector
import hashlib
from General import *

def getOwnedArtworks(username):
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
        if isCurrentHashCorrect(tup) and tup[2] == username:
            ownedList.append(str(tup[4]))
        lastHash = tup[8]
        nonce += 1
    db.close()
    return "\n".join(ownedList)
