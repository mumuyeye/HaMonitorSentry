# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Py\demo\step4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#import time
#import sys
#import cv2
from PyQt5.QtChart import QChartView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import (QChartView, QChart, QBarSeries, QBarSet, QLineSeries, QPieSeries,
                           QLegend, QBarCategoryAxis, QValueAxis)
from PyQt5.QtCore import QTimer
import PyQt5

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from detect import detection as det
from PIL import Image

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.Qt import QUrl

import cv2 as cv
import numpy as np
import os
import sys
import xml.dom.minidom as xmldom
import argparse
from nms import py_cpu_nms
import time as T
import re
import linecache
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from utils.torch_utils import select_device, time_sync
from models.common import DetectMultiBackend
from util import plot_one_box, cal_iou, xyxy_to_xywh, xywh_to_xyxy, updata_trace_list, draw_trace
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.augmentations import Albumentations, augment_hsv, copy_paste, letterbox, mixup, random_perspective
from utils.general import (DATASETS_DIR, LOGGER, NUM_THREADS, check_dataset, check_requirements, check_yaml, clean_str,
                           cv2, is_colab, is_kaggle, segments2boxes, xyn2xy, xywh2xyxy, xywhn2xyxy, xyxy2xywhn)
from utils.torch_utils import torch_distributed_zero_first
from pathlib import Path
import ipdb
import shutil

import torch
import torch.backends.cudnn as cudnn


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, md):
        self.frame_s = 2
        self.frame = []  # 存图片
        self.detectFlag = False  # 检测flag
        self.cap = []
        self.timer_camera = QTimer()  # 定义定时器
        self.timer_video = QTimer()
        self.timer_video.timeout.connect(self.show_camera2)
        self.timer_video.timeout.connect(self.show_camera3)
        self.model = md

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #返回主界面
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 165, 45))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFlat(True)
        #h回放抛物信息
        self.show_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_btn.setGeometry(QtCore.QRect(880, 885, 300, 52))
        self.show_btn.setObjectName("pushButton")
        self.show_btn.setFlat(True)
        #视频界面
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(48, 152, 785, 690))
        #self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
