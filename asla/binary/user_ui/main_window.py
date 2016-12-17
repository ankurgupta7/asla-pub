from ui_main_window import Ui_MainWindow
from binary.ml_tools.predict_service import PredictService

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QMainWindow
import threading
import time
import glob
import os
import requests
import json

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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        [self.model_path, self.scaler_path] = self.update_models()
        self.thread = PredictionThread(self, self.model_path, self.scaler_path)
        self.thread.predict_service.user_ges.msg_ready_signal.connect(self.status_ready)
        self.pred_serv_launch = False
        QWebSettings.globalSettings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)
        QWebSettings.globalSettings().setAttribute(QWebSettings.WebGLEnabled, True)
        self.applyBtn.clicked.connect(self.applyBtn_clicked)

    def status_ready(self, txt):
        self.statusbar.showMessage(txt)
    def update_models(self):
        """ checks if the model is stale and updates it from remote
        returns the filepath for the latest model file"""
        # model_files = glob.glob("../models/model*pkl")
        # scaler_files =  glob.glob("../models/scaler*pkl")
        model_fname = 'model.pkl'
        scaler_fname = 'scaler.pkl'
        try:
            model_json = requests.get("http://asla.heroku.com/models")
            model_url = json.load(model_json)['url']
            r = requests.get(model_url)
            with open(model_fname, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
            scaler_json = requests.get("http://asla.heroku.com/scalers")
            scaler_url = json.load(model_json)['url']
            r = requests.get(scaler_url)
            with open(scaler_fname, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
        except Exception as e:
            latest_model = os.path.abspath(model_fname)
            latest_scaler = os.path.abspath(scaler_fname)

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

    def doSpacebarpressed(self):
        """checks if the user has pressed spacebar. toggles recording of gestures"""
        # connecting pyqt threadsafe

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
    a
    return None


class PredictionThread():
    def __init__(self, main_window, model_path, scaler_path):
        self.thread = None
        self.stop = True

        self.predict_service = PredictService(model_path, scaler_path)
        self.predict_service.make_gesture_obj()
        # self.predict_service.setStatusbar(main_window.statusbar)
        self.status_bar = main_window.statusbar
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
        self.readMessageThread = threading.Thread(target=self.do_read_msg)
    def do_read_msg(self):
        msg = self.predict_service.user_ges.getStatus()
        self.status_bar.showMessage(msg)
    def kill_gesture_prediction_service_thread(self):
        """ kills prediction service and cleans up"""
        self.stop = True
        self.thread.join(1)
        # self.readMessageThread.join(1);
        while self.thread.isAlive() or self.readMessageThread.isAlive():
            print 'why wouldnt you die thread!'
            self.thread.join(1)