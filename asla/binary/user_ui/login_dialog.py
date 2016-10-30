from ui_main_window import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMessageBox


class LoginDialog(QtGui.QDialog, Ui_MainWindow):
    def __init__(self):
        QtGui.QDialog.__init__()
        self.setupUi(self)

        self.loginBtn.clicked.connect(self.loginBtn_clicked())


    def onAccept(self):
        # auth = Auth()
        if True: #auth.doLogin(self.txtUsername.text(), self.txtPassword.text()):
            self.setResult(self.Success)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle(("LoginDialog", "Pythonthusiast", None))
            msgBox.setText(("LoginDialog", "Either incorrect username and/or password. Try again!", None))
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)


    def loginBtn_clicked(self):
        """ sends the username and password to server for euthentication """
        print('db not setup. Enjoy.. EEHAAHA!!')
        self.result = True
