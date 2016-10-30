from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(585, 607)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logoHolder = QtGui.QLabel(self.centralwidget)
        self.logoHolder.setText(_fromUtf8(""))
        self.logoHolder.setPixmap(QtGui.QPixmap(_fromUtf8("resources/logo.png")))
        self.logoHolder.setScaledContents(False)
        self.logoHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.logoHolder.setObjectName(_fromUtf8("logoHolder"))
        self.verticalLayout.addWidget(self.logoHolder)
        self.mainTabContainer = QtGui.QTabWidget(self.centralwidget)
        self.mainTabContainer.setElideMode(QtCore.Qt.ElideRight)
        self.mainTabContainer.setDocumentMode(False)
        self.mainTabContainer.setObjectName(_fromUtf8("mainTabContainer"))
        self.gestureTab = QtGui.QWidget()
        self.gestureTab.setObjectName(_fromUtf8("gestureTab"))
        self.gridLayout = QtGui.QGridLayout(self.gestureTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.predLabel = QtGui.QLabel(self.gestureTab)
        self.predLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(120)
        self.predLabel.setFont(font)
        self.predLabel.setScaledContents(True)
        self.predLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.predLabel.setObjectName(_fromUtf8("predLabel"))
        self.gridLayout.addWidget(self.predLabel, 0, 0, 1, 1)
        self.skeletonView = QtWebKit.QWebView(self.gestureTab)
        self.skeletonView.setUrl(QtCore.QUrl(_fromUtf8("file:///Perlich-Bones.html")))
        self.skeletonView.setObjectName(_fromUtf8("skeletonView"))
        self.gridLayout.addWidget(self.skeletonView, 1, 0, 1, 1)
        self.mainTabContainer.addTab(self.gestureTab, _fromUtf8(""))
        self.gameTab = QtGui.QWidget()
        self.gameTab.setObjectName(_fromUtf8("gameTab"))
        self.applyBtn = QtGui.QPushButton(self.gameTab)
        self.applyBtn.setGeometry(QtCore.QRect(101, 113, 80, 23))
        self.applyBtn.setObjectName(_fromUtf8("applyBtn"))
        self.unameLabel = QtGui.QLabel(self.gameTab)
        self.unameLabel.setGeometry(QtCore.QRect(9, 35, 48, 16))
        self.unameLabel.setObjectName(_fromUtf8("unameLabel"))
        self.pswdLabel = QtGui.QLabel(self.gameTab)
        self.pswdLabel.setGeometry(QtCore.QRect(9, 61, 46, 16))
        self.pswdLabel.setObjectName(_fromUtf8("pswdLabel"))
        self.dispnameLabel = QtGui.QLabel(self.gameTab)
        self.dispnameLabel.setGeometry(QtCore.QRect(9, 9, 64, 16))
        self.dispnameLabel.setObjectName(_fromUtf8("dispnameLabel"))
        self.psqdConfirmL = QtGui.QLabel(self.gameTab)
        self.psqdConfirmL.setGeometry(QtCore.QRect(9, 87, 86, 16))
        self.psqdConfirmL.setObjectName(_fromUtf8("psqdConfirmL"))
        self.dispname = QtGui.QLineEdit(self.gameTab)
        self.dispname.setGeometry(QtCore.QRect(101, 9, 133, 20))
        self.dispname.setObjectName(_fromUtf8("dispname"))
        self.uname = QtGui.QLineEdit(self.gameTab)
        self.uname.setEnabled(False)
        self.uname.setGeometry(QtCore.QRect(101, 35, 133, 20))
        self.uname.setObjectName(_fromUtf8("uname"))
        self.pswd = QtGui.QLineEdit(self.gameTab)
        self.pswd.setGeometry(QtCore.QRect(101, 61, 133, 20))
        self.pswd.setEchoMode(QtGui.QLineEdit.Password)
        self.pswd.setObjectName(_fromUtf8("pswd"))
        self.pswdConfirm = QtGui.QLineEdit(self.gameTab)
        self.pswdConfirm.setGeometry(QtCore.QRect(101, 87, 133, 20))
        self.pswdConfirm.setEchoMode(QtGui.QLineEdit.Password)
        self.pswdConfirm.setObjectName(_fromUtf8("pswdConfirm"))
        self.mainTabContainer.addTab(self.gameTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.mainTabContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.predLabel.setText(_translate("MainWindow", "D", None))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.gestureTab), _translate("MainWindow", "Gesture Mode", None))
        self.applyBtn.setText(_translate("MainWindow", "Apply Changes", None))
        self.unameLabel.setText(_translate("MainWindow", "Username", None))
        self.pswdLabel.setText(_translate("MainWindow", "Password", None))
        self.dispnameLabel.setText(_translate("MainWindow", "Display Name", None))
        self.psqdConfirmL.setText(_translate("MainWindow", "Confirm Password", None))
        self.dispname.setText(_translate("MainWindow", "Ankur Gupta", None))
        self.uname.setText(_translate("MainWindow", "agupta82", None))
        self.pswd.setText(_translate("MainWindow", "asdasda", None))
        self.pswdConfirm.setText(_translate("MainWindow", "asdadsd", None))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.gameTab), _translate("MainWindow", "Profile", None))
    


from PyQt4 import QtWebKit
