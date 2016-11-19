from ui_login_dialog import Ui_Dialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QDialog


import requests
from requests.auth import HTTPDigestAuth
import json

url = 'https://google.com'

class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.loginBtn.clicked.connect(self.loginBtn_clicked)
        self.Success = False

    def onAccept(self):
        # auth = Auth()

        myResponse = requests.post(url, auth=HTTPDigestAuth(self.uname.text(), self.pswd.text()),
                                  verify=True)
        #
        # myResponse.ok = True
        # if (myResponse.ok): #auth.doLogin(self.txtUsername.text(), self.txtPassword.text()):
        if True:
            self.setResult(self.Success)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle(QtCore.QString("Failed Login"))
            msgBox.setText("Either incorrect username and/or password. Try again!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)

    def loginBtn_clicked(self):
        """ sends the username and password to server for euthentication """
        self.onAccept()
        print('db not setup. Enjoy.. EEHAAHA!!')
        self.Success = True
        self.close()
