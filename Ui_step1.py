# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Py\demo\step1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
import os
from PyQt5.QtWidgets import *
import sys
from PyQt5 import *


from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 960)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        #self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(670,540,250,80))
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton2.setFlat(True)
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setGeometry(QtCore.QRect(670, 640, 250, 80))
        #self.gridLayout.addWidget(self.pushButton, 2, 1, 2, 1)
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #ont = QtGui.QFont()
        #font.setFamily("AcadEref")
        #font.setPointSize(26)

        #self.label.setFont(font)
        #self.label.setAutoFillBackground(False)
        #self.label.setStyleSheet("color: rgb(255, 255, 255);")
        #self.label.setObjectName("label")
        #self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        #spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        #spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        #spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        #spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.close)
        self.pushButton2.clicked.connect(self.close)
        self.retranslateUi(MainWindow)
        self.setWindowIcon(QIcon(os.getcwd() + '\img\logo.ico'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("img/9.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "高空抛物智能监测平台"))
        self.pushButton.setText(_translate("MainWindow", "     "))
        #self.label.setText(_translate("MainWindow", "高空抛物智能监测与分析平台"))
