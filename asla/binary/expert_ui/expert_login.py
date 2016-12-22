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


class Ui_ExpertloginForm(object):
    """ Login form for expert"""

    def setupUi(self, loginForm):
        """ sets up the ui with pre fixed values. """
        loginForm.setObjectName(_fromUtf8("loginForm"))
        loginForm.resize(271, 139)
        self.verticalLayout = QtGui.QVBoxLayout(loginForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.remMeChk = QtGui.QCheckBox(loginForm)
        self.remMeChk.setObjectName(_fromUtf8("remMeChk"))
        self.gridLayout.addWidget(self.remMeChk, 1, 0, 1, 2)
        self.atoken = QtGui.QLineEdit(loginForm)
        self.atoken.setObjectName(_fromUtf8("atoken"))
        self.gridLayout.addWidget(self.atoken, 0, 0, 1, 4)
        self.loginbtn = QtGui.QPushButton(loginForm)
        self.loginbtn.setObjectName(_fromUtf8("loginbtn"))
        self.gridLayout.addWidget(self.loginbtn, 1, 2, 1, 2)
        self.signupLink = QtGui.QLabel(loginForm)
        self.signupLink.setOpenExternalLinks(True)
        self.signupLink.setObjectName(_fromUtf8("signupLink"))
        self.gridLayout.addWidget(self.signupLink, 3, 2, 1, 1)
        self.signupText = QtGui.QLabel(loginForm)
        self.signupText.setObjectName(_fromUtf8("signupText"))
        self.gridLayout.addWidget(self.signupText, 3, 1, 1, 1)
        self.line = QtGui.QFrame(loginForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        """Repaints the UI on scaling and moving"""
        loginForm.setWindowTitle(_translate("loginForm", "Form", None))
        self.remMeChk.setText(_translate("loginForm", "Remeber Me", None))
        self.atoken.setText(_translate("loginForm", "Expert Access Token", None))
        self.loginbtn.setText(_translate("loginForm", "Login", None))
        self.signupLink.setText(_translate("loginForm", "<a href=\"http://getasla.com/signup\">Signup</a>", None))
        self.signupText.setText(_translate("loginForm", "Don\'t have an account? ", None))

    def loginbtnClicked(self):
        """ sends the authentication token to server for authentication """
