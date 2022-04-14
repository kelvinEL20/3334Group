from PyQt5.QtWidgets  import QMessageBox
import hashlib
import mysql.connector
import string
import random

def showAlert(msg):
    alert = QMessageBox()
    alert.setIcon(QMessageBox.Critical)
    alert.setText(str(msg))
    alert.setWindowTitle("Error")
    alert.exec_()

def showInfo(msg):
    info = QMessageBox()
    info.setIcon(QMessageBox.Information)
    info.setText(str(msg))
    info.setWindowTitle("Information")
    info.exec_()

# Verify hash of current block
def isCurrentHashCorrect(tup):
    strForCheck = ""
    for i in range(9):
        strForCheck += str(tup[i])
    hashOut = hashlib.sha256(strForCheck.encode('utf-8')).hexdigest()
    return hashOut.startswith("000")

# Check if signature of current block correct
def isSignCorrect(tup):
    nonce = str(tup[0])
    user = tup[2]
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
    forSign = key + nonce
    db.close()
    return tup[3] == hashlib.sha256(forSign.encode('utf-8')).hexdigest()

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
    hashStr = content
    allChar = string.ascii_letters + string.digits
    while not hashStr.startswith("000"):
        ans = ''.join(random.choice(allChar) for i in range(64))
        hashStr = content + ans
        hashStr = hashlib.sha256(hashStr.encode('utf-8')).hexdigest()
    return ans
