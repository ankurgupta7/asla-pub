from ui_login_dialog import Ui_Dialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QDialog, QLineEdit

import requests
from requests.auth import HTTPDigestAuth
import json

url = 'https://aslaflaskwebsite.herokuapp.com/authenticate'


class LoginDialog(QDialog, Ui_Dialog):
    """Login Dialog"""
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pswd.setEchoMode(QLineEdit.Password)
        self.loginBtn.clicked.connect(self.loginBtn_clicked)
        self.Success = False
        self.uname.setText('bonjour.trevor@gmail.com')
        self.pswd.setText('asla')

    def onAccept(self):
        # auth = Auth()
        payload ={}
        payload['email'] = self.uname.text()
        payload['pwd'] = self.pswd.text()

        # payload = (json.dumps(payload))
        myResponse = requests.post(url, payload)

        #myResponse.ok = True
        if (myResponse.status_code == 200): #auth.doLogin(self.txtUsername.text(), self.txtPassword.text()):
            # if True:
            # self.setResult(self.Success)
            self.Success = True
            self.close()
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
                # print('db not setup. Enjoy.. EEHAAHA!!')
            msgBox.setWindowTitle("Failed Login")
            msgBox.setText("Either incorrect username and/or password. Try again!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            # self.setResult(self.)

    def loginBtn_clicked(self):
        """ sends the username and password to server for euthentication """
        self.onAccept()