#"font: 87 14pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        #视频上传
        self.videoUp = QtWidgets.QPushButton(self.centralwidget)
        self.videoUp.setGeometry(QtCore.QRect(85, 885, 210, 120))
        self.videoUp.setObjectName("videoUp")
        self.videoUp.setFlat(True)
        #算法选择按钮
        self.detect_pushdwon1 = QtWidgets.QPushButton(self.centralwidget)
        self.detect_pushdwon1.setGeometry(QtCore.QRect(75, 67, 220, 65))
        self.detect_pushdwon1.setObjectName(".videoUp")
        self.detect_pushdwon2 = QtWidgets.QPushButton(self.centralwidget)
        self.detect_pushdwon2.setGeometry(QtCore.QRect(360, 120, 180, 52))
        self.detect_pushdwon2.setObjectName(".videoUp")
        self.detect_pushdwon3 = QtWidgets.QPushButton(self.centralwidget)
        self.detect_pushdwon3.setGeometry(QtCore.QRect(572, 120, 180, 52))
        self.detect_pushdwon3.setObjectName(".videoUp")
        self.detect_pushdwon1.setFlat(True)
        self.detect_pushdwon2.setFlat(True)
        self.detect_pushdwon3.setFlat(True)
        #停止监测
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(305, 885, 230, 120))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFlat(True)
        #抛物画面捕捉
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 190, 690, 620))
        #self.label_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        #self.label_3 = QtWidgets.QLabel(self.centralwidget)
        #self.label_3.setGeometry(QtCore.QRect(1250, 100, 250, 30))
        #self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        #                           "font: 87 14pt \"Arial Black\";")
        #self.label_3.setObjectName("label_3")
        #self.label_4 = QtWidgets.QLabel(self.centralwidget)
        #self.label_4.setGeometry(QtCore.QRect(350, 940, 250, 80))
        #self.label_4.setStyleSheet("color: rgb(0, 255, 0);\n"
        #                           "font: 87 14pt \"Arial Black\";")
        #self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(MainWindow.close)
        self.videoUp.clicked.connect(self.slotStart)

        self.detect_pushdwon1.clicked.connect(self.func1)
        self.detect_pushdwon2.clicked.connect(self.func2)
        self.detect_pushdwon3.clicked.connect(self.func3)
        self.pushButton_4.clicked.connect(self.slotStop)
        self.show_btn.clicked.connect(self.show_his)
        self.setWindowIcon(QIcon(os.getcwd() + '/img/logo.ico'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("img/fenxi.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频分析"))
        #self.pushButton.setText(_translate("MainWindow", "返回主界面"))
        #self.label.setText(_translate("MainWindow", "Waiting a video!"))
        #self.videoUp.setText(_translate("MainWindow", "视频上传"))
        #self.detect_pushdwon1.setText(_translate("MainWindow", "MOG2"))
        #self.detect_pushdwon2.setText(_translate("MainWindow", "GMG"))
        #self.detect_pushdwon3.setText(_translate("MainWindow", "KNN"))
        #self.pushButton_4.setText(_translate("MainWindow", "停止监测"))
        #self.label_3.setText(_translate("MainWindow", "抛物画面捕捉"))
        #self.label_4.setText(_translate("MainWindow", "背景建模算法选择"))
        #self.show_btn.setText(_translate("MainWindow", "回放抛物信息"))
   
    def slotStop(self):
        """ Slot function to stop the programme
            """
        if self.cap != []:
            self.cap.release()
            self.timer_camera.stop()  # 停止计时器
            self.label.setText("This video has been closed.")
            self.label.setStyleSheet("QLabel{background:pink;}"
                                     "QLabel{color:rgb(100,100,100);font-size:15px;font-weight:bold;font-family:宋体;}")
            self.cap_video = []
            #self.wid.setText("This video has been stopped.")
            #self.wid.setStyleSheet("QLabel{background:pink;}"
             #                        "QLabel{color:rgb(100,100,100);font-size:15px;font-weight:bold;font-family:宋体;}"
             #                        )
        else:
            #self.label.setText("未输入视频")
            Warming = QMessageBox.warning(self, "Warming", "请先输入要监测的视频！",
                                         QMessageBox.Yes)
        
    
    def slotStart(self):
        self.RemoveDir()
        if self.timer_video.isActive() == False:
            imgName, imgType = QFileDialog.getOpenFileName(self, "打开视频", "", "*.mp4;;*.AVI;;*.rmvb;;All Files(*)")
            self.cap_video = cv.VideoCapture(imgName)
            flag = self.cap_video.isOpened()
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"上传视频识别！",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)       
            else:
                # self.timer_camera3.start(30)
                self.show_camera2()
                self.videoUp.setText(u'关闭视频')
        else:
            # self.timer_camera3.stop()
            self.cap_video.release()
            self.label.clear()
            self.timer_video.stop()
            self.frame_s=3
            self.label_2.clear()
            self.videoUp.setText(u'打开视频')

    def func1(self):
        self.model.alt("MOG2")
        self.detection()

    def func2(self):
        self.model.alt("GMG")
        self.detection()

    def func3(self):
        self.model.alt("KNN")
        self.detection()

    def detection(self):

            if self.timer_video.isActive() == False:
                flag = self.cap_video.isOpened()
                if flag == False:
                    msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

                else:
                    self.timer_video.start(30)

            else:
                self.timer_video.stop()
                self.cap_video.release()
                self.label_2.clear()


    def show_camera2(self):     #显示视频的左边

                  #抽帧
        length = int(self.cap_video.get(cv.CAP_PROP_FRAME_COUNT))   #抽帧
        #print(self.frame_s,length) #抽帧
        flag, self.image1 = self.cap_video.read()   #image1是视频的
        if flag == True:
            if self.frame_s%3==0:  #抽帧
                #dir_path=os.getcwd()
                # print("dir_path",dir_path)
                #camera_source =dir_path+ "\\data\\test\\video.jpg"
                #cv.imwrite(camera_source, self.image1)
                
                frame = cv.cvtColor(self.image1, cv.COLOR_BGR2RGB)
                height, width, bytesPerComponent = self.image1.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                self.label.setPixmap(QtGui.QPixmap.fromImage(q_image))
                
                
        else:
            self.cap_video.release()
            self.label.clear()
            self.timer_video.stop()
            self.output_video()
            self.label_2.clear()
            self.videoUp.setText(u'打开视频')

    def show_camera3(self):

        flag, self.image1 = self.cap_video.read()
        self.frame_s += 1
        if flag==True:
            if self.frame_s % 3 == 0:   #抽帧
                # face = self.face_detect.align(self.image)
                # if face:
                #     pass

                #dir_path = os.getcwd()
                #camera_source = dir_path + "\\data\\test\\video.jpg"

                #cv.imwrite(camera_source, self.image1)
                # print("im01")
                
                #while True:
                    #rval, frame = self.cap_video.read()
                    #if frame is None:
                    #    break

                    #fgMask = self.model.backSub.apply(frame)

                    fgMask = self.model.backSub.apply(self.image1)
                    fgMask = cv.cvtColor(fgMask, cv.COLOR_GRAY2RGB)

                    frame1 = self.image1
                    frame2 = self.image1
                    self.model.framenum = self.model.framenum + 1
                    img = letterbox(self.image1, self.model.imgsz, stride=self.model.stride, auto=True)[0]
                    mask = letterbox(fgMask, self.model.imgsz, stride=self.model.stride, auto=True)[0]
                    # Convert
                    img = np.concatenate((img, mask), axis=2)
                    mask = mask.transpose((2, 0, 1))[::-1]
                    img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
                    mask = np.ascontiguousarray(mask)
                    img = np.ascontiguousarray(img)
                    ma = mask
                    im = img
                    ma = torch.from_numpy(ma).to(self.model.device)
                    im = torch.from_numpy(im).to(self.model.device)
                    ma = ma.half() if self.model.fp16 else ma.float()
                    im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
                    ma /= 255
                    im /= 255  # 0 - 255 to 0.0 - 1.0
                    if len(im.shape) == 3:
                        im = im[None]  # expand for batch dim
                        ma = ma[None]

                    # example shape of img(torch.Size([1, 3, 384, 640]))
                    # slice_img = []

                    pred = self.model.model(im, ma, augment=False, visualize=False)
                    # pred shape[1, x, 6]
                    pred = non_max_suppression(pred, self.model.conf_thres, self.model.iou_thres, classes=None, agnostic=False, max_det=50)

                    # import ipdb
                    bounds = []
                    for i, det in enumerate(pred):
                        im0 = self.image1.copy()
                        gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]

                        if len(det):
                            initial = True
                            det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                            #print(det)
                            #print("1")

                            for *xyxy, conf, cls in reversed(det):
                                bounds.append((torch.tensor(xyxy).view(1, 4)).view(-1).tolist())

                    for box in bounds:
                        frame1 = cv.rectangle(frame1, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), color=self.model.box_color,
                              thickness=1)
                        visual_file_root = os.path.join("video","1")
                        if not os.path.exists(visual_file_root):
                            os.mkdir(visual_file_root)
                        visual_file = os.path.join(visual_file_root,"detframe{}.jpg".format(self.model.framenum))
                        cv.imwrite(visual_file, frame1)

                    video_out_root = os.path.join("video", "2")
                    if not os.path.exists(video_out_root):
                        os.mkdir(video_out_root)
                    video_out = os.path.join(video_out_root,"outframe{}.jpg".format(self.frame_s))
                    cv.imwrite(video_out, frame1)

                    height, width, bytesPerComponent = self.image1.shape
                    bytesPerLine = bytesPerComponent * width
                    q_image = QImage(self.image1.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.label_2.width(), self.label_2.height())
                #print(f"self.video_box.width:{self.video_box.width()}, self.label.width():{self.label.width()}")
                #q_image = QImage(frame.data, width, height, bytesPerLine,
                #                 QImage.Format_RGB888).scaled(self.video_box.width(), self.video_box.height())

                    self.label_2.setPixmap(QPixmap.fromImage(q_image))

    def output_video(self):
        im_dir = os.path.join("video", "2/")
        im_list = os.listdir(im_dir)
        im_list.sort(key=lambda x: x.split('.')[0])
        img = Image.open(os.path.join(im_dir, im_list[0]))
        img_size = img.size
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_dir = os.path.join("video", "3", "out1.mp4")
        videoWriter = cv2.VideoWriter(video_dir, fourcc, 24, img_size)
        # count = 1
        for i in im_list:
            im_name = os.path.join(im_dir + i)
            frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
            videoWriter.write(frame)
        videoWriter.release()
        print('finish video_output')

    def show_his(self):
        video = cv2.VideoCapture("video/3/out1.mp4")
        if not video.isOpened():
            print("Could not open video")
            sys.exit()
        
        plt.ion()  # 开启交互模式
        # 调整 figsize 参数以改变窗口大小
        figure, ax = plt.subplots(figsize=(10, 6))  # 这里的数值可以根据需要调整
        ax.axis('off')  # 去除坐标轴
        figure.canvas.set_window_title('回放抛物信息')

        # 调整布局参数以减少留白
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

        while True:
            ok, frame = video.read()
            if ok:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 转换颜色空间
                if 'display_image' in locals():  # 如果display_image已定义，则更新数据
                    display_image.set_data(frame)
                else:
                    display_image = ax.imshow(frame, aspect='auto')  # 首次显示图像，铺满整个页面
                plt.pause(0.1)  # 设置暂停时间

                if plt.waitforbuttonpress(0.1):
                    break  # 如果在0.1秒内有按键则退出循环
            else:
                print('failed')
                break

        video.release()
        plt.ioff()  # 关闭交互模式
        plt.show()

    def RemoveDir(filepath):
        '''
        如果文件夹不存在就创建，如果文件存在就清空！
        '''
        filepath = "video/2"
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        else:
            shutil.rmtree(filepath)
            os.mkdir(filepath)
