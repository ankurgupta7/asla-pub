# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created: Fri Nov 18 18:13:29 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    """QT generated class"""
    def setupUi(self, Dialog):
        """QT generated method"""
        Dialog.setObjectName("Dialog")
        Dialog.resize(262, 143)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setObjectName("loginBtn")
        self.gridLayout.addWidget(self.loginBtn, 2, 2, 1, 2)
        self.rememberMeChk = QtWidgets.QCheckBox(Dialog)
        self.rememberMeChk.setObjectName("rememberMeChk")
        self.gridLayout.addWidget(self.rememberMeChk, 2, 0, 1, 2)
        self.pswd = QtWidgets.QLineEdit(Dialog)
        self.pswd.setObjectName("pswd")
        self.gridLayout.addWidget(self.pswd, 1, 0, 1, 4)
        self.uname = QtWidgets.QLineEdit(Dialog)
        self.uname.setObjectName("uname")
        self.gridLayout.addWidget(self.uname, 0, 0, 1, 4)
        self.hline = QtWidgets.QFrame(Dialog)
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.gridLayout.addWidget(self.hline, 3, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.signUptxt = QtWidgets.QLabel(Dialog)
        self.signUptxt.setObjectName("signUptxt")
        self.gridLayout.addWidget(self.signUptxt, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """QT generated method"""
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginBtn.setText(_translate("Dialog", "Login"))
        self.rememberMeChk.setText(_translate("Dialog", "Remeber Me"))
        self.pswd.setText(_translate("Dialog", "Password"))
        self.uname.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "<a href=\"http://getasla.com/signup\">Signup</a>"))
        self.signUptxt.setText(_translate("Dialog", "Don\'t have an account? "))

