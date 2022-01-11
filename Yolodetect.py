# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MFyolo/ui/Yolodetect.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import cv2
import os
import time
import numpy as np
from PIL import Image
from yolo import YOLO
class Ui_Form(object):
    def __init__(self):
        super().__init__()
        #-----------------------#
        # 视频参数设置
        #-----------------------#
        self.video_path = "myVideoSave\origin\TESTroad.mp4"
        self.video_save_path = "myVideoSave\TestF1.mp4"
        self.video_fps       = 25.0
        self.video_width     = 1280
        self.video_Heigth    = 960
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 720)
        self.openBcarmera = QtWidgets.QPushButton(Form)
        self.openBcarmera.setGeometry(QtCore.QRect(40, 660, 111, 41))
        self.openBcarmera.setObjectName("openBcarmera")
        self.startBdetect = QtWidgets.QPushButton(Form)
        self.startBdetect.setGeometry(QtCore.QRect(180, 660, 111, 41))
        self.startBdetect.setObjectName("startBdetect")
        self.label_left = QtWidgets.QLabel(Form)
        self.label_left.setGeometry(QtCore.QRect(20, 190, 420, 380))
        self.label_left.setObjectName("label_left")
        self.label_right = QtWidgets.QLabel(Form)
        self.label_right.setGeometry(QtCore.QRect(490, 190, 420, 380))
        self.label_right.setObjectName("label_right")

        # 定时器设置
        self.timer_camera1 = QtCore.QTimer()
        self.timer_camera2 = QtCore.QTimer()
        self.timer_camera3 = QtCore.QTimer()
        self.timer_camera4 = QtCore.QTimer()
        self.cap = cv2.VideoCapture(self.video_path)
        #定时器信号与槽的连接
        self.timer_camera1.timeout.connect(self.show_camera)
        self.timer_camera2.timeout.connect(self.show_Detected_camera)
        # self.timer_camera3.timeout.connect(self.show_camera2)
        # self.timer_camera4.timeout.connect(self.show_camera2)
        # self.timer_camera4.timeout.connect(self.show_camera3)
        #按钮信号与槽的连接
        self.openBcarmera.clicked.connect(self.button_open_camera_click)
        self.startBdetect.clicked.connect(self.button_detect_camera_click)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YoloV3检测平台"))
        self.openBcarmera.setText(_translate("Form", "打开摄像头"))
        self.startBdetect.setText(_translate("Form", "开始检测"))
        self.label_left.setText(_translate("Form", "TextLabel_left"))
        self.label_right.setText(_translate("Form", "TextLabel_right"))

    def button_open_camera_click(self):
        if self.timer_camera1.isActive() == False:
            flag = self.cap.open(self.video_path)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                self.timer_camera1.start(30)

                self.openBcarmera.setText(u'关闭摄像头')
        else:
            self.timer_camera1.stop()
            self.cap.release()
            self.label_left.clear()
            self.timer_camera2.stop()

            self.label_left.clear()
            self.openBcarmera.setText(u'打开摄像头')
    def show_camera(self):  #摄像头左边
        flag, self.image = self.cap.read()
        if not flag:
            raise ValueError("未能正确读取摄像头（视频），请注意是否正确安装摄像头（是否正确填写视频路径）。")
        
        
        # if self.video_save_path!="":
        #     fourcc  = cv2.VideoWriter_fourcc(*'XVID')
            
            
        #     size    = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        #     out     = cv2.VideoWriter(self.video_save_path, fourcc, self.video_fps, size)
        #-----------------------#
        # 用于保存图像
        #-----------------------#
        # dir_path=os.getcwd()
        # camera_source =dir_path+ "\\data\\test\\2.jpg"
        # cv2.imwrite(camera_source, self.image)
        #------------------------------------------------------------#
        # 设置视频宽高
        #------------------------------------------------------------#
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,self.video_width)
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,self.video_Heigth)
        
        width  = self.cap.get(3)
        height = self.cap.get(4)

        # 设置新的图片分辨率框架
        width_new = 1280
        height_new = 1000

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(self.image, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(self.image, (int(width * height_new / height), height_new))

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],3 * show.shape[1], QtGui.QImage.Format_RGB888)


        self.label_left.setPixmap(QtGui.QPixmap.fromImage(showImage))
    
    def button_detect_camera_click(self):
        if self.timer_camera2.isActive() == False:
            self.yolo = YOLO()
            self.timer_camera2.start(30)
            self.startBdetect.setText(u'停止检测')
        else:
            self.label_right.clear()
            self.timer_camera2.stop()
            self.startBdetect.setText(u'开始检测')
    def show_Detected_camera(self):

        # 转变成Image
        show = Image.fromarray(np.uint8(self.image))
        # 进行检测
        show = np.array(self.yolo.detect_image(show))
        #BGR 转换为 RGB
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],3 * show.shape[1], QtGui.QImage.Format_RGB888)


        self.label_right.setPixmap(QtGui.QPixmap.fromImage(showImage))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #splash = QSplashScreen(QPixmap(".\\data\\source_image\\logo.png"))
    # 设置画面中的文字的字体
    # splash.setFont(QFont('Microsoft YaHei UI', 12))
    # # 显示画面
    # splash.show()
    # # 显示信息
    # splash.showMessage("程序初始化中... 0%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    # time.sleep(0.3)
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Form()
    # splash.showMessage("正在加载模型配置文件...60%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    ui.setupUi(MainWindow)
    # splash.showMessage("正在加载模型配置文件...100%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    # splash.close()
    MainWindow.show() 

    sys.exit(app.exec_())

