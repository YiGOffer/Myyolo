# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MFyolo\ui\YOLOdetect_2.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import cv2
import os
import time
import numpy as np
from PIL import Image
from nets.yolo import YoloBody
from yolo import YOLO

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1420, 716)
        self.label_left = QtWidgets.QLabel(Form)
        self.label_left.setGeometry(QtCore.QRect(10, 30, 700, 320))
        self.label_left.setObjectName("label_left")
        self.label_right = QtWidgets.QLabel(Form)
        self.label_right.setGeometry(QtCore.QRect(710, 30, 700, 320))
        self.label_right.setObjectName("label_right")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 370, 841, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("华光楷体一_CNKI")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.open_weight_path = QtWidgets.QLineEdit(self.groupBox)
        self.open_weight_path.setGeometry(QtCore.QRect(170, 30, 561, 20))
        self.open_weight_path.setObjectName("open_weight_path")
        self.select_weith_pth_button = QtWidgets.QPushButton(self.groupBox)
        self.select_weith_pth_button.setGeometry(QtCore.QRect(740, 30, 71, 20))
        self.select_weith_pth_button.setObjectName("select_weith_pth_button")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(30, 80, 681, 71))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.open_camera_button = QtWidgets.QPushButton(self.tab)
        self.open_camera_button.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.open_camera_button.setObjectName("open_camera_button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.open_video_path = QtWidgets.QLineEdit(self.tab_2)
        self.open_video_path.setGeometry(QtCore.QRect(70, 20, 401, 20))
        self.open_video_path.setObjectName("open_video_path")
        self.open_video_button = QtWidgets.QPushButton(self.tab_2)
        self.open_video_button.setGeometry(QtCore.QRect(490, 20, 71, 20))
        self.open_video_button.setObjectName("open_video_button")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("华光楷体一_CNKI")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.start_video_button = QtWidgets.QPushButton(self.tab_2)
        self.start_video_button.setGeometry(QtCore.QRect(580, 0, 91, 41))
        self.start_video_button.setObjectName("start_video_button")
        self.tabWidget.addTab(self.tab_2, "")
        self.start_YOLOdetect_button = QtWidgets.QPushButton(self.groupBox)
        self.start_YOLOdetect_button.setGeometry(QtCore.QRect(730, 100, 91, 41))
        self.start_YOLOdetect_button.setObjectName("start_YOLOdetect_button")
        self.open_classes_path = QtWidgets.QLineEdit(self.groupBox)
        self.open_classes_path.setGeometry(QtCore.QRect(170, 60, 561, 20))
        self.open_classes_path.setObjectName("open_classes_path")
        self.select_classes_txt_button = QtWidgets.QPushButton(self.groupBox)
        self.select_classes_txt_button.setGeometry(QtCore.QRect(740, 60, 71, 20))
        self.select_classes_txt_button.setObjectName("select_classes_txt_button")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("华光楷体一_CNKI")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.raise_()
        self.label_3.raise_()
        self.open_weight_path.raise_()
        self.select_weith_pth_button.raise_()
        self.start_YOLOdetect_button.raise_()
        self.open_classes_path.raise_()
        self.select_classes_txt_button.raise_()
        self.label_7.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 530, 841, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 151, 21))
        font = QtGui.QFont()
        font.setFamily("华光楷体一_CNKI")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pretrain_document_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.pretrain_document_path.setGeometry(QtCore.QRect(180, 30, 561, 20))
        self.pretrain_document_path.setObjectName("pretrain_document_path")
        self.data_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.data_path.setGeometry(QtCore.QRect(180, 70, 561, 20))
        self.data_path.setObjectName("data_path")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 151, 21))
        font = QtGui.QFont()
        font.setFamily("华光楷体一_CNKI")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.select_pretrain_pth_button = QtWidgets.QPushButton(self.groupBox_2)
        self.select_pretrain_pth_button.setGeometry(QtCore.QRect(750, 30, 71, 20))
        self.select_pretrain_pth_button.setObjectName("select_pretrain_pth_button")
        self.select_vocdata_button = QtWidgets.QPushButton(self.groupBox_2)
        self.select_vocdata_button.setGeometry(QtCore.QRect(750, 70, 71, 20))
        self.select_vocdata_button.setObjectName("select_vocdata_button")
        self.start_train_button = QtWidgets.QPushButton(self.groupBox_2)
        self.start_train_button.setGeometry(QtCore.QRect(710, 110, 111, 31))
        self.start_train_button.setObjectName("start_train_button")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(870, 370, 511, 311))
        self.textEdit.setObjectName("textEdit")

        # 定时器设置
        self.timer_camera1 = QtCore.QTimer()#摄像头显示
        self.timer_camera2 = QtCore.QTimer()#检测画面显示
        self.timer_camera3 = QtCore.QTimer()#视频显示 
        # 摄像头对象创建
        self.cap = cv2.VideoCapture(0)
        #定时器信号与槽的连接
        self.timer_camera1.timeout.connect(self.show_camera)
        self.timer_camera3.timeout.connect(self.show_video)
        self.timer_camera2.timeout.connect(self.show_Detected_camera)
        #按钮信号与槽的连接
        self.open_camera_button.clicked.connect(self.button_open_camera_click)
        self.start_YOLOdetect_button.clicked.connect(self.button_detect_camera_click)
        self.open_video_button.clicked.connect(self.open_select_video_click)
        self.start_video_button.clicked.connect(self.button_open_videoPath_click)
        self.select_weith_pth_button.clicked.connect(self.open_select_weight_click)
        self.select_classes_txt_button.clicked.connect(self.open_select_classes_txt_click)
        # yolo对象创建
        self.yolo = YOLO()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YoloV3训练检测平台"))
        self.label_left.setText(_translate("Form", "等待摄像头连接。。。"))
        self.label_right.setText(_translate("Form", "等待开始检测。。。"))
        self.groupBox.setTitle(_translate("Form", "检测操作区"))
        self.label_3.setText(_translate("Form", "权重文件路径："))
        self.select_weith_pth_button.setText(_translate("Form", "浏览"))
        self.open_camera_button.setText(_translate("Form", "打开摄像头"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "检测摄像头画面"))
        self.open_video_button.setText(_translate("Form", "浏览"))
        self.label_6.setText(_translate("Form", "视频路径："))
        self.start_video_button.setText(_translate("Form", "打开视频"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "检测视频画面"))
        self.start_YOLOdetect_button.setText(_translate("Form", "开始YOLO检测"))
        self.select_classes_txt_button.setText(_translate("Form", "浏览"))
        self.label_7.setText(_translate("Form", "classes.txt文件路径："))
        self.groupBox_2.setTitle(_translate("Form", "训练操作区"))
        self.label_4.setText(_translate("Form", "预训练权重文件路径："))
        self.label_5.setText(_translate("Form", "数据集路径："))
        self.select_pretrain_pth_button.setText(_translate("Form", "浏览"))
        self.select_vocdata_button.setText(_translate("Form", "浏览"))
        self.start_train_button.setText(_translate("Form", "开始训练"))
    
    def open_select_weight_click(self):
        _translate = QtCore.QCoreApplication.translate
        self.directory_weight = QFileDialog.getOpenFileName(None, "选择文件", "H:/")
        weight_path = self.directory_weight[0]
        self.yolo._defaults["model_path"]=weight_path
        self.open_weight_path.setText(_translate("Form", weight_path))
        # if(self.open_classes_path.text() != '' and self.open_weight_path.text()!='' ):
        #     self.yolo.yoloinit()
        # else:
        #     #-------------在文本框显示信息-----------待补充----#
        #     self.textEdit.append('未成功生成yolo模型。。。请检查是否选择了权重文件或者classes.txt文件路径')
        #     return

    def open_select_classes_txt_click(self):
        _translate = QtCore.QCoreApplication.translate
        self.directory_classes = QFileDialog.getOpenFileName(None, "选择文件", "H:/")
        classes_path = self.directory_classes[0]
        self.yolo._defaults["classes_path"]=classes_path
        self.open_classes_path.setText(_translate("Form", classes_path))
        # if(self.open_classes_path.text() != '' and self.open_weight_path.text()!='' ):
        #     self.yolo.yoloinit()
        # else:
        #     #-------------在文本框显示信息-----------待补充----#
        #     self.textEdit.append('未成功生成yolo模型。。。请检查是否选择了权重文件或者classes.txt文件路径')
        #     return
        
        
    def open_select_video_click(self):
        _translate = QtCore.QCoreApplication.translate
        self.directory1 = QFileDialog.getOpenFileName(None, "选择文件", "H:/")
        self.video_path = self.directory1[0]
        self.open_video_path.setText(_translate("Form", self.video_path))

    def button_open_videoPath_click(self):
        self.timer_camera1.stop()
        self.label_left.clear()
        video_path = self.open_video_path.text()
        if self.timer_camera3.isActive() == False:
            flag = self.cap.open(video_path)
            if flag == False:
                self.textEdit.append('打开视频失败！请检查视频路径是否正确！')
            else:
                
                self.timer_camera3.start(30)
                self.start_video_button.setText(u'关闭视频')
        else:
            
            self.timer_camera2.stop()
            self.label_right.clear()
            self.timer_camera3.stop()
            self.timer_camera1.stop()
            self.label_left.clear()
            video_path = ''
            self.start_video_button.setText(u'打开视频')
            self.start_YOLOdetect_button.setText(u'开始YOLO检测')
            self.open_camera_button.setText(u'打开摄像头')


    def button_open_camera_click(self):
        self.timer_camera3.stop()
        self.label_left.clear()
        self.video_path = 0
        if self.timer_camera1.isActive() == False:
            flag = self.cap.open(self.video_path)
            if flag == False:
                self.textEdit.append('打开相机失败！请检测相机与电脑是否连接正确！')
            else:
                self.timer_camera1.start(30)
                self.open_camera_button.setText(u'关闭摄像头')
        else:
            self.timer_camera2.stop()
            self.label_right.clear()
            self.timer_camera1.stop()
            self.label_left.clear()
            self.open_camera_button.setText(u'打开摄像头')
    def show_video(self):   #左边显示视频画面
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
        width_new = 700
        height_new = 320

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(self.image, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(self.image, (int(width * height_new / height), height_new))

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],3 * show.shape[1], QtGui.QImage.Format_RGB888)


        self.label_left.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def show_camera(self):  #左边显示摄像头画面
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
        width_new = 700
        height_new = 320

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = cv2.resize(self.image, (width_new, int(height * width_new / width)))
        else:

            show = cv2.resize(self.image, (int(width * height_new / height), height_new))

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],3 * show.shape[1], QtGui.QImage.Format_RGB888)


        self.label_left.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def button_detect_camera_click(self):
        if  self.timer_camera1.isActive() == False or self.timer_camera3.isActive() == False :
            self.textEdit.append('未获取到图像源，请检查视频或摄像头是否打开')
            return 
        elif self.open_classes_path.text() == '' or self.open_weight_path.text() =='':
            self.textEdit.append('未成功生成yolo模型。。。请检查是否选择了权重文件或者classes.txt文件路径')
            return
        elif self.timer_camera2.isActive() == False:
            self.yolo.yoloinit()
            self.timer_camera2.start(30)
            self.start_YOLOdetect_button.setText(u'停止YOLO检测')
        else:
            self.timer_camera2.stop()
            self.label_right.clear()
            self.timer_camera1.stop()
            self.label_left.clear()
            self.start_YOLOdetect_button.setText(u'开始YOLO检测')
            self.open_camera_button.setText(u'打开摄像头')
            self.start_video_button.setText(u'打开视频')
            
    def show_Detected_camera(self):
        
        # 格式转变，BGRtoRGB
        frame = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        # 进行检测
        frame = np.array(self.yolo.detect_image(frame))
        # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        
        # 单独窗口
        #cv2.imshow("Detect",frame)
            
        # 显示到右边窗口
        width  = self.cap.get(3)
        height = self.cap.get(4)

        # 设置新的图片分辨率框架
        width_new = 700
        height_new = 320

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            frame = cv2.resize(frame, (width_new, int(height * width_new / width)))
        else:

            frame = cv2.resize(frame, (int(width * height_new / height), height_new))

        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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