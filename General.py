from PyQt5.QtWidgets  import QMessageBox
import hashlib
import mysql.connector

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
    return tup[3] == hashlib.sha256(forSign.encode('utf-8')).hexdigest()
