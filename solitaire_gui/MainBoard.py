# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1155, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 80, 116))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 40, 80, 116))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 150, 800, 400))
        self.label.setObjectName("label")

        self.rules_label = QtWidgets.QLabel(self.centralwidget)
        self.rules_label.setGeometry(QtCore.QRect(1010, 40, 120, 280))
        self.rules_label.setObjectName("label")
        self.rules_label.setStyleSheet("font: 14pt Comic Sans MS;border-radius: 15px;border: 3px solid white;color: white;")
        self.rules_label.setText("Rules:\nK\nT + Q\nJ + 2\n10 + 3\n9 + 4\n8 + 5\n7 + 6")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1030, 710, 55, 25))
        self.lcdNumber.setObjectName("lcdNumber")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 26))
        self.menubar.setObjectName("menubar")
        self.menuPoints = QtWidgets.QMenu(self.menubar)
        self.menuPoints.setObjectName("menuPoints")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "N"))
        self.pushButton_2.setText(_translate("MainWindow", "N"))
        self.menuPoints.setTitle(_translate("MainWindow", "Rules"))
