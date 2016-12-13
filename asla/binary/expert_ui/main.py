from PyQt5.QtWidgets import QApplication
from expert import ExpertMainWindow

import sip
import sys

sip.setapi("QString", 1)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    a.setStyle("fusion")
    # loginDialog = LoginDialog()

    # isAuth = False
    # result = -1
    # while not isAuth:
    #     result = loginDialog.exec_()
    #     if result == LoginDialog.Success or result == LoginDialog.Rejected:
    #         isAuth = True
    #     else:
    #         isAuth = False


    # if result == LoginDialog.Success:
    w = ExpertMainWindow()
    w.show()
    a.exec_()
