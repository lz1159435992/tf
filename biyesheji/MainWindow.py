# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Zheng\PycharmProjects\tf\biyesheji\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon
import collections
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(710, 250, 160, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mr1button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mr1button.setObjectName("mr1button")
        self.verticalLayout.addWidget(self.mr1button)
        self.mr2Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mr2Button.setObjectName("mr2Button")
        self.verticalLayout.addWidget(self.mr2Button)
        self.mr3Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mr3Button.setObjectName("mr3Button")
        self.verticalLayout.addWidget(self.mr3Button)
        self.mr4Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mr4Button.setObjectName("mr4Button")
        self.verticalLayout.addWidget(self.mr4Button)
        self.mr5Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mr5Button.setObjectName("mr5Button")
        self.verticalLayout.addWidget(self.mr5Button)
        self.mr6Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mr6Button.setObjectName("mr6Button")
        self.verticalLayout.addWidget(self.mr6Button)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 78))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 301, 78))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_test = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_test.setObjectName("lineEdit_test")
        self.horizontalLayout_3.addWidget(self.lineEdit_test)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 0, 371, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(710, 0, 160, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_data = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.verticalLayout_2.addWidget(self.lineEdit_data)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.mr1data = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mr1data.setObjectName("mr1data")
        self.verticalLayout_2.addWidget(self.mr1data)
        self.mr2data = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mr2data.setObjectName("mr2data")
        self.verticalLayout_2.addWidget(self.mr2data)
        self.mr3data = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mr3data.setObjectName("mr3data")
        self.verticalLayout_2.addWidget(self.mr3data)
        self.mr4data = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mr4data.setObjectName("mr4data")
        self.verticalLayout_2.addWidget(self.mr4data)
        self.mr5data = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mr5data.setObjectName("mr5data")
        self.verticalLayout_2.addWidget(self.mr5data)
        self.mr6data = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mr6data.setObjectName("mr6data")
        self.verticalLayout_2.addWidget(self.mr6data)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(609, 250, 91, 199))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(620, 460, 239, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.m = PlotCanvas(self, width=6, height=4)  # 实例化一个画布对象
        self.m.move(0, 200)
        self.retranslateUi(MainWindow)
        self.mr1button.clicked.connect(MainWindow.mr1test)
        self.mr2Button.clicked.connect(MainWindow.mr2test)
        self.mr3Button.clicked.connect(MainWindow.mr3test)
        self.mr4Button.clicked.connect(MainWindow.mr4test)
        self.mr5Button.clicked.connect(MainWindow.mr5test)
        self.mr6Button.clicked.connect(MainWindow.mr6test)
        self.pushButton_7.clicked.connect(MainWindow.gefiles)
        self.pushButton_6.clicked.connect(MainWindow.setBrowerPath)
        self.pushButton_10.clicked.connect(MainWindow.setTestPath)
        self.pushButton_9.clicked.connect(MainWindow.setBrowerPath_2)
        self.mr1data.clicked.connect(MainWindow.mr1_data)
        self.mr2data.clicked.connect(MainWindow.mr2_data)
        self.mr3data.clicked.connect(MainWindow.mr3_data)
        self.mr4data.clicked.connect(MainWindow.mr4_data)
        self.mr5data.clicked.connect(MainWindow.mr5_data)
        self.mr6data.clicked.connect(MainWindow.mr6_data)
        self.pushButton_11.clicked.connect(MainWindow.geTestRe)
        self.pushButton.clicked.connect(MainWindow.mr1_result)
        self.pushButton_3.clicked.connect(MainWindow.mr2_result)
        self.pushButton_2.clicked.connect(MainWindow.mr3_result)
        self.pushButton_4.clicked.connect(MainWindow.mr4_result)
        self.pushButton_5.clicked.connect(MainWindow.mr5_result)
        self.pushButton_8.clicked.connect(MainWindow.mr6_result)
        self.pushButton_12.clicked.connect(MainWindow.all_result)
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mr1button.setText(_translate("MainWindow", "mr1测试"))
        self.mr2Button.setText(_translate("MainWindow", "mr2测试"))
        self.mr3Button.setText(_translate("MainWindow", "mr3测试"))
        self.mr4Button.setText(_translate("MainWindow", "mr4测试"))
        self.mr5Button.setText(_translate("MainWindow", "mr5测试"))
        self.mr6Button.setText(_translate("MainWindow", "mr6测试"))
        self.pushButton_6.setText(_translate("MainWindow", "选择目标文件夹"))
        self.pushButton_7.setText(_translate("MainWindow", "生成目录"))
        self.pushButton_10.setText(_translate("MainWindow", "选择测试程序文件夹"))
        self.pushButton_11.setText(_translate("MainWindow", "生成对照数据"))
        self.pushButton_9.setText(_translate("MainWindow", "选择工作目录"))
        self.mr1data.setText(_translate("MainWindow", "mr1蜕变"))
        self.mr2data.setText(_translate("MainWindow", "mr2蜕变"))
        self.mr3data.setText(_translate("MainWindow", "mr3蜕变"))
        self.mr4data.setText(_translate("MainWindow", "mr4蜕变"))
        self.mr5data.setText(_translate("MainWindow", "mr5蜕变"))
        self.mr6data.setText(_translate("MainWindow", "mr6蜕变"))
        self.pushButton.setText(_translate("MainWindow", "mr1测试结果"))
        self.pushButton_3.setText(_translate("MainWindow", "mr2测试结果"))
        self.pushButton_2.setText(_translate("MainWindow", "mr3测试结果"))
        self.pushButton_4.setText(_translate("MainWindow", "mr4测试结果"))
        self.pushButton_5.setText(_translate("MainWindow", "mr5测试结果"))
        self.pushButton_8.setText(_translate("MainWindow", "mr6测试结果"))
        self.pushButton_12.setText(_translate("MainWindow", "所有结果统计"))


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.init_plot()#打开App时可以初始化图片
        #self.plot()

    def plot(self):

        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(100)

    def init_plot(self):
        x = [0]
        y = [0]
        # for (key, value) in re_dict.items():
        #     x.append(key)
        #     y.append(int(value))
        #     print(key + '  :  ' + str(value))
        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        self.axes.plot(x, y)

    def update_figure(self, re_dict):
        """

        :param re_dict:
        """
        x = []
        y = []
        re_dict = collections.OrderedDict(re_dict)
        print('--------------------------------------')
        for (key, value) in re_dict.items():
            x.append(key[0:3] + key[-6:-3])
            y.append(int(value))
            print(key + '  :  ' + str(value))
        self.axes.cla()
        self.axes.plot(x, y)
        # x = np.linspace(0, 10, 10)
        # y = [random.randint(0, 10) for i in range(10)]
        # xx = np.linspace(0, 10)
        # f = interpolate.interp1d(x, y, 'quadratic')  # 产生插值曲线的函数
        # yy = f(xx)

        # self.axes.plot(x, y, 'o',xx,yy)
        self.draw()


class EmittingStr(QtCore.QObject):
        textWritten = QtCore.pyqtSignal(str)  #定义一个发送str的信号
        def write(self, text):
            self.textWritten.emit(str(text))
