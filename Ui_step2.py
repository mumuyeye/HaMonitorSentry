# -*- coding: utf-8 -*-
import os
# Form implementation generated from reading ui file 'e:\Py\demo\step2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
from PyQt5.QtChart import QChartView
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import (QChartView, QChart, QBarSeries, QBarSet, QLineSeries, QPieSeries,
                           QLegend, QBarCategoryAxis, QValueAxis)
import cv2
from datetime import datetime
import random
from PyQt5.QtCore import QTimer

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #返回主界面
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 17, 170, 45))
        self.pushButton.setStyleSheet("color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFlat(True)
        #下一组
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(200, 855, 210, 60))
        self.pushButton_0.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_0.setFlat(True)
        #刷新数据
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1025, 850, 210, 60))
        self.pushButton_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setFlat(True)

        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(100, 100, 200, 40))
        #font = QtGui.QFont()
        #font.setFamily("AcadEref")
        #font.setPointSize(14)
        #self.label.setFont(font)
        #self.label.setStyleSheet("color: rgb(255, 255, 255);")
        #self.label.setObjectName("label")
        """
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 1000, 1100))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        """
        self.p0 = QtWidgets.QLabel(self.centralwidget)
        self.p1 = QtWidgets.QLabel(self.centralwidget)
        self.p2 = QtWidgets.QLabel(self.centralwidget)
        self.p3 = QtWidgets.QLabel(self.centralwidget)
        self.p4 = QtWidgets.QLabel(self.centralwidget)
        self.p5 = QtWidgets.QLabel(self.centralwidget)
        self.p6 = QtWidgets.QLabel(self.centralwidget)
        self.p7 = QtWidgets.QLabel(self.centralwidget)
        self.p8 = QtWidgets.QLabel(self.centralwidget)

        self.p = [self.p0,self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7,self.p8]

        self.create_label(self.p0, "p0", 200, 105, 800//3, 720)
        self.create_label(self.p1, "p1", 200+800//3, 105, 800//3, 720 // 3)
        self.create_label(self.p2, "p2", 200+800//3+800//3, 105, 800 // 3, 720 // 3)

        self.create_label(self.p3, "p3", 200, 105+720//3, 800 // 3, 720 // 3)
        self.create_label(self.p4, "p4", 200+800//3, 105+720//3, 800 // 3, 720 // 3)
        self.create_label(self.p5, "p5", 200+800//3+800//3, 105+720//3, 800 // 3, 720 // 3)

        self.create_label(self.p6, "p6", 200, 105+720//3+720//3, 800 // 3, 720 // 3)
        self.create_label(self.p7, "p7", 200+800//3, 105+720//3+720//3, 800 // 3, 720 // 3)
        self.create_label(self.p8, "p8", 200+800//3+800//3, 105+720//3+720//3, 800 // 3, 720 // 3)





        self.graphicsView = QChartView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(1030, 50, 528, 375))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("background-color: rgba(255, 0, 0, 0);\n"
                                       "border:0px;")

        #self.graphicsView_2 = QChartView(self.centralwidget)
        #self.graphicsView_2.setGeometry(QtCore.QRect(1000, 700, 600, 550))
        #self.graphicsView_2.setObjectName("graphicsView_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        #self.textBrowser.setGeometry(QtCore.QRect(50, 150, 750, 800))
        self.textBrowser.setGeometry(QtCore.QRect(1040,455,508,370))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: rgba(255, 0, 0, 0);\n"
                                       "border:0px;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("img/3.png")
        painter.drawPixmap(self.rect(), pixmap)

    def create_label(self, name,p,x,y,w,h):

        name.setGeometry(QtCore.QRect(x, y, w, h))
        name.setStyleSheet("background-color: rgb(255, 255, 255);")
        name.setText("")
        name.setObjectName(p)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据分析"))
        #self.pushButton.setText(_translate("MainWindow", "返回主界面"))
        #self.pushButton_0.setText(_translate("MainWindow", "下一组"))
        #self.pushButton_1.setText(_translate("MainWindow", "刷新数据"))
        #self.label.setText(_translate("MainWindow", "历史抛物统计"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
from PyQt5.QtChart import QChartView


class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = "video/history_record/"
        self.flag = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.P = self.ui.p
        self.picture()
        self.current_index = 0 
        self.filepath = os.listdir("history_img")
        self.filepath.sort(key=lambda x: datetime.strptime(x, '%Y-%m-%d'), reverse=False)  
        self.ui.pushButton_0.clicked.connect(self.picture)
        self.ui.pushButton_1.clicked.connect(self.printf)
        self.setWindowIcon(QIcon(os.getcwd() + '/img/logo.ico'))
        self.printf()
        self.createChart()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createChart(self):
        # 创建条状单元
        barSet0 = QBarSet('高空抛物数量')
        barSet0.append([2, 1, 3, 3, 0, 5, 1, 0, 1, 2, 4, 0])
        barSet0.setColor(QColor(167, 192, 223))  

        barSet1 = QBarSet('高层危险行为数量')
        barSet1.append([1, 3, 2, 4, 3, 2, 1, 1, 0, 1, 0, 1])
        barSet1.setColor(QColor(220, 167, 235))  

        # 条状图
        barSeries = QBarSeries()
        barSeries.append(barSet0)
        barSeries.append(barSet1)
        barSeries.setLabelsVisible(True)  # 显示各条形的数据标签

        # 创建图表
        chart = QChart()
        chart.addSeries(barSeries)
        chart.setTitle('高层危险事件分布百分比')
        chart.setAnimationOptions(QChart.SeriesAnimations)  # 添加动画

        # 设置横向坐标(X轴)
        categories = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
        axisX = QBarCategoryAxis()

        # 设置 X 轴标签的字体大小
        font = QFont()
        font.setPixelSize(10)  # 您可以根据需要调整字号大小
        axisX.setLabelsFont(font)

        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        barSeries.attachAxis(axisX)

        # 设置纵向坐标(Y轴)
        axisY = QValueAxis()
        axisY.setRange(0, 4)  # 假设最大事件数为4
        axisY.setLabelFormat("%d")
        axisY.setTitleText("事件数量")
        chart.addAxis(axisY, Qt.AlignLeft)
        barSeries.attachAxis(axisY)

        # 图例属性
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        # 图表视图
        self.ui.graphicsView.setChart(chart)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)


    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("img/8.jpg")
        painter.drawPixmap(self.rect(), pixmap)


    def picture(self):
        i = 0
        for fileName in os.listdir(self.file_name):
            #print(fileName)
            if(i<self.flag*9):
                i=i+1
                continue

            img = cv2.imread(self.file_name + fileName)
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.P[i%9].width(),
                                                                                                   self.P[i%9].height())
            self.P[i%9].setPixmap(QtGui.QPixmap.fromImage(q_image))
            i += 1
            if(i==(self.flag+1)*9):
                self.flag=self.flag+1
                break

    def printf(self):
        self.ui.textBrowser.setFont(QtGui.QFont("Microsoft YaHei", 15))  # 设置一次字体，避免在循环中重复设置

        try:
            # 每次显示3条消息，或者根据文件剩余数量显示更少
            for i in range(3):
                if self.current_index >= len(self.filepath):
                    break  # 如果所有文件都已处理，退出循环

                filename = self.filepath[self.current_index]
                self.current_index += 1
                event_type = random.choice(["高空抛物", "高层危险行为"])
                event_count = 1  # 暂时固定事件数量为1件
                mes = f"{filename} 发生{event_type} {event_count}件"
                self.ui.textBrowser.append(mes)  # 显示事件信息

                cursor = self.ui.textBrowser.textCursor()
                self.ui.textBrowser.moveCursor(cursor.End)
                QtWidgets.QApplication.processEvents()

        except Exception as e:
            print(e)  # 显示异常信息
