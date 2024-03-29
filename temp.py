from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import mysql.connector
import requests
from Login import *
from Reg import *
from App import *
from General import *
from Inventory import *
from Exchange import *

class Ui_MainWindow(object):
    currentUser = ""
    artDict = {}
    artList = []
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
        self.RegPageLabel_3 = QtWidgets.QLabel(self.RegPage)
        self.RegPageLabel_3.setGeometry(QtCore.QRect(80, 310, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageLabel_3.setFont(font)
        self.RegPageLabel_3.setObjectName("RegPageLabel_3")
        self.RegPageUsernameInput = QtWidgets.QLineEdit(self.RegPage)
        self.RegPageUsernameInput.setGeometry(QtCore.QRect(240, 240, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageUsernameInput.setFont(font)
        self.RegPageUsernameInput.setObjectName("RegPageUsernameInput")
        self.RegPagePasswordInput = QtWidgets.QLineEdit(self.RegPage)
        self.RegPagePasswordInput.setGeometry(QtCore.QRect(240, 320, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPagePasswordInput.setFont(font)
        self.RegPagePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RegPagePasswordInput.setObjectName("RegPagePasswordInput")
        self.RegPageConfirmPasswordInput = QtWidgets.QLineEdit(self.RegPage)
        self.RegPageConfirmPasswordInput.setGeometry(QtCore.QRect(240, 400, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RegPageConfirmPasswordInput.setFont(font)
        self.RegPageConfirmPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RegPageConfirmPasswordInput.setObjectName("RegPageConfirmPasswordInput")
        self.btnRegPageReg = QtWidgets.QPushButton(self.RegPage)
        self.btnRegPageReg.setGeometry(QtCore.QRect(229, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnRegPageReg.setFont(font)
        self.btnRegPageReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegPageReg.setObjectName("btnRegPageReg")
        self.btnRegPageBack = QtWidgets.QPushButton(self.RegPage)
        self.btnRegPageBack.setGeometry(QtCore.QRect(548, 530, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnRegPageBack.setFont(font)
        self.btnRegPageBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegPageBack.setObjectName("btnRegPageBack")
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
        self.GalleryLabel_1 = QtWidgets.QLabel(self.AppPageGalleryTab)
        self.GalleryLabel_1.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.GalleryLabel_1.setObjectName("GalleryLabel_1")
        self.btnGalleryShow = QtWidgets.QPushButton(self.AppPageGalleryTab)
        self.btnGalleryShow.setGeometry(QtCore.QRect(50, 640, 121, 51))
        self.btnGalleryShow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGalleryShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnGalleryShow.setObjectName("btnGalleryShow")
        self.GallerySortTypeComboBox = QtWidgets.QComboBox(self.AppPageGalleryTab)
        self.GallerySortTypeComboBox.setGeometry(QtCore.QRect(340, 640, 131, 51))
        self.GallerySortTypeComboBox.setObjectName("GallerySortTypeComboBox")
        self.GallerySortTypeComboBox.addItem("")
        self.GallerySortTypeComboBox.addItem("")
        self.btnGallerySort = QtWidgets.QPushButton(self.AppPageGalleryTab)
        self.btnGallerySort.setGeometry(QtCore.QRect(220, 640, 121, 51))
        self.btnGallerySort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGallerySort.setObjectName("btnGallerySort")
        self.GalleryLine = QtWidgets.QFrame(self.AppPageGalleryTab)
        self.GalleryLine.setGeometry(QtCore.QRect(511, 0, 21, 601))
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
        self.GalleryArtWrokList = QtWidgets.QListWidget(self.AppPageGalleryTab)
        self.GalleryArtWrokList.setGeometry(QtCore.QRect(20, 70, 441, 541))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.GalleryArtWrokList.setFont(font)
        self.GalleryArtWrokList.setObjectName("GalleryArtWrokList")
        self.btnLogout = QtWidgets.QPushButton(self.AppPageGalleryTab)
        self.btnLogout.setGeometry(QtCore.QRect(680, 630, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnLogout.setFont(font)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setObjectName("btnLogout")
        self.GalleryLine_2 = QtWidgets.QFrame(self.AppPageGalleryTab)
        self.GalleryLine_2.setGeometry(QtCore.QRect(520, 590, 501, 21))
        self.GalleryLine_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.GalleryLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GalleryLine_2.setObjectName("GalleryLine_2")
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
        self.btnExchangeClear = QtWidgets.QPushButton(self.AppPageExchangeTab)
        self.btnExchangeClear.setGeometry(QtCore.QRect(370, 650, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnExchangeClear.setFont(font)
        self.btnExchangeClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExchangeClear.setObjectName("btnExchangeClear")
        self.AppPageTab.addTab(self.AppPageExchangeTab, "")
        self.AppPageUploadTab = QtWidgets.QWidget()
        self.AppPageUploadTab.setObjectName("AppPageUploadTab")
        self.UploadLabel_1 = QtWidgets.QLabel(self.AppPageUploadTab)
        self.UploadLabel_1.setGeometry(QtCore.QRect(0, 40, 1011, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.UploadLabel_1.setFont(font)
        self.UploadLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.UploadLabel_1.setObjectName("UploadLabel_1")
        self.UploadLabel_2 = QtWidgets.QLabel(self.AppPageUploadTab)
        self.UploadLabel_2.setGeometry(QtCore.QRect(20, 130, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.UploadLabel_2.setFont(font)
        self.UploadLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UploadLabel_2.setObjectName("UploadLabel_2")
        self.UploadLine = QtWidgets.QFrame(self.AppPageUploadTab)
        self.UploadLine.setGeometry(QtCore.QRect(0, 90, 1021, 21))
        self.UploadLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.UploadLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.UploadLine.setObjectName("UploadLine")
        self.UploadLabel_3 = QtWidgets.QLabel(self.AppPageUploadTab)
        self.UploadLabel_3.setGeometry(QtCore.QRect(20, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.UploadLabel_3.setFont(font)
        self.UploadLabel_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UploadLabel_3.setObjectName("UploadLabel_3")
        self.UploadArtworkPreviewLabel = QtWidgets.QLabel(self.AppPageUploadTab)
        self.UploadArtworkPreviewLabel.setGeometry(QtCore.QRect(480, 250, 451, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UploadArtworkPreviewLabel.setFont(font)
        self.UploadArtworkPreviewLabel.setTextFormat(QtCore.Qt.PlainText)
        self.UploadArtworkPreviewLabel.setScaledContents(True)
        self.UploadArtworkPreviewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UploadArtworkPreviewLabel.setObjectName("UploadArtworkPreviewLabel")
        self.UploadArtworkNameInput = QtWidgets.QLineEdit(self.AppPageUploadTab)
        self.UploadArtworkNameInput.setGeometry(QtCore.QRect(240, 130, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.UploadArtworkNameInput.setFont(font)
        self.UploadArtworkNameInput.setObjectName("UploadArtworkNameInput")
        self.UploadArtworkUrlInput = QtWidgets.QLineEdit(self.AppPageUploadTab)
        self.UploadArtworkUrlInput.setGeometry(QtCore.QRect(240, 200, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.UploadArtworkUrlInput.setFont(font)
        self.UploadArtworkUrlInput.setObjectName("UploadArtworkUrlInput")
        self.btnUploadPreview = QtWidgets.QPushButton(self.AppPageUploadTab)
        self.btnUploadPreview.setGeometry(QtCore.QRect(110, 360, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnUploadPreview.setFont(font)
        self.btnUploadPreview.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUploadPreview.setObjectName("btnUploadPreview")
        self.btnUploadUpload = QtWidgets.QPushButton(self.AppPageUploadTab)
        self.btnUploadUpload.setEnabled(False)
        self.btnUploadUpload.setGeometry(QtCore.QRect(110, 490, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnUploadUpload.setFont(font)
        self.btnUploadUpload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUploadUpload.setObjectName("btnUploadUpload")
        self.btnUploadClear = QtWidgets.QPushButton(self.AppPageUploadTab)
        self.btnUploadClear.setEnabled(True)
        self.btnUploadClear.setGeometry(QtCore.QRect(110, 620, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnUploadClear.setFont(font)
        self.btnUploadClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUploadClear.setObjectName("btnUploadClear")
        self.AppPageTab.addTab(self.AppPageUploadTab, "")
        self.AppPageInventoryTab = QtWidgets.QWidget()
        self.AppPageInventoryTab.setObjectName("AppPageInventoryTab")
        self.InventoryLabel_1 = QtWidgets.QLabel(self.AppPageInventoryTab)
        self.InventoryLabel_1.setGeometry(QtCore.QRect(70, 170, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.InventoryLabel_1.setFont(font)
        self.InventoryLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.InventoryLabel_1.setObjectName("InventoryLabel_1")
        self.InventoryTextOutput = QtWidgets.QTextBrowser(self.AppPageInventoryTab)
        self.InventoryTextOutput.setGeometry(QtCore.QRect(360, 30, 621, 651))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.InventoryTextOutput.setFont(font)
        self.InventoryTextOutput.setObjectName("InventoryTextOutput")
        self.btnInventoryUpdate = QtWidgets.QPushButton(self.AppPageInventoryTab)
        self.btnInventoryUpdate.setGeometry(QtCore.QRect(110, 310, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnInventoryUpdate.setFont(font)
        self.btnInventoryUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInventoryUpdate.setObjectName("btnInventoryUpdate")
        self.btnInventoryDownload = QtWidgets.QPushButton(self.AppPageInventoryTab)
        self.btnInventoryDownload.setGeometry(QtCore.QRect(50, 470, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnInventoryDownload.setFont(font)
        self.btnInventoryDownload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInventoryDownload.setObjectName("btnInventoryDownload")
        self.btnInventoryUpload = QtWidgets.QPushButton(self.AppPageInventoryTab)
        self.btnInventoryUpload.setGeometry(QtCore.QRect(50, 590, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnInventoryUpload.setFont(font)
        self.btnInventoryUpload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInventoryUpload.setObjectName("btnInventoryUpload")
        self.AppPageTab.addTab(self.AppPageInventoryTab, "")
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
        
        self.btnGalleryShow.clicked.connect(self.galleryShowClicked)
        self.btnGallerySort.clicked.connect(self.gallerySortClicked)
        self.btnLogout.clicked.connect(self.logoutClicked)
        
        self.btnUploadPreview.clicked.connect(self.uploadPreviewClicked)
        self.btnUploadClear.clicked.connect(self.uploadClearClicked)
        self.btnUploadUpload.clicked.connect(self.uploadUploadClicked)
        
        self.btnInventoryUpdate.clicked.connect(self.inventoryUpdateClicked)
        self.btnInventoryDownload.clicked.connect(self.inventoryDownloadClicked)

        self.btnExchangeClear.clicked.connect(self.exchangeClearClicked)
        self.btnExchangeConstructBlock.clicked.connect(self.exchangeConstructClicked)
        self.btnExchangeAppendToChain.clicked.connect(self.exchangeAppendClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoginPageLogin.setText(_translate("MainWindow", "Login"))
        self.btnLoginPageReg.setText(_translate("MainWindow", "Register"))
        self.LoginPageLabel_2.setText(_translate("MainWindow", "Username:"))
        self.LoginPageLabel_3.setText(_translate("MainWindow", "Password:"))
        self.LoginPageLabel_1.setText(_translate("MainWindow", "Login Page"))
        self.RegPageLabel_2.setText(_translate("MainWindow", "Username:"))
        self.RegPageLabel_1.setText(_translate("MainWindow", "Register"))
        self.RegPageLabel_4.setText(_translate("MainWindow", "Confirm:"))
        self.RegPageLabel_3.setText(_translate("MainWindow", "Password:"))
        self.btnRegPageReg.setText(_translate("MainWindow", "Register"))
        self.btnRegPageBack.setText(_translate("MainWindow", "Back"))
        self.GalleryLabel_1.setText(_translate("MainWindow", "List of Artworks:"))
        self.btnGalleryShow.setText(_translate("MainWindow", "Show"))
        self.GallerySortTypeComboBox.setItemText(0, _translate("MainWindow", "Name"))
        self.GallerySortTypeComboBox.setItemText(1, _translate("MainWindow", "New"))
        self.btnGallerySort.setText(_translate("MainWindow", "Sort by"))
        self.GalleryLabel_2.setText(_translate("MainWindow", "Display Area (Scaled):"))
        self.GalleryArtworkLabel.setText(_translate("MainWindow", "The selected artwork will be displayed here"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))
        self.AppPageTab.setTabText(self.AppPageTab.indexOf(self.AppPageGalleryTab), _translate("MainWindow", "Gallery"))
        self.ExchangeLabel_1.setText(_translate("MainWindow", "Transfer ownership of"))
        self.ExchangeFileNameInput.setPlaceholderText(_translate("MainWindow", "Artwork name"))
        self.ExchangeLabel_2.setText(_translate("MainWindow", "to"))
        self.ExchangeUsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.ExchangeConfirmUsernameInput.setPlaceholderText(_translate("MainWindow", "Confirm Username"))
        self.btnExchangeConstructBlock.setText(_translate("MainWindow", "Construct block"))
        self.btnExchangeAppendToChain.setText(_translate("MainWindow", "Append to chain"))
        self.ExchangeLabel_3.setText(_translate("MainWindow", "Preview block:"))
        self.btnExchangeClear.setText(_translate("MainWindow", "Clear"))
        self.AppPageTab.setTabText(self.AppPageTab.indexOf(self.AppPageExchangeTab), _translate("MainWindow", "Exchange"))
        self.UploadLabel_1.setText(_translate("MainWindow", "Upload your artwork here"))
        self.UploadLabel_2.setText(_translate("MainWindow", "Name of Artwork:"))
        self.UploadLabel_3.setText(_translate("MainWindow", "URL of Artwork:"))
        self.UploadArtworkPreviewLabel.setText(_translate("MainWindow", "The selected artwork will be displayed here (scaled)"))
        self.UploadArtworkNameInput.setPlaceholderText(_translate("MainWindow", "At most 50 characters"))
        self.UploadArtworkUrlInput.setPlaceholderText(_translate("MainWindow", "Supports .jpg, .jpeg and .png (imgur.com is suggested)"))
        self.btnUploadPreview.setText(_translate("MainWindow", "Preview"))
        self.btnUploadUpload.setText(_translate("MainWindow", "Upload"))
        self.btnUploadClear.setText(_translate("MainWindow", "Clear"))
        self.AppPageTab.setTabText(self.AppPageTab.indexOf(self.AppPageUploadTab), _translate("MainWindow", "Upload"))
        self.InventoryLabel_1.setText(_translate("MainWindow", "My artworks:"))
        self.InventoryTextOutput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnInventoryUpdate.setText(_translate("MainWindow", "Update"))
        self.btnInventoryDownload.setText(_translate("MainWindow", "Download Chain"))
        self.btnInventoryUpload.setText(_translate("MainWindow", "Upload Chain"))
        self.AppPageTab.setTabText(self.AppPageTab.indexOf(self.AppPageInventoryTab), _translate("MainWindow", "Inventory"))
        
        self.AppPage.setVisible(False)
        self.RegPage.setVisible(False)
        
    # Functions    
    def loginClicked(self):
        username = self.LoginPageUsernameInput.text()
        password = self.LoginPagePasswordInput.text()
        if username == "" or password == "":
            showAlert("Columns cannot be empty")
        elif len(username) > 20:
            showAlert("Max length for username is 20")
        else:
            if checkLogin(username, password):
                self.currentUser = username
                self.LoginPage.setVisible(False)
                self.RegPage.setVisible(False)
                self.loadArtworkList()
                self.AppPage.setVisible(True)
                self.InventoryLabel_1.setText(self.currentUser + "'s artworks:")
            else:
                showAlert("Username or password incorrect")
            
    def loginPageRegClicked(self):
        self.clearAll()
        self.AppPage.setVisible(False)
        self.LoginPage.setVisible(False)
        self.RegPage.setVisible(True)
    
    def regPageRegClicked(self):
        username = self.RegPageUsernameInput.text()
        password = self.RegPagePasswordInput.text()
        confirmPassword = self.RegPageConfirmPasswordInput.text()
        if username == "" or password == "" or confirmPassword == "":
            showAlert("Columns cannot be empty")
        elif len(username) > 20:
            showAlert("Max length for username is 20")
        elif password != confirmPassword:
            showAlert("Confirm password does not match")
        elif len(password) < 8:
            showAlert("Password must be at least 8 in length")
        elif username == password:
            showAlert("Password must be different from username")
        elif username.upper() == "NULL" or password.upper() == "NULL":
            showAlert("Columns cannot be \"NULL\"")
        elif " " in username:
            showAlert("Please don't use space characters in the name")
        else:
            if register(username, password):
                self.clearAll()
                self.AppPage.setVisible(False)
                self.RegPage.setVisible(False)
                self.LoginPage.setVisible(True)
                showInfo("Successfully registered")

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
        self.GalleryArtWrokList.clear()
        self.GalleryArtworkLabel.setText("The selected artwork will be displayed here")
        self.GallerySortTypeComboBox.setCurrentText("Name")
        self.ExchangeFileNameInput.setText("")
        self.ExchangeUsernameInput.setText("")
        self.ExchangeConfirmUsernameInput.setText("")
        self.ExchangePreviewBlockOutputTextArea.setText("")
        self.btnExchangeConstructBlock.setEnabled(True)
        self.btnExchangeAppendToChain.setEnabled(False)
        self.UploadArtworkNameInput.setText("")
        self.UploadArtworkUrlInput.setText("")
        self.btnUploadPreview.setEnabled(True)
        self.btnUploadUpload.setEnabled(False)
        self.UploadArtworkPreviewLabel.setText("The selected artwork will be displayed here (scaled)")
        self.InventoryTextOutput.setText("")
    
    def logoutClicked(self):
        self.currentUser = ""
        self.clearAll()
        self.AppPage.setVisible(False)
        self.RegPage.setVisible(False)
        self.LoginPage.setVisible(True)
    
    # Load list of artworks
    def loadArtworkList(self):
        db = mysql.connector.connect(
        host = "localhost",
        user = "kelvin",
        password = "kelvin",
        database = "3334group"
        )
        cur = db.cursor()
        sql = "SELECT * FROM artwork_table"
        cur.execute(sql)
        allArtworks = cur.fetchall()
        self.artDict.clear()
        self.artList.clear()
        for tup in allArtworks:
            artName = tup[1]
            artUrl = tup[3]
            self.artDict[artName] = artUrl
        for key in self.artDict:
            self.artList.append(key)
        self.GalleryArtWrokList.addItems(self.artList)
        db.close()
    
    # Show button in gallery clicked
    def galleryShowClicked(self):
        selectedRow = self.GalleryArtWrokList.currentRow()
        selectedArt = self.artList[selectedRow]
        if selectedArt in self.artDict:
            url = self.artDict[selectedArt]
        else:
            showAlert("Image lost")
        image = QImage()
        try:
            image.loadFromData(requests.get(url).content)
            self.GalleryArtworkLabel.setPixmap(QPixmap(image))
        except:
            showAlert("Url is broken, failed to load image")
        
    # Sort button in gallery clicked
    def gallerySortClicked(self):
        db = mysql.connector.connect(
        host = "localhost",
        user = "kelvin",
        password = "kelvin",
        database = "3334group"
        )
        cur = db.cursor()
        if self.GallerySortTypeComboBox.currentText() == "New":
            sql = "SELECT * FROM artwork_table ORDER BY upload_datetime DESC"
        elif self.GallerySortTypeComboBox.currentText() == "Name":
            sql = "SELECT * FROM artwork_table ORDER BY artwork_name"
        cur.execute(sql)
        allArtworks = cur.fetchall()
        self.artDict.clear()
        self.artList.clear()
        for tup in allArtworks:
            artName = tup[1]
            artUrl = tup[3]
            self.artDict[artName] = artUrl
        for key in self.artDict:
            self.artList.append(key)
        self.GalleryArtWrokList.clear()
        self.GalleryArtWrokList.addItems(self.artList)
        db.close()
    
    def uploadPreviewClicked(self):
        artworkName = self.UploadArtworkNameInput.text()
        artworkUrl = self.UploadArtworkUrlInput.text()
        if artworkName == "" or artworkUrl == "":
            showAlert("Columns cannot be empty")
        elif len(artworkName) > 50:
            showAlert("Name should not exist 50 characters")
        elif not (artworkUrl.endswith(".jpg") or artworkUrl.endswith(".jpeg") or artworkUrl.endswith(".png")):
            showAlert("Please upload supported file types only")
        elif " " in artworkName or " " in artworkUrl:
            showAlert("Please do not use space characters in the name or url")
        else: # Check if name or url alreadt exists in database
            db = mysql.connector.connect(
            host = "localhost",
            user = "kelvin",
            password = "kelvin",
            database = "3334group"
            )
            cur = db.cursor()
            sql = "SELECT * FROM artwork_table"
            cur.execute(sql)
            allArtworks = cur.fetchall()
            nameList = []
            urlList = []
            for tup in allArtworks:
                nameList.append(tup[1])
                urlList.append(tup[3])
            if artworkName in nameList or artworkUrl in urlList:
                showAlert("Artwork already exsit in database")
            else: # Show in Preview label
                image = QImage()
                try:
                    image.loadFromData(requests.get(artworkUrl).content)
                    self.UploadArtworkPreviewLabel.setPixmap(QPixmap(image))
                    self.btnUploadPreview.setEnabled(False)
                    self.btnUploadUpload.setEnabled(True)
                    self.UploadArtworkNameInput.setEnabled(False)
                    self.UploadArtworkUrlInput.setEnabled(False)
                except:
                    showAlert("Failed to get image from url")
            db.close()
    
    def uploadClearClicked(self):
        self.UploadArtworkNameInput.setText("")
        self.UploadArtworkUrlInput.setText("")
        self.btnUploadPreview.setEnabled(True)
        self.btnUploadUpload.setEnabled(False)
        self.UploadArtworkNameInput.setEnabled(True)
        self.UploadArtworkUrlInput.setEnabled(True)
        self.UploadArtworkPreviewLabel.setText("The selected artwork will be displayed here (scaled)")
        
    def uploadUploadClicked(self):
        artworkName = self.UploadArtworkNameInput.text()
        artworkUrl = self.UploadArtworkUrlInput.text()
        toListSuccess = False
        try:
            uploadToArtworkListTable(artworkName, artworkUrl)
            toListSuccess = True
        except:
            showAlert("Error when uploading to artwork list")
        if toListSuccess:
            try: 
                showInfo("Click ok to start genereating hash, this will take a moment")
                uploadToChain_Own(self.currentUser, artworkName, artworkUrl)
            except:
                showAlert("Error when uploading to chain")
        self.uploadClearClicked()
        self.GalleryArtWrokList.clear()
        self.loadArtworkList()
        showInfo("Artwork uploaded")
    
    def inventoryUpdateClicked(self):
        self.InventoryTextOutput.setText(getOwnedArtworks(self.currentUser))
        
    def inventoryDownloadClicked(self):
        try:
            downloadChain()
            showInfo("Download succeed")
        except:
            showAlert("Failed to download from chain")
            
    def exchangeClearClicked(self):
        self.ExchangeFileNameInput.setText("")
        self.ExchangeUsernameInput.setText("")
        self.ExchangeConfirmUsernameInput.setText("")
        self.btnExchangeConstructBlock.setEnabled(True)
        self.btnExchangeAppendToChain.setEnabled(False)
        self.ExchangePreviewBlockOutputTextArea.setText("")
        self.ExchangeFileNameInput.setEnabled(True)
        self.ExchangeUsernameInput.setEnabled(True)
        self.ExchangeConfirmUsernameInput.setEnabled(True)
        
    def exchangeConstructClicked(self):
        artName = self.ExchangeFileNameInput.text()
        username = self.ExchangeUsernameInput.text()
        confirmUsername = self.ExchangeConfirmUsernameInput.text()
        if username == self.currentUser:
            showAlert("No need to transfer artwork to yourself")
            return
        if username != confirmUsername:
            showAlert("Username does not match")
            return
        if not checkOwnership(artName, self.currentUser):
            showAlert("Cannot find " + artName + " owned by you")
            return
        if not userExist(username):
            showAlert("User not found")
            return
        self.ExchangeFileNameInput.setEnabled(False)
        self.ExchangeUsernameInput.setEnabled(False)
        self.ExchangeConfirmUsernameInput.setEnabled(False)
        self.btnExchangeConstructBlock.setEnabled(False)
        self.btnExchangeAppendToChain.setEnabled(True)
        self.ExchangePreviewBlockOutputTextArea.setText(generateBlockPreview(self.currentUser, username, artName))
        
    def exchangeAppendClicked(self):
        allText = self.ExchangePreviewBlockOutputTextArea.toPlainText()
        currentHash = allText.split("current_hash: ", 1)[1]
        for line in allText.split("\n"):
            if "nonce: " in line:
                nonce = line.split("nonce: ", 1)[1]
            elif "user_sign: " in line:
                sign = line.split("user_sign: ", 1)[1]
            elif "previous_hash: " in line:
                prevHash = line.split("previous_hash: ", 1)[1]
            elif "base64_art_hash: " in line:
                base64Art = line.split("base64_art_hash: ", 1)[1]
        artName = self.ExchangeFileNameInput.text()
        username = self.ExchangeUsernameInput.text()
        try:
            appendToChain(nonce, prevHash, self.currentUser, sign, artName, base64Art, username, currentHash)
            self.exchangeClearClicked()
            showInfo("Artwork sent")
        except:
            showAlert("Append failed, someone may have used the same nounce, please press clear and try again")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
