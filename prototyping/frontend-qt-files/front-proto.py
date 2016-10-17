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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(472, 501)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainTabContainer = QtGui.QTabWidget(self.centralwidget)
        self.mainTabContainer.setObjectName(_fromUtf8("mainTabContainer"))
        self.gestureTab = QtGui.QWidget()
        self.gestureTab.setObjectName(_fromUtf8("gestureTab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.gestureTab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.boneWebV = KWebView(self.gestureTab)
        self.boneWebV.setUrl(QtCore.QUrl(_fromUtf8("file:///home/srinivas/Perlich-Bones.html")))
        self.boneWebV.setObjectName(_fromUtf8("boneWebV"))
        self.horizontalLayout.addWidget(self.boneWebV)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.predLabel = QtGui.QLabel(self.gestureTab)
        self.predLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.predLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.predLabel.setObjectName(_fromUtf8("predLabel"))
        self.horizontalLayout.addWidget(self.predLabel)
        self.mainTabContainer.addTab(self.gestureTab, _fromUtf8(""))
        self.gameTab = QtGui.QWidget()
        self.gameTab.setObjectName(_fromUtf8("gameTab"))
        self.mainTabContainer.addTab(self.gameTab, _fromUtf8(""))
        self.profileTab = QtGui.QWidget()
        self.profileTab.setObjectName(_fromUtf8("profileTab"))
        self.mainTabContainer.addTab(self.profileTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.mainTabContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.predLabel.setText(_translate("MainWindow", "Prediction", None))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.gestureTab), _translate("MainWindow", "Gesture Mode", None))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.gameTab), _translate("MainWindow", "Profile Settings", None))
        self.mainTabContainer.setTabText(self.mainTabContainer.indexOf(self.profileTab), _translate("MainWindow", "Game Mode", None))

from kwebview import KWebView
