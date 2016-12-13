from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from ui_expert import Ui_MainWindow
from binary.ml_tools.training_service import TrainingService
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# from PyQt4 import QtGui, QtCore
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl

import threading
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class ExpertMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.skeletonView.setUrl(QtCore.QUrl(
            "http://jaanga.github.io/gestification-r2/template-leap-threejs/pehrlich-threejs-bones/pehrlich-threejs-bones.html"))
        self.submitDataBtn.clicked.connect(self.submitDataBtn_clicked)
        self.thread = TrainingThread(self)
        self.train_serv_launch = False
        self.statusbar.show()

    def submitDataBtn_clicked(self):
        """ collects all the gesture data from expert and sends it to the server for training """

    def checkSpacebarpressed(self):
        """checks if the user has pressed spacebar. toggles recording of gestures"""

    def ifLabelTrainingFin(self):
        """checks with the label training service if label traning is over fr particualar label"""

    def offerNextLabel(self):
        """ offers next label for traning if prev label is finised training"""

    def checkIfLabelSelected(self):
        """ does not allow expert to start traning if label is not selected """

    def updateTimeLeft(self):
        """ updates clock to let the expert know of time left to hold gesture"""

    def doSpacebarpressed(self):
        """checks if the user has pressed spacebar. toggles recording of gestures"""
        if self.train_serv_launch:
            self.thread.kill_gesture_trainion_service_thread()
            self.train_serv_launch = False
        else:
            self.thread.spawn_gesture_trainion_service_thread(self.labelCombo.currentText())
            self.train_serv_launch = True

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.doSpacebarpressed()
        else:
            pass


class TrainingThread():
    def __init__(self, main_window):
        self.thread = None
        self.stop = True

        self.train_service = TrainingService()
        self.train_service.set_status_bar(main_window.statusbar)

        self.trained_label = None

    def do_train_label(self, cur_label):
        print 'in train label. MainWindow. thread functioning'
        while True:
            self.train_service.capture_gesture(label=cur_label)
            if self.stop == True:
                break

            time.sleep(0.05)

    def spawn_gesture_trainion_service_thread(self, cur_label):
        """ spawns a thread and calls on gesture predticiton service every few miliseconds"""
        self.thread = threading.Thread(target=self.do_train_label, args=(cur_label))
        self.stop = False
        self.thread.start()

    def kill_gesture_trainion_service_thread(self):
        """ kills trainion service and cleans up"""
        self.stop = True
        self.thread.join(1)
        while self.thread.isAlive():
            print 'why wouldnt you die thread!'
            self.thread.join(1)
