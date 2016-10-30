from PyQt4.QtGui import QApplication
from login_dialog import LoginDialog
from main_window import MainWindow

import sip
import sys

sip.setapi("QString", 2)


if __name__ == "__main__":
    a = QApplication(sys.argv)

    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()
        if result == LoginDialog.Success or result == LoginDialog.Rejected:
            isAuth = True
        else:
            isAuth = False


    # if result == LoginDialog.Success:
    w = MainWindow()
    w.show()
    a.exec_()
