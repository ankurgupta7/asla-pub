from PyQt5.QtWidgets import QApplication
from login_dialog import LoginDialog
from main_window import MainWindow

import sip
import sys

sip.setapi("QString", 1)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    a.setStyle("fusion")
    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    # while not isAuth:
    loginDialog.exec_()
        # if result == loginDialog.Success or result == loginDialog.Rejected:
        #     isAuth = True
        # else:
        #     isAuth = False
    isAuth = loginDialog.Success

    if isAuth == True:
        w = MainWindow()
        w.show()
        a.exec_()
    # exit(0)