from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    """ main native binary ui class for expert """
    def setupUi(self, MainWindow):
        """ sets up the ui with pre fixed values. """

        MainWindow.setObjectName(_fromUtf8("Asla_Expert"))
        MainWindow.resize(679, 416)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.skeletonView = QtWebKit.QWebView(self.centralwidget)
        self.skeletonView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.skeletonView.setObjectName(_fromUtf8("skeletonView"))
        self.gridLayout_2.addWidget(self.skeletonView, 1, 0, 1, 3)
        self.labelCombo = QtGui.QComboBox(self.centralwidget)
        self.labelCombo.setStatusTip(_fromUtf8(""))
        self.labelCombo.setObjectName(_fromUtf8("labelCombo"))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.labelCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.labelCombo, 0, 0, 1, 1)
        self.submitDataBtn = QtGui.QPushButton(self.centralwidget)
        self.submitDataBtn.setObjectName(_fromUtf8("submitDataBtn"))
        self.gridLayout_2.addWidget(self.submitDataBtn, 2, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.curLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curLabel.setFont(font)
        self.curLabel.setObjectName(_fromUtf8("curLabel"))
        self.gridLayout.addWidget(self.curLabel, 1, 0, 1, 1)
        self.iternum = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iternum.setFont(font)
        self.iternum.setObjectName(_fromUtf8("iternum"))
        self.gridLayout.addWidget(self.iternum, 1, 1, 1, 1)
        self.timeleft = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeleft.setFont(font)
        self.timeleft.setObjectName(_fromUtf8("timeleft"))
        self.gridLayout.addWidget(self.timeleft, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Asla_Expert):
        """repaints the ui on scaling and moving"""
        Asla_Expert.setWindowTitle(_translate("Asla_Expert", "MainWindow", None))
        self.labelCombo.setItemText(0, _translate("Asla_Expert", "Choose a Label to Train", None))
        self.labelCombo.setItemText(1, _translate("Asla_Expert", "A", None))
        self.labelCombo.setItemText(2, _translate("Asla_Expert", "B", None))
        self.labelCombo.setItemText(3, _translate("Asla_Expert", "C", None))
        self.labelCombo.setItemText(4, _translate("Asla_Expert", "D", None))
        self.labelCombo.setItemText(5, _translate("Asla_Expert", "E", None))
        self.labelCombo.setItemText(6, _translate("Asla_Expert", "F", None))
        self.labelCombo.setItemText(7, _translate("Asla_Expert", "G", None))
        self.labelCombo.setItemText(8, _translate("Asla_Expert", "H", None))
        self.labelCombo.setItemText(9, _translate("Asla_Expert", "I", None))
        self.labelCombo.setItemText(10, _translate("Asla_Expert", "J", None))
        self.labelCombo.setItemText(11, _translate("Asla_Expert", "K", None))
        self.labelCombo.setItemText(12, _translate("Asla_Expert", "L", None))
        self.labelCombo.setItemText(13, _translate("Asla_Expert", "M", None))
        self.labelCombo.setItemText(14, _translate("Asla_Expert", "N", None))
        self.labelCombo.setItemText(15, _translate("Asla_Expert", "O", None))
        self.labelCombo.setItemText(16, _translate("Asla_Expert", "P", None))
        self.submitDataBtn.setText(_translate("Asla_Expert", "Submit Gesture Data to Server", None))
        self.label.setText(_translate("Asla_Expert", "Label being Trained", None))
        self.label_2.setText(_translate("Asla_Expert", "Iteration#", None))
        self.label_3.setText(_translate("Asla_Expert", "Hold For", None))
        self.curLabel.setText(_translate("Asla_Expert", "A", None))
        self.iternum.setText(_translate("Asla_Expert", "1", None))
        self.timeleft.setText(_translate("Asla_Expert", "5s", None))


from PyQt4 import QtWebKit
