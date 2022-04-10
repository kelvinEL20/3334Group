from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginPage = QtWidgets.QWidget(self.centralwidget)
        self.LoginPage.setGeometry(QtCore.QRect(0, 0, 1024, 751))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.LoginPage.setFont(font)
        self.LoginPage.setInputMethodHints(QtCore.Qt.ImhNone)
        self.LoginPage.setObjectName("LoginPage")
        self.btnLoginPageLogin = QtWidgets.QPushButton(self.LoginPage)
        self.btnLoginPageLogin.setGeometry(QtCore.QRect(231, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnLoginPageLogin.setFont(font)
        self.btnLoginPageLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLoginPageLogin.setObjectName("btnLoginPageLogin")
        self.btnLoginPageReg = QtWidgets.QPushButton(self.LoginPage)
        self.btnLoginPageReg.setGeometry(QtCore.QRect(550, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnLoginPageReg.setFont(font)
        self.btnLoginPageReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLoginPageReg.setObjectName("btnLoginPageReg")
        self.LoginPageLabel_2 = QtWidgets.QLabel(self.LoginPage)
        self.LoginPageLabel_2.setGeometry(QtCore.QRect(80, 230, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LoginPageLabel_2.setFont(font)
        self.LoginPageLabel_2.setObjectName("LoginPageLabel_2")
        self.LoginPageLabel_3 = QtWidgets.QLabel(self.LoginPage)
        self.LoginPageLabel_3.setGeometry(QtCore.QRect(80, 390, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LoginPageLabel_3.setFont(font)
        self.LoginPageLabel_3.setObjectName("LoginPageLabel_3")
        self.LoginPageLabel_1 = QtWidgets.QLabel(self.LoginPage)
        self.LoginPageLabel_1.setGeometry(QtCore.QRect(390, 80, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LoginPageLabel_1.setFont(font)
        self.LoginPageLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginPageLabel_1.setObjectName("LoginPageLabel_1")
        self.LoginPageUsernameInput = QtWidgets.QLineEdit(self.LoginPage)
        self.LoginPageUsernameInput.setGeometry(QtCore.QRect(242, 240, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LoginPageUsernameInput.setFont(font)
        self.LoginPageUsernameInput.setObjectName("LoginPageUsernameInput")
        self.LoginPagePasswordInput = QtWidgets.QLineEdit(self.LoginPage)
        self.LoginPagePasswordInput.setEnabled(True)
        self.LoginPagePasswordInput.setGeometry(QtCore.QRect(242, 400, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LoginPagePasswordInput.setFont(font)
        self.LoginPagePasswordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.LoginPagePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginPagePasswordInput.setPlaceholderText("")
        self.LoginPagePasswordInput.setClearButtonEnabled(False)
        self.LoginPagePasswordInput.setObjectName("LoginPagePasswordInput")
        self.RegPage = QtWidgets.QWidget(self.centralwidget)
        self.RegPage.setGeometry(QtCore.QRect(0, 0, 1024, 751))
        self.RegPage.setObjectName("RegPage")
        self.btnRegPageBack = QtWidgets.QPushButton(self.RegPage)
        self.btnRegPageBack.setGeometry(QtCore.QRect(548, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnRegPageBack.setFont(font)
        self.btnRegPageBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegPageBack.setObjectName("btnRegPageBack")
        self.RegPageUsernameInput = QtWidgets.QLineEdit(self.RegPage)
        self.RegPageUsernameInput.setGeometry(QtCore.QRect(240, 240, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageUsernameInput.setFont(font)
        self.RegPageUsernameInput.setObjectName("RegPageUsernameInput")
        self.RegPageLabel_2 = QtWidgets.QLabel(self.RegPage)
        self.RegPageLabel_2.setGeometry(QtCore.QRect(80, 230, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageLabel_2.setFont(font)
        self.RegPageLabel_2.setObjectName("RegPageLabel_2")
        self.RegPageLabel_1 = QtWidgets.QLabel(self.RegPage)
        self.RegPageLabel_1.setGeometry(QtCore.QRect(388, 80, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageLabel_1.setFont(font)
        self.RegPageLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.RegPageLabel_1.setObjectName("RegPageLabel_1")
        self.RegPageLabel_4 = QtWidgets.QLabel(self.RegPage)
        self.RegPageLabel_4.setGeometry(QtCore.QRect(80, 390, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageLabel_4.setFont(font)
        self.RegPageLabel_4.setObjectName("RegPageLabel_4")
        self.RegPageConfirmPasswordInput = QtWidgets.QLineEdit(self.RegPage)
        self.RegPageConfirmPasswordInput.setEnabled(True)
        self.RegPageConfirmPasswordInput.setGeometry(QtCore.QRect(240, 400, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageConfirmPasswordInput.setFont(font)
        self.RegPageConfirmPasswordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.RegPageConfirmPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RegPageConfirmPasswordInput.setPlaceholderText("")
        self.RegPageConfirmPasswordInput.setClearButtonEnabled(False)
        self.RegPageConfirmPasswordInput.setObjectName("RegPageConfirmPasswordInput")
        self.btnRegPageReg = QtWidgets.QPushButton(self.RegPage)
        self.btnRegPageReg.setGeometry(QtCore.QRect(229, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnRegPageReg.setFont(font)
        self.btnRegPageReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegPageReg.setObjectName("btnRegPageReg")
        self.RegPageLabel_3 = QtWidgets.QLabel(self.RegPage)
        self.RegPageLabel_3.setGeometry(QtCore.QRect(80, 310, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageLabel_3.setFont(font)
        self.RegPageLabel_3.setObjectName("RegPageLabel_3")
        self.RegPagePasswordInput = QtWidgets.QLineEdit(self.RegPage)
        self.RegPagePasswordInput.setEnabled(True)
        self.RegPagePasswordInput.setGeometry(QtCore.QRect(240, 320, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPagePasswordInput.setFont(font)
        self.RegPagePasswordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.RegPagePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RegPagePasswordInput.setPlaceholderText("")
        self.RegPagePasswordInput.setClearButtonEnabled(False)
        self.RegPagePasswordInput.setObjectName("RegPagePasswordInput")
        self.AppPage = QtWidgets.QWidget(self.centralwidget)
        self.AppPage.setGeometry(QtCore.QRect(0, 0, 1024, 751))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AppPage.setFont(font)
        self.AppPage.setObjectName("AppPage")
        self.AppPageTab = QtWidgets.QTabWidget(self.AppPage)
        self.AppPageTab.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.AppPageTab.setObjectName("AppPageTab")
        self.AppPageGalleryTab = QtWidgets.QWidget()
        self.AppPageGalleryTab.setObjectName("AppPageGalleryTab")
        self.GalleryArtWrokList = QtWidgets.QListView(self.AppPageGalleryTab)
        self.GalleryArtWrokList.setGeometry(QtCore.QRect(20, 70, 441, 541))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.GalleryArtWrokList.setFont(font)
        self.GalleryArtWrokList.setObjectName("GalleryArtWrokList")
        self.GalleryLabel_1 = QtWidgets.QLabel(self.AppPageGalleryTab)
        self.GalleryLabel_1.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.GalleryLabel_1.setObjectName("GalleryLabel_1")
        self.btnGalleryShow = QtWidgets.QPushButton(self.AppPageGalleryTab)
        self.btnGalleryShow.setGeometry(QtCore.QRect(50, 640, 121, 51))
        self.btnGalleryShow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGalleryShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnGalleryShow.setObjectName("btnGalleryShow")
        self.GallerySortTypeComboBox = QtWidgets.QComboBox(self.AppPageGalleryTab)
        self.GallerySortTypeComboBox.setGeometry(QtCore.QRect(340, 640, 91, 51))
        self.GallerySortTypeComboBox.setObjectName("GallerySortTypeComboBox")
        self.GallerySortTypeComboBox.addItem("")
        self.btnGallerySort = QtWidgets.QPushButton(self.AppPageGalleryTab)
        self.btnGallerySort.setGeometry(QtCore.QRect(220, 640, 121, 51))
        self.btnGallerySort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGallerySort.setObjectName("btnGallerySort")
        self.GalleryLine = QtWidgets.QFrame(self.AppPageGalleryTab)
        self.GalleryLine.setGeometry(QtCore.QRect(511, 0, 21, 711))
        self.GalleryLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.GalleryLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GalleryLine.setObjectName("GalleryLine")
        self.GalleryLabel_2 = QtWidgets.QLabel(self.AppPageGalleryTab)
        self.GalleryLabel_2.setGeometry(QtCore.QRect(550, 20, 171, 31))
        self.GalleryLabel_2.setObjectName("GalleryLabel_2")
        self.GalleryArtworkLabel = QtWidgets.QLabel(self.AppPageGalleryTab)
        self.GalleryArtworkLabel.setGeometry(QtCore.QRect(550, 130, 451, 451))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.GalleryArtworkLabel.setFont(font)
        self.GalleryArtworkLabel.setTextFormat(QtCore.Qt.PlainText)
        self.GalleryArtworkLabel.setScaledContents(True)
        self.GalleryArtworkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GalleryArtworkLabel.setObjectName("GalleryArtworkLabel")
        self.AppPageTab.addTab(self.AppPageGalleryTab, "")
        self.AppPageExchangeTab = QtWidgets.QWidget()
        self.AppPageExchangeTab.setObjectName("AppPageExchangeTab")
        self.ExchangeLabel_1 = QtWidgets.QLabel(self.AppPageExchangeTab)
        self.ExchangeLabel_1.setGeometry(QtCore.QRect(50, 50, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExchangeLabel_1.setFont(font)
        self.ExchangeLabel_1.setObjectName("ExchangeLabel_1")
        self.ExchangeFileNameInput = QtWidgets.QLineEdit(self.AppPageExchangeTab)
        self.ExchangeFileNameInput.setGeometry(QtCore.QRect(50, 130, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExchangeFileNameInput.setFont(font)
        self.ExchangeFileNameInput.setObjectName("ExchangeFileNameInput")
        self.ExchangeLabel_2 = QtWidgets.QLabel(self.AppPageExchangeTab)
        self.ExchangeLabel_2.setGeometry(QtCore.QRect(50, 200, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExchangeLabel_2.setFont(font)
        self.ExchangeLabel_2.setObjectName("ExchangeLabel_2")
        self.ExchangeUsernameInput = QtWidgets.QLineEdit(self.AppPageExchangeTab)
        self.ExchangeUsernameInput.setGeometry(QtCore.QRect(50, 280, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExchangeUsernameInput.setFont(font)
        self.ExchangeUsernameInput.setObjectName("ExchangeUsernameInput")
        self.ExchangeConfirmUsernameInput = QtWidgets.QLineEdit(self.AppPageExchangeTab)
        self.ExchangeConfirmUsernameInput.setGeometry(QtCore.QRect(50, 350, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExchangeConfirmUsernameInput.setFont(font)
        self.ExchangeConfirmUsernameInput.setObjectName("ExchangeConfirmUsernameInput")
        self.btnExchangeConstructBlock = QtWidgets.QPushButton(self.AppPageExchangeTab)
        self.btnExchangeConstructBlock.setGeometry(QtCore.QRect(120, 440, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnExchangeConstructBlock.setFont(font)
        self.btnExchangeConstructBlock.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExchangeConstructBlock.setObjectName("btnExchangeConstructBlock")
        self.btnExchangeAppendToChain = QtWidgets.QPushButton(self.AppPageExchangeTab)
        self.btnExchangeAppendToChain.setEnabled(False)
        self.btnExchangeAppendToChain.setGeometry(QtCore.QRect(120, 550, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnExchangeAppendToChain.setFont(font)
        self.btnExchangeAppendToChain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExchangeAppendToChain.setObjectName("btnExchangeAppendToChain")
        self.ExchangeLabel_3 = QtWidgets.QLabel(self.AppPageExchangeTab)
        self.ExchangeLabel_3.setGeometry(QtCore.QRect(550, 50, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ExchangeLabel_3.setFont(font)
        self.ExchangeLabel_3.setObjectName("ExchangeLabel_3")
        self.ExchangeLine = QtWidgets.QFrame(self.AppPageExchangeTab)
        self.ExchangeLine.setGeometry(QtCore.QRect(511, 0, 21, 711))
        self.ExchangeLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.ExchangeLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ExchangeLine.setObjectName("ExchangeLine")
        self.ExchangePreviewBlockOutputTextArea = QtWidgets.QTextBrowser(self.AppPageExchangeTab)
        self.ExchangePreviewBlockOutputTextArea.setGeometry(QtCore.QRect(550, 120, 441, 571))
        self.ExchangePreviewBlockOutputTextArea.setObjectName("ExchangePreviewBlockOutputTextArea")
        self.AppPageTab.addTab(self.AppPageExchangeTab, "")
        self.AppPage.raise_()
        self.RegPage.raise_()
        self.LoginPage.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.AppPageTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Connect the buttons with functions
        self.btnLoginPageLogin.clicked.connect(self.loginClicked)
        self.btnLoginPageReg.clicked.connect(self.loginPageRegClicked)
        
        self.btnRegPageReg.clicked.connect(self.regPageRegClicked)
        self.btnRegPageBack.clicked.connect(self.regPageBackClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoginPageLogin.setText(_translate("MainWindow", "Login"))
        self.btnLoginPageReg.setText(_translate("MainWindow", "Register"))
        self.LoginPageLabel_2.setText(_translate("MainWindow", "Username:"))
        self.LoginPageLabel_3.setText(_translate("MainWindow", "Password:"))
        self.LoginPageLabel_1.setText(_translate("MainWindow", "Login Page"))
        self.btnRegPageBack.setText(_translate("MainWindow", "Back"))
        self.RegPageLabel_2.setText(_translate("MainWindow", "Username:"))
        self.RegPageLabel_1.setText(_translate("MainWindow", "Register"))
        self.RegPageLabel_4.setText(_translate("MainWindow", "Confirm:"))
        self.btnRegPageReg.setText(_translate("MainWindow", "Register"))
        self.RegPageLabel_3.setText(_translate("MainWindow", "Password:"))
        self.GalleryLabel_1.setText(_translate("MainWindow", "List of Artworks:"))
        self.btnGalleryShow.setText(_translate("MainWindow", "Show"))
        self.GallerySortTypeComboBox.setItemText(0, _translate("MainWindow", "Name"))
        self.btnGallerySort.setText(_translate("MainWindow", "Sort by:"))
        self.GalleryLabel_2.setText(_translate("MainWindow", "Display Area (Scaled):"))
        self.GalleryArtworkLabel.setText(_translate("MainWindow", "The selected artwork will be displayed here"))
        self.AppPageTab.setTabText(self.AppPageTab.indexOf(self.AppPageGalleryTab), _translate("MainWindow", "Gallery"))
        self.ExchangeLabel_1.setText(_translate("MainWindow", "Transfer ownership of"))
        self.ExchangeFileNameInput.setPlaceholderText(_translate("MainWindow", "Artwork file name"))
        self.ExchangeLabel_2.setText(_translate("MainWindow", "to"))
        self.ExchangeUsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.ExchangeConfirmUsernameInput.setPlaceholderText(_translate("MainWindow", "Confirm Username"))
        self.btnExchangeConstructBlock.setText(_translate("MainWindow", "Construct block"))
        self.btnExchangeAppendToChain.setText(_translate("MainWindow", "Append to chain"))
        self.ExchangeLabel_3.setText(_translate("MainWindow", "Preview block:"))
        self.AppPageTab.setTabText(self.AppPageTab.indexOf(self.AppPageExchangeTab), _translate("MainWindow", "Exchange"))

        self.AppPage.setVisible(False)
        self.RegPage.setVisible(False)
    
    # Functions    
    def loginClicked(self):
        return
    
    def loginPageRegClicked(self):
        self.clearAll()
        self.AppPage.setVisible(False)
        self.LoginPage.setVisible(False)
        self.RegPage.setVisible(True)
    
    def regPageRegClicked(self):
        return

    def regPageBackClicked(self):
        self.clearAll()
        self.AppPage.setVisible(False)
        self.RegPage.setVisible(False)
        self.LoginPage.setVisible(True)
        
    # Clear all input and output area
    def clearAll(self):
        self.LoginPagePasswordInput.setText("")
        self.LoginPageUsernameInput.setText("")
        self.RegPageUsernameInput.setText("")
        self.RegPagePasswordInput.setText("")
        self.RegPageConfirmPasswordInput.setText("")
        self.GalleryArtworkLabel.clear()
        self.ExchangeFileNameInput.setText("")
        self.ExchangeUsernameInput.setText("")
        self.ExchangeConfirmUsernameInput.setText("")
        self.ExchangePreviewBlockOutputTextArea.setText("")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())