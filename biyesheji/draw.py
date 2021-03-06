import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
import random
import numpy as np
from scipy import interpolate


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
        x = []
        y = []
        for (key, value) in re_dict.items():
            x.append(key)
            y.append(int(value))
            print(key + '  :  ' + str(value))
        self.axes.plot(x, y)
        # x = np.linspace(0, 10, 10)
        # y = [random.randint(0, 10) for i in range(10)]
        # xx = np.linspace(0, 10)
        # f = interpolate.interp1d(x, y, 'quadratic')  # 产生插值曲线的函数
        # yy = f(xx)
        # self.axes.cla()
        # self.axes.plot(x, y, 'o',xx,yy)
        self.set_window_title("aaa")
        self.draw()