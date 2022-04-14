from PyQt5.QtWidgets  import QMessageBox
import hashlib

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
