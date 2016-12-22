# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created: Fri Nov 18 18:10:57 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    """QT generated class for User UI Main Window"""
    def setupUi(self, MainWindow):
        """QT generated method"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logoHolder = QtWidgets.QLabel(self.centralwidget)
        self.logoHolder.setText("")
        self.logoHolder.setPixmap(QtGui.QPixmap("resources/logo.png"))
        self.logoHolder.setScaledContents(False)
        self.logoHolder.setAlignment(QtCore.Qt.AlignCenter)
        self.logoHolder.setObjectName("logoHolder")
        self.verticalLayout.addWidget(self.logoHolder)
        self.mainTabContainer = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabContainer.setElideMode(QtCore.Qt.ElideRight)
        self.mainTabContainer.setDocumentMode(False)
        self.mainTabContainer.setObjectName("mainTabContainer")
        self.gestureTab = QtWidgets.QWidget()
        self.gestureTab.setObjectName("gestureTab")
        self.gridLayout = QtWidgets.QGridLayout(self.gestureTab)
        self.gridLayout.setObjectName("gridLayout")
        self.predLabel = QtWidgets.QLabel(self.gestureTab)
        self.predLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(120)
        self.predLabel.setFont(font)
        self.predLabel.setScaledContents(True)
        self.predLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.predLabel.setObjectName("predLabel")
        self.gridLayout.addWidget(self.predLabel, 0, 0, 1, 1)
        self.skeletonView = QtWebKitWidgets.QWebView(self.gestureTab)
        self.skeletonView.setUrl(QtCore.QUrl("http://jaanga.github.io/gestification-r2/template-leap-threejs/pehrlich-threejs-bones/pehrlich-threejs-bones.html"))
        self.skeletonView.setObjectName("skeletonView")
        self.gridLayout.addWidget(self.skeletonView, 1, 0, 1, 1)
        self.mainTabContainer.addTab(self.gestureTab, "")
        self.gameTab = QtWidgets.QWidget()
        self.gameTab.setObjectName("gameTab")
        self.applyBtn = QtWidgets.QPushButton(self.gameTab)
        self.applyBtn.setGeometry(QtCore.QRect(101, 113, 80, 23))
        self.applyBtn.setObjectName("applyBtn")
        self.unameLabel = QtWidgets.QLabel(self.gameTab)
        self.unameLabel.setGeometry(QtCore.QRect(9, 35, 48, 16))
        self.unameLabel.setObjectName("unameLabel")
        self.pswdLabel = QtWidgets.QLabel(self.gameTab)
        self.pswdLabel.setGeometry(QtCore.QRect(9, 61, 46, 16))
        self.pswdLabel.setObjectName("pswdLabel")
        self.dispnameLabel = QtWidgets.QLabel(self.gameTab)
        self.dispnameLabel.setGeometry(QtCore.QRect(9, 9, 64, 16))
        self.dispnameLabel.setObjectName("dispnameLabel")
        self.psqdConfirmL = QtWidgets.QLabel(self.gameTab)
        self.psqdConfirmL.setGeometry(QtCore.QRect(9, 87, 86, 16))
        self.psqdConfirmL.setObjectName("psqdConfirmL")
        self.dispname = QtWidgets.QLineEdit(self.gameTab)
        self.dispname.setGeometry(QtCore.QRect(101, 9, 133, 20))
        self.dispname.setObjectName("dispname")
        self.uname = QtWidgets.QLineEdit(self.gameTab)
        self.uname.setEnabled(False)
        self.uname.setGeometry(QtCore.QRect(101, 35, 133, 20))
        self.uname.setObjectName("uname")
        self.pswd = QtWidgets.QLineEdit(self.gameTab)
        self.pswd.setGeometry(QtCore.QRect(101, 61, 133, 20))
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswd.setObjectName("pswd")
        self.pswdConfirm = QtWidgets.QLineEdit(self.gameTab)
        self.pswdConfirm.setGeometry(QtCore.QRect(101, 87, 133, 20))
        self.pswdConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswdConfirm.setObjectName("pswdConfirm")
        self.mainTabContainer.addTab(self.gameTab, "")
        self.verticalLayout.addWidget(self.mainTabContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """QT generated method"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.predLabel.setText(_translate("MainWindow", "D"))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.gestureTab), _translate("MainWindow", "Gesture Mode"))
        self.applyBtn.setText(_translate("MainWindow", "Apply Changes"))
        self.unameLabel.setText(_translate("MainWindow", "Username"))
        self.pswdLabel.setText(_translate("MainWindow", "Password"))
        self.dispnameLabel.setText(_translate("MainWindow", "Display Name"))
        self.psqdConfirmL.setText(_translate("MainWindow", "Confirm Password"))
        self.dispname.setText(_translate("MainWindow", "Ankur Gupta"))
        self.uname.setText(_translate("MainWindow", "agupta82"))
        self.pswd.setText(_translate("MainWindow", "asdasda"))
        self.pswdConfirm.setText(_translate("MainWindow", "asdadsd"))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.gameTab), _translate("MainWindow", "Profile"))

from PyQt5 import QtWebKitWidgets
