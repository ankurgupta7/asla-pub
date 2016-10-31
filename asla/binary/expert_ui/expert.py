from PyQt4.QtGui import QMainWindow
from ui_expert import Ui_MainWindow
from binary.ml_tools.training_service import TrainingService

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl

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
        self.submitDataBtn.clicked.connect(self.submitDataBtn_clicked)
        self.skeletonView.load(QUrl("http://htmlpreview.github.io/?https://github.com/leapmotion/leapjs/blob/master/examples/threejs-bones.html"))

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
    def spawn_gesture_prediction_service_thread(self):
        """ spawns a thread and calls on gesture predticiton service every few miliseconds"""
        self.thread = threading.Thread(target=self.do_predict_label())
        self.thread.start()

    def kill_gesture_prediction_service_thread(self):
        """ kills prediction service and cleans up"""
        self.thread.join(1)
        if self.thread.isAlive():
            print 'why wouldnt you die thread!'
            self.thread.join(1)

    def do_predict_label(self):
        while True:
            self.predict_service.capture_gesture()
            self.predicted_label = self.predict_service.predict_label()
            time.sleep(0.05)

    def doSpacebarpressed(self):
        """checks if the user has pressed spacebar. toggles recording of gestures"""
        if self.pred_serv_launch:
            self.kill_gesture_prediction_service_thread()
            self.pred_serv_launch = False
        else:
            self.spawn_gesture_prediction_service_thread()
            self.pred_serv_launch = True

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.doSpacebarpressed()
        else:
            pass
