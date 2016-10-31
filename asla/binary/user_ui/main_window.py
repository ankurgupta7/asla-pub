
from ui_main_window import Ui_MainWindow
from PyQt4 import QtGui, QtCore
# from asla..predict_service import PredictService
from PyQt4.QtGui import QApplication
from binary.ml_tools.predict_service import PredictService

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

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.predict_service = PredictService('','')
        self.predicted_label = None
        self.thread = threading.Thread(target=self.do_predict_label())

        self.applyBtn.clicked.connect(self.applyBtn_clicked())
        self.pred_serv_launch = False

    def applyBtn_clicked(self):
        """ collects data from input fields and sends it to server for authenctication """


    def skeletonView_render(self, handCoords):
        """ does projections of hand coordinates on 3d space and renders bones on screen
            :param handCoords: hand coordinates for all fingers and thumbs
        """
        asla_unused(handCoords)
        self.skeletonView.setUrl('file:///../resources/Perlich_Bones.html')

    def spawn_gesture_prediction_service_thread(self):
        """ spawns a thread and calls on gesture predticiton service every few miliseconds"""
        self.thread.start()

    def kill_gesture_prediction_service_thread(self):
        """ """
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



def asla_unused(a):
    return None