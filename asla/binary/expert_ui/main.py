from PyQt5.QtWidgets import QApplication
from expert import ExpertMainWindow

import sip
import sys

sip.setapi("QString", 1)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    a.setStyle("fusion")
    w = ExpertMainWindow()
    w.show()
    a.exec_()
