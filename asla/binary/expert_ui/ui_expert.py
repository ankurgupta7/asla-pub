# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expert.ui'
#
# Created: Mon Dec 12 22:19:50 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.skeletonView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.skeletonView.setUrl(QtCore.QUrl("http://jaanga.github.io/gestification-r2/template-leap-threejs/pehrlich-threejs-bones/pehrlich-threejs-bones.html"))

        self.skeletonView.setObjectName("skeletonView")
        self.gridLayout_2.addWidget(self.skeletonView, 1, 0, 1, 3)
        self.labelCombo = QtWidgets.QComboBox(self.centralwidget)
        self.labelCombo.setStatusTip("")
        self.labelCombo.setObjectName("labelCombo")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.labelCombo.addItem("")
        self.gridLayout_2.addWidget(self.labelCombo, 0, 0, 1, 1)
        self.submitDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitDataBtn.setObjectName("submitDataBtn")
        self.gridLayout_2.addWidget(self.submitDataBtn, 2, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.curLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curLabel.setFont(font)
        self.curLabel.setObjectName("curLabel")
        self.gridLayout.addWidget(self.curLabel, 1, 0, 1, 1)
        self.iternum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iternum.setFont(font)
        self.iternum.setObjectName("iternum")
        self.gridLayout.addWidget(self.iternum, 1, 1, 1, 1)
        self.timeleft = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeleft.setFont(font)
        self.timeleft.setObjectName("timeleft")
        self.gridLayout.addWidget(self.timeleft, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCombo.setItemText(0, _translate("MainWindow", "Choose a Label to Train"))
        self.labelCombo.setItemText(1, _translate("MainWindow", "A"))
        self.labelCombo.setItemText(2, _translate("MainWindow", "B"))
        self.labelCombo.setItemText(3, _translate("MainWindow", "C"))
        self.labelCombo.setItemText(4, _translate("MainWindow", "D"))
        self.labelCombo.setItemText(5, _translate("MainWindow", "E"))
        self.labelCombo.setItemText(6, _translate("MainWindow", "F"))
        self.labelCombo.setItemText(7, _translate("MainWindow", "G"))
        self.labelCombo.setItemText(8, _translate("MainWindow", "H"))
        self.labelCombo.setItemText(9, _translate("MainWindow", "I"))
        self.labelCombo.setItemText(10, _translate("MainWindow", "J"))
        self.labelCombo.setItemText(11, _translate("MainWindow", "K"))
        self.labelCombo.setItemText(12, _translate("MainWindow", "L"))
        self.labelCombo.setItemText(13, _translate("MainWindow", "M"))
        self.labelCombo.setItemText(14, _translate("MainWindow", "N"))
        self.labelCombo.setItemText(15, _translate("MainWindow", "O"))
        self.labelCombo.setItemText(16, _translate("MainWindow", "P"))
        self.submitDataBtn.setText(_translate("MainWindow", "Submit Gesture Data to Server"))
        self.label.setText(_translate("MainWindow", "Label being Trained"))
        self.label_2.setText(_translate("MainWindow", "Iteration#"))
        self.label_3.setText(_translate("MainWindow", "Hold For"))
        self.curLabel.setText(_translate("MainWindow", "A"))
        self.iternum.setText(_translate("MainWindow", "1"))
        self.timeleft.setText(_translate("MainWindow", "5s"))

from PyQt5 import QtWebKitWidgets
