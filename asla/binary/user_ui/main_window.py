from ui_main_window import Ui_MainWindow
from binary.ml_tools.predict_service import PredictService

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebSettings
import threading
import time
import glob
import os


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

        [self.model_path, self.scaler_path] = self.update_models()
        self.thread = PredictionThread(self, self.model_path, self.scaler_path)
        self.pred_serv_launch = False
        QWebSettings.globalSettings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)
        QWebSettings.globalSettings().setAttribute(QWebSettings.WebGLEnabled, True)
        self.applyBtn.clicked.connect(self.applyBtn_clicked)

    def update_models(self):
        """ checks if the model is stale and updates it from remote
        returns the filepath for the latest model file"""
        model_files = glob.glob("../models/model*pkl")
        latest_model = os.path.abspath(max(model_files))
        scaler_files =  glob.glob("../models/scaler*pkl")
        latest_scaler = os.path.abspath(max(scaler_files))

        return (latest_model, latest_scaler)

    def applyBtn_clicked(self):
        """ collects data from input fields and sends it to server for authenctication """
        print("Nice that you clicked Apply. nothing will happen though!")

    def skeleton_view_render(self, handCoords):
        """ does projections of hand coordinates on 3d space and renders bones on screen
            :param handCoords: hand coordinates for all fingers and thumbs
        """
        asla_unused(handCoords)
        self.skeletonView.setUrl('file:///../resources/Perlich_Bones.html')

    # def do_predict_label(self):
    #     while True:
    #         print 'in predict label. mainwindow. thread functioning'
    #         # self.predict_service.capture_gesture()
    #         # self.predicted_label = self.predict_service.predict_label()
    #         time.sleep(0.500)

    def doSpacebarpressed(self):
        """checks if the user has pressed spacebar. toggles recording of gestures"""
        if self.pred_serv_launch:
            self.thread.kill_gesture_prediction_service_thread()
            self.pred_serv_launch = False
        else:
            self.thread.spawn_gesture_prediction_service_thread()
            self.pred_serv_launch = True

    def keyPressEvent(self, event):
        print 'key press detected!'
        if event.key() == QtCore.Qt.Key_Space:
            self.doSpacebarpressed()
        else:
            pass


def asla_unused(a):
    return None


class PredictionThread():
    def __init__(self, main_window, model_path, scaler_path):
        self.thread = None
        self.stop = True

        self.predict_service = PredictService(model_path, scaler_path)
        self.predict_service.setStatusbar(main_window.statusbar)
        self.predicted_label = None
        self.main_window = main_window

    def do_predict_label(self):
        print 'in predict label. mainwindow. thread functioning'
        while True:
            self.predict_service.capture_gesture()
            self.predicted_label = self.predict_service.predict_label()
            self.main_window.predLabel.setText(self.predicted_label)
            if self.stop == True:
                break

            time.sleep(0.05)

    def spawn_gesture_prediction_service_thread(self):
        """ spawns a thread and calls on gesture predticiton service every few miliseconds"""
        self.thread = threading.Thread(target=self.do_predict_label)
        self.stop = False
        self.thread.start()

    def kill_gesture_prediction_service_thread(self):
        """ kills prediction service and cleans up"""
        self.stop = True
        self.thread.join(1)
        while self.thread.isAlive():
            print 'why wouldnt you die thread!'
            self.thread.join(1)