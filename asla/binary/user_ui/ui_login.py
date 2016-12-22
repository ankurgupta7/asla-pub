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

class Ui_loginForm(object):
    """ Main class for handling login ui for the user"""
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
        self.loginBtn = QtGui.QPushButton(loginForm)
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.gridLayout.addWidget(self.loginBtn, 2, 2, 1, 2)
        self.rememberMeChk = QtGui.QCheckBox(loginForm)
        self.rememberMeChk.setObjectName(_fromUtf8("rememberMeChk"))
        self.gridLayout.addWidget(self.rememberMeChk, 2, 0, 1, 2)
        self.pswd = QtGui.QLineEdit(loginForm)
        self.pswd.setObjectName(_fromUtf8("pswd"))
        self.gridLayout.addWidget(self.pswd, 1, 0, 1, 4)
        self.uname = QtGui.QLineEdit(loginForm)
        self.uname.setObjectName(_fromUtf8("uname"))
        self.gridLayout.addWidget(self.uname, 0, 0, 1, 4)
        self.hline = QtGui.QFrame(loginForm)
        self.hline.setFrameShape(QtGui.QFrame.HLine)
        self.hline.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline.setObjectName(_fromUtf8("hline"))
        self.gridLayout.addWidget(self.hline, 3, 0, 1, 4)
        self.label_4 = QtGui.QLabel(loginForm)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.signUptxt = QtGui.QLabel(loginForm)
        self.signUptxt.setObjectName(_fromUtf8("signUptxt"))
        self.gridLayout.addWidget(self.signUptxt, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        """repaints the ui on scaling and moving"""
        loginForm.setWindowTitle(_translate("loginForm", "Form", None))
        self.loginBtn.setText(_translate("loginForm", "Login", None))
        self.rememberMeChk.setText(_translate("loginForm", "Remeber Me", None))
        self.pswd.setText(_translate("loginForm", "Password", None))
        self.uname.setText(_translate("loginForm", "Username", None))
        self.label_4.setText(_translate("loginForm", "<a href=\"http://getasla.com/signup\">Signup</a>", None))
        self.signUptxt.setText(_translate("loginForm", "Don\'t have an account? ", None))