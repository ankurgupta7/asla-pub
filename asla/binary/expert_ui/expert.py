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
    """Main bean class for the expert ui"""
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # self.status_ready("Connect Leap and Press Spacebar to start")
        self.skeletonView.setUrl(QtCore.QUrl(
            "http://jaanga.github.io/gestification-r2/template-leap-threejs/pehrlich-threejs-bones/pehrlich-threejs-bones.html"))
        self.submitDataBtn.clicked.connect(self.submitDataBtn_clicked)
        self.labelCombo.currentIndexChanged.connect(self.label_combo_changed)
        self.label_3.setText("Repetitions per Label")
        # self.timeleft.setText("3")
        # self.iternum.setText("0")
        self.cal_train_msg_slot("Connect Leap and Press Spacebar to start", "3", "0")
        self.new_train_thread()
        letters = ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.labelCombo.addItems(letters)
        self.train_serv_launch = False
        self.statusbar.show()

    def label_combo_changed(self):
        """Set new label"""
        self.curLabel.setText(self.labelCombo.currentText())

    def new_train_thread(self):
        """Thread used by training service"""
        self.thread = TrainingThread(self)
        self.thread.train_service.exp_ges.msg_ready_signal.connect(self.status_ready)
        self.thread.train_service.exp_ges.iter_rep_signal.connect(self.cal_train_msg_slot)
        self.thread.train_service.exp_ges.calibration.msg_ready_signal.connect(self.cal_train_msg_slot)

    def submitDataBtn_clicked(self):
        """ Collects all the gesture data from expert and sends it to the server for training """
        if (self.thread.train_service.send_to_server() == True):
            self.doSpacebarpressed()
            self.new_train_thread()
            self.cal_train_msg_slot("Data Uploaded. Select a new Label and Press Spacebar to Continue", "3", "0")
            # self.doSpacebarpressed()
        else:
            self.status_ready("Error: Data NOT uploaded. Network TimeOut.")

    def cal_train_msg_slot(self, msg, reps, iter):
        """Displays message to the expert"""
        # text = msg + '. repetitions = ' + iter +'/' + reps
        self.statusbar.showMessage(msg)
        self.iternum.setText(iter)
        self.timeleft.setText(reps)

    def status_ready(self, txt):
        """Show message"""
        self.statusbar.showMessage(txt)

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
            self.thread.train_service.exp_ges.set_stop_thread_flag(False)
            self.thread.kill_gesture_trainion_service_thread()
            self.train_serv_launch = False
            self.status_ready("Training Stopped. Press Spacebar to continue Training or Click Upload Data")
        else:
            if self.labelCombo.currentIndex() == 0:
                self.status_ready("Choose a Label from the Label Dropdown above")
                return
            self.thread.spawn_gesture_trainion_service_thread(self.labelCombo.currentText())
            self.train_serv_launch = True

    def closeEvent(self, *args, **kwargs):
        """Close event"""
        self.thread.kill_gesture_trainion_service_thread()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.doSpacebarpressed()
        else:
            pass


class TrainingThread():
    """Class to manage the Training Thread"""
    def __init__(self, main_window):
        self.thread = None
        self.stop = True

        self.train_service = TrainingService()
        self.main_window = main_window
        self.train_service.make_gesture_obj()

        self.train_service.exp_ges.set_stop_thread_flag(False)
        # self.predict_service.setStatusbar(main_window.statusbar)
        self.status_bar = main_window.statusbar

        self.trained_label = None

    def do_train_label(self, cur_label):
        """Calls the training service """
        print 'in train label. MainWindow. thread functioning'
        if True:
            self.train_service.capture_gesture(label=cur_label)
            # self.train_service.set_status_bar(self.main_window.statusbar)

            if self.stop == True:
                # break
                pass
            time.sleep(0.05)

    def spawn_gesture_trainion_service_thread(self, cur_label):
        """ spawns a thread and calls on gesture predticiton service every few miliseconds"""
        self.thread = threading.Thread(target=self.do_train_label, args=cur_label)
        self.stop = False
        self.thread.start()

    def kill_gesture_trainion_service_thread(self):
        """ kills trainion service and cleans up"""
        self.stop = True
        if self.thread == None:
            return
        self.thread.join(1)
        while self.thread.isAlive():
            self.train_service.exp_ges.set_stop_thread_flag(True)
            print 'why wouldnt you die thread!'
            self.thread.join(1)
