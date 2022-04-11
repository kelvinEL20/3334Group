from PyQt5.QtWidgets  import QMessageBox

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
