# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(262, 143)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.loginBtn = QtGui.QPushButton(Dialog)
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.gridLayout.addWidget(self.loginBtn, 2, 2, 1, 2)
        self.rememberMeChk = QtGui.QCheckBox(Dialog)
        self.rememberMeChk.setObjectName(_fromUtf8("rememberMeChk"))
        self.gridLayout.addWidget(self.rememberMeChk, 2, 0, 1, 2)
        self.pswd = QtGui.QLineEdit(Dialog)
        self.pswd.setObjectName(_fromUtf8("pswd"))
        self.gridLayout.addWidget(self.pswd, 1, 0, 1, 4)
        self.uname = QtGui.QLineEdit(Dialog)
        self.uname.setObjectName(_fromUtf8("uname"))
        self.gridLayout.addWidget(self.uname, 0, 0, 1, 4)
        self.hline = QtGui.QFrame(Dialog)
        self.hline.setFrameShape(QtGui.QFrame.HLine)
        self.hline.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline.setObjectName(_fromUtf8("hline"))
        self.gridLayout.addWidget(self.hline, 3, 0, 1, 4)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.signUptxt = QtGui.QLabel(Dialog)
        self.signUptxt.setObjectName(_fromUtf8("signUptxt"))
        self.gridLayout.addWidget(self.signUptxt, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.loginBtn.setText(_translate("Dialog", "Login", None))
        self.rememberMeChk.setText(_translate("Dialog", "Remeber Me", None))
        self.pswd.setText(_translate("Dialog", "Password", None))
        self.uname.setText(_translate("Dialog", "Username", None))
        self.label_4.setText(_translate("Dialog", "<a href=\"http://getasla.com/signup\">Signup</a>", None))
        self.signUptxt.setText(_translate("Dialog", "Don\'t have an account? ", None))

