import sys
import gc
from MainWindow import Ui_MainWindow

import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import data
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
import datetime
import collections

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from childWindow import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox, QPushButton, QTableView, QLabel, QHeaderView, QVBoxLayout


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    signal = pyqtSignal(dict, str)
    all_signal = pyqtSignal(list, list)
    #all_signal = pyqtSignal(dict, dict, dict, dict, dict, dict, dict, dict, str, str, str, str, str, str, str, str)

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def mr1test(self):
        starttime = datetime.datetime.now()
        a = data.testingmr1_(self.lineEdit_data.text())
        if a == 0:
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr1测试完成,用时"+timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr2test(self):
        starttime = datetime.datetime.now()
        a = data.testingmr2_(self.lineEdit_data.text())
        print(a)
        if a == 0:
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr2测试完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr3test(self):
        starttime = datetime.datetime.now()
        a = data.testingmr3_(self.lineEdit_data.text())
        print(a)
        if a == 0:
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr3测试完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr4test(self):
        starttime = datetime.datetime.now()
        a = data.testingmr4_(self.lineEdit_data.text())
        print(a)
        if a == 0:
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr4测试完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr5test(self):
        starttime = datetime.datetime.now()
        a = data.testingmr5_(self.lineEdit_data.text())
        print(a)
        if a == 0:
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr5测试完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr6test(self):
        starttime = datetime.datetime.now()
        a = data.testingmr6_(self.lineEdit_data.text())
        print(a)
        if a == 0:
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr6测试完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr1_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = data.readmr_(1, self.lineEdit_data.text())
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def mr2_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = data.readmr_(2, self.lineEdit_data.text())
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def mr3_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = data.readmr_(3, self.lineEdit_data.text())
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def mr4_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = data.readmr_(4, self.lineEdit_data.text())
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def mr5_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = data.readmr_(5, self.lineEdit_data.text())
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def mr6_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = data.readmr_(6, self.lineEdit_data.text())
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def all_result(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            re_dict = {}
            re_dict1 = data.readmr_(1, self.lineEdit_data.text())
            re_dict2 = data.readmr_(2, self.lineEdit_data.text())
            re_dict3 = data.readmr_(3, self.lineEdit_data.text())
            re_dict4 = data.readmr_(4, self.lineEdit_data.text())
            re_dict5 = data.readmr_(5, self.lineEdit_data.text())
            re_dict6 = data.readmr_(6, self.lineEdit_data.text())
            list = []
            list.append(re_dict1)
            list.append(re_dict2)
            list.append(re_dict3)
            list.append(re_dict4)
            list.append(re_dict5)
            list.append(re_dict6)
            for i in list:
                if i:
                    for (key, value) in i.items():
                        if key not in re_dict:
                            re_dict[key] = value
                        else:
                            re_dict[key] = re_dict[key] + value
            re_dict = collections.OrderedDict(re_dict)
            self.m.update_figure(re_dict)

    def mr1_data(self):
        starttime = datetime.datetime.now()
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            data.allmr1_(self.lineEdit_data.text())
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr1蜕变完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr2_data(self):
        starttime = datetime.datetime.now()
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            data.allmr2_(self.lineEdit_data.text())
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr2蜕变完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr3_data(self):
        starttime = datetime.datetime.now()
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            data.allmr3_(self.lineEdit_data.text())
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr3蜕变完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr4_data(self):
        starttime = datetime.datetime.now()
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            data.allmr4_(self.lineEdit_data.text())
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr4蜕变完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr5_data(self):
        starttime = datetime.datetime.now()
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            data.allmr5_(self.lineEdit_data.text())
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr5蜕变完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def mr6_data(self):
        starttime = datetime.datetime.now()
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # print(reply)
            # self.echo(reply)
        else:
            data.allmr6_(self.lineEdit_data.text())
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self, "提示", "mr6蜕变完成,用时" + timeStr, QMessageBox.Yes | QMessageBox.No)

    def outputWritten(self, text):  # 输出控制台信息
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def setTestPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "C:\\")
        self.lineEdit_test.setText(download_path)

    def geTestRe(self):
        if not self.lineEdit_data.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "工作路径为空。", QMessageBox.Yes | QMessageBox.No)
            # self.pu = QPushButton(self)
            # self.pu.setText('sdf')
            # self.pu.setVisible(True)
            # self.pu.setGeometry(50,50, 100, 50)
            # self.gridLayout.addWidget(self.pu)
            # self.gridlayout.addWidget(self.pu)
            if self.lineEdit_test.text().strip():
                for dirpath, dirnames, filenames in os.walk(self.lineEdit_test.text()):
                    i = 0
                    self.varList = filenames
                    for filepath in filenames:
                        self.varList[i] = QPushButton(self)
                        self.varList[i].setText(str(filepath)[0:3] + str(filepath)[-6:-3])
                        self.varList[i].setVisible(True)
                        if str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOD139':
                            self.varList[i].clicked.connect(lambda: self.AOD139())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOD149':
                            self.varList[i].clicked.connect(lambda: self.AOD149())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOR729':
                            self.varList[i].clicked.connect(lambda: self.AOR729())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOR738':
                            self.varList[i].clicked.connect(lambda: self.AOR738())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'ASR189':
                            self.varList[i].clicked.connect(lambda: self.ASR189())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'ASR200':
                            self.varList[i].clicked.connect(lambda: self.ASR200())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'CRP537':
                            self.varList[i].clicked.connect(lambda: self.CRP537())
                        elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'CRP549':
                            self.varList[i].clicked.connect(lambda: self.CRP549())
                        # self.varList[i].clicked.connect(str(filepath)[0:3] + str(filepath)[-6:-3])
                        self.varList[i].setGeometry(50, 50, 100, 50)
                        self.gridLayout.addWidget(self.varList[i], int(i / 3), (i - 3 * int(i / 3)))
                        i = i + 1
                self.soft_result = QPushButton(self)
                self.soft_result.setText('展示所有结果')
                self.soft_result.setVisible(True)
                self.soft_result.clicked.connect(lambda: self.allsoft_result())
                self.soft_result.setGeometry(50, 50, 100, 50)
                self.gridLayout.addWidget(self.soft_result, int(i / 3), (i - 3 * int(i / 3)))
                reply = QMessageBox.information(self, "提示", "生成程序信息按钮", QMessageBox.Yes | QMessageBox.No)
        elif not self.lineEdit_test.text().strip():
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            starttime = datetime.datetime.now()
            for dirpath, dirnames, filenames in os.walk(self.lineEdit_test.text()):
                i = 0
                self.varList = filenames
                for filepath in filenames:
                    self.varList[i] = QPushButton(self)
                    self.varList[i].setText(str(filepath)[0:3] + str(filepath)[-6:-3])
                    self.varList[i].setVisible(True)
                    if str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOD139':
                        self.varList[i].clicked.connect(lambda: self.AOD139())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOD149':
                        self.varList[i].clicked.connect(lambda: self.AOD149())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOR729':
                        self.varList[i].clicked.connect(lambda: self.AOR729())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOR738':
                        self.varList[i].clicked.connect(lambda: self.AOR738())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'ASR189':
                        self.varList[i].clicked.connect(lambda: self.ASR189())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'ASR200':
                        self.varList[i].clicked.connect(lambda: self.ASR200())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'CRP537':
                        self.varList[i].clicked.connect(lambda: self.CRP537())
                    elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'CRP549':
                        self.varList[i].clicked.connect(lambda: self.CRP549())
                    # self.varList[i].clicked.connect(str(filepath)[0:3] + str(filepath)[-6:-3])
                    self.varList[i].setGeometry(50, 50, 100, 50)
                    self.gridLayout.addWidget(self.varList[i], int(i / 3), (i - 3 * int(i / 3)))
                    i = i + 1
            self.soft_result = QPushButton(self)
            self.soft_result.setText('展示所有结果')
            self.soft_result.setVisible(True)
            self.soft_result.clicked.connect(lambda: self.allsoft_result())
            self.soft_result.setGeometry(50, 50, 100, 50)
            self.gridLayout.addWidget(self.soft_result, int(i / 3), (i - 3 * int(i / 3)))
            #reply = QMessageBox.information(self, "提示", "生成程序信息按钮", QMessageBox.Yes | QMessageBox.No)
            #生成对照的测试数据
            data.gettest_(self.lineEdit_data.text(), self.lineEdit_test.text())
            #计算时间
            endtime = datetime.datetime.now()
            seconds = (endtime - starttime).seconds
            start = starttime.strftime('%Y-%m-%d %H:%M')
            # 100 秒
            # 分钟
            minutes = seconds // 60
            second = seconds % 60
            print((endtime - starttime))
            timeStr = str(minutes) + '分钟' + str(second) + "秒"
            print("程序从 " + start + ' 开始运行,运行时间为：' + timeStr)
            reply = QMessageBox.information(self,
                                            "提示",
                                            "对照数据生成完成，程序信息按钮生成完成，用时：" + timeStr,
                                            QMessageBox.Yes | QMessageBox.No)
        # for dirpath, dirnames, filenames in os.walk(self.lineEdit_test.text()):
        #     i = 0
        #     self.varList = filenames
        #     for filepath in filenames:
        #         self.varList[i] = QPushButton(self)
        #         self.varList[i].setText(str(filepath)[0:3] + str(filepath)[-6:-3])
        #         self.varList[i].setVisible(True)
        #         if str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOD139':
        #             self.varList[i].clicked.connect(lambda: self.AOD139())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOD149':
        #             self.varList[i].clicked.connect(lambda: self.AOD149())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOR729':
        #             self.varList[i].clicked.connect(lambda: self.AOR729())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'AOR738':
        #             self.varList[i].clicked.connect(lambda: self.AOR738())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'ASR189':
        #             self.varList[i].clicked.connect(lambda: self.ASR189())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'ASR200':
        #             self.varList[i].clicked.connect(lambda: self.ASR200())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'CRP537':
        #             self.varList[i].clicked.connect(lambda: self.CRP537())
        #         elif str(filepath)[0:3] + str(filepath)[-6:-3] == 'CRP549':
        #             self.varList[i].clicked.connect(lambda: self.CRP549())
        #         # self.varList[i].clicked.connect(str(filepath)[0:3] + str(filepath)[-6:-3])
        #         self.varList[i].setGeometry(50, 50, 100, 50)
        #         self.gridLayout.addWidget(self.varList[i], int(i / 3), (i - 3 * int(i / 3)))
        #         i = i + 1
        # self.soft_result = QPushButton(self)
        # self.soft_result.setText('展示所有结果')
        # self.soft_result.setVisible(True)
        # self.soft_result.clicked.connect(lambda: self.allsoft_result())
        # self.soft_result.setGeometry(50, 50, 100, 50)
        # self.gridLayout.addWidget(self.soft_result, int(i / 3), (i - 3 * int(i / 3)))
        # # self.pu = QPushButton(self)
        # # self.pu.setText('sdf')
        # # self.pu.setVisible(True)
        # # self.pu.setGeometry(50,50, 100, 50)
        # # self.gridLayout.addWidget(self.pu)
        # # self.gridlayout.addWidget(self.pu)

    def AOD139(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOD139':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)
            # self.child.tableView.setModel(self.model)
            # child_ui = Ui_Dialog()
            # child_ui.trantable(self.model)

            # self.child.tableshow()
            # self.model = QStandardItemModel(8, 2)
            # self.model.setHorizontalHeaderLabels(['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6'])
            # for row in range(8):
            #     for column in range(2):
            #         item = QStandardItem('aaa')
            #         self.model.setItem(row, column, item)
            # # self.child.label = QLabel()
            # # self.child.label.setText('AAAA')
            # self.child.tableView = QTableView()
            # self.child.tableView.setModel(self.model)
            # self.child.tableView.setAlignment(QtCore.Qt.AlignCenter)
            # self.child.tableView.setVisible(True)
            # #self.child.tableView.setObjectName("aaaaaa")
            # # self.child.tableView.setObjectName("aaaaaa")
            # self.child.tableshow()
            # 对话框

            # dictsignal = pyqtSignal(dict)
            # child.show()

    def AOD149(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOD149':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def AOR729(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOR729':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            print(dict_)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def AOR738(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOR738':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def ASR189(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'ASR189':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def ASR200(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'ASR200':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def CRP537(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'CRP537':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def CRP549(self):
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'CRP549':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            dict_ = collections.OrderedDict(dict_)
            for (key, value) in dict_.items():
                print(key + '  :  ' + str(value))
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict_
            self.signal.connect(self.child.tableshow)
            self.signal.emit(dict_, name)

    def allsoft_result(self):
        print("www")
        if not self.lineEdit_test.text().strip():
            # tk.messagebox.showwarning("警告", '工作路径为空！')
            # tk.mainloop()
            reply = QMessageBox.warning(self, "警告", "程序测试路径为空。", QMessageBox.Yes | QMessageBox.No)
        else:
            filepath = self.lineEdit_test.text()
            lines = filepath.split('/')
            filepath = ''
            dict_ = {}
            dict_list = []
            name_list = []
            name = ''
            list = ['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6']
            # 1 AOD139
            for i in range(len(lines) - 1):
                if i == 0:
                    filepath = filepath + lines[i]
                else:
                    filepath = filepath + '\\' + lines[i]
            filepath = filepath + '\\data'
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOD139':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 2 AOD149
            name = ''
            dict_ = {}
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOD149':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 3 AOR729
            dict_ = {}
            name = ''
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOR729':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 4 AOR738
            name = ''
            dict_ = {}
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'AOR738':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 5 ASR189
            dict_ = {}
            name = ''
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'ASR189':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 6 ASR200
            dict_ = {}
            name = ''
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'ASR200':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 7 CRP537
            dict_ = {}
            name = ''
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'CRP537':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # 8 CRP549
            name = ''
            dict_ = {}
            for i in range(6):
                dict_['mr' + str(i + 1)] = 0
                if not os.path.exists(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy'):
                    continue
                    # np.save(filepath + '\\mr' + str(i) + '\\mr_result.npy', re_dict)
                else:
                    re_dict = np.load(filepath + '\\mr' + str(i + 1) + '\\mr_result.npy', allow_pickle = True).item()
                    for (key, value) in re_dict.items():
                        lines = key.split('+')
                        if (lines[0][0:3] + lines[0][-6:-3]) == 'CRP549':
                            name = lines[0]
                            dict_[list[i]] = dict_[list[i]] + value
            if dict_:
                dict_ = collections.OrderedDict(dict_)
                dict_list.append(dict_)
                name_list.append(name)
            print(dict_)
            if not os.path.exists(filepath + '\\' + name):
                os.makedirs(filepath + '\\' + name)
            if not os.path.exists(filepath + '\\' + name + '\\dict.npy'):
                np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            np.save(filepath + '\\' + name + '\\dict.npy', dict_)
            # self.child = QDialog()
            self.child = ChildWindow()
            child_ui = Ui_Dialog()
            child_ui.setupUi(self.child)
            self.child.show()
            # 发射信号 传递字典dict list
            self.all_signal.connect(self.child.all_tableshow)
            self.all_signal.emit(dict_list, name_list)
            #self.all_signal.emit(dict_list[0], dict_list[1], dict_list[2], dict_list[3], dict_list[4], dict_list[5], dict_list[6], dict_list[7], name_list[0], name_list[1], name_list[2], name_list[3], name_list[4], name_list[5], name_list[6], name_list[7])
            # self.signal.connect(self.child.tableshow)
            # self.signal.emit(dict_, name)

    def setFilePath(self):  # 获取文件路径  暂时未使用，留作备用
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.lineEdit_file.setText(file_path)

    def setBrowerPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "C:\\")
        self.lineEdit.setText(download_path)

    def setBrowerPath_2(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "C:\\")
        self.lineEdit_data.setText(download_path)

    def gefiles(self):
        filed = self.lineEdit.text()
        print(filed[-1:])
        if filed[-1:] is not '/':
            filed = filed + '/'
        print(filed)
        if not os.path.exists(filed + 'biyesheji/'):  # 若不存在路径则创建
            os.makedirs(filed + 'biyesheji/')
        if not os.path.exists(filed + 'biyesheji/data/'):  # 若不存在路径则创建
            os.makedirs(filed + 'biyesheji/data/')
        if not os.path.exists(filed + 'biyesheji/code/'):  # 若不存在路径则创建
            os.makedirs(filed + 'biyesheji/code/')
        if not os.path.exists(filed + 'biyesheji/code_test/'):  # 若不存在路径则创建
            os.makedirs(filed + 'biyesheji/code_test/')
        filed = filed + 'biyesheji/data/'
        read_dictionary = {}
        for x in range(1, 7):
            if not os.path.exists(filed + '\\mr' + str(x)):
                os.makedirs(filed + '\\mr' + str(x))
            elif not os.path.exists(filed + '\\mr' + str(x) + '\\result.npy'):
                np.save(filed + '\\mr' + str(x) + '\\result.npy', read_dictionary)
        print(filed)
        # root = tk.Tk()
        # root.withdraw()
        # file_path = filedialog.askopenfilename()
        #a = data.gedata()
        a = np.loadtxt("C:\\Users\\Zheng\\PycharmProjects\\tf\\biyesheji\\Xy.txt")
        print(a)
        for index in range(10):
            c = np.empty(shape = [0, 3])
            b = np.empty(shape = [0, 3])
            for row in range(300):
                print("******************")
                print(a[row:row+1,:])
                if row % 10 == index:
                    c = np.append(c, a[row:row+1,:], axis=0)
                    #c = np.row_stack(c, a[row:row+1,:])
                else:
                    b = np.append(b, a[row:row+1,:], axis=0)
                    #b = np.row_stack(b, a[row:row+1,:])
            # b = a[0:int(index * 300 / 10), :]
            # c = a[int(index * 300 / 10):int((index + 1) * 300 / 10), :]
            # d = a[int((index + 1) * 300 / 10):300, :]
            # e = np.vstack((b, d))
            print(b)
            print(c)
            if not os.path.exists(filed + str(index + 1) + 'fold/mr0/'):  # 若不存在路径则创建
                os.makedirs(filed + str(index + 1) + 'fold/mr0/')
            np.savetxt(filed + str(index + 1) + 'fold/mr0/train.txt', b)
            np.savetxt(filed + str(index + 1) + 'fold/mr0/test.txt', c)
            del b
            del c
            gc.collect()
        # if len(filed) != 0:
        # data.allmr1_(filed+'biyesheji/data')


class ChildWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('显示结果')
        print(11)
        # self.pushButton.clicked.connect( self.btnClick)#按钮事件绑定

    def tableshow(self, dict_, name):
        print(3)
        print(dict_)
        self.model = QStandardItemModel()
        # self.model = QStandardItemModel(6, 2)
        list = []
        for (key, value) in dict_.items():
            list.append(str(key))
        #list.append('总和')
        self.model.setHorizontalHeaderLabels(list)
        self.model.setVerticalHeaderLabels([name])
        # self.model.setHorizontalHeaderLabels(['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6'])
        r = 0
        c = 0
        for (key, value) in dict_.items():
            # for row in range(6):
            # for column in range(2):
            item = QStandardItem(str(value))
            self.model.setItem(r, c, item)
            c = c + 1
        # self.child.label = QLabel()
        # self.child.label.setText('AAAA')
        # self.tableView = QTableView()
        # print(self.model.data())
        self.tableView = QtWidgets.QTableView()
        # self.tableView.setGeometry(QtCore.QRect(30, 81, 551, 231))
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.setAlignment(QtCore.Qt.AlignCenter)

    def all_tableshow(self, list_dict, list_name):
    #def all_tableshow(self, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, name1, name2, name3, name4, name5, name6, name7, name8):
        #list_dict, list_name
        # print(name5)
        # list_dict = []
        # list_dict.append(dict1)
        # list_dict.append(dict2)
        # list_dict.append(dict3)
        # list_dict.append(dict4)
        # list_dict.append(dict5)
        # list_dict.append(dict6)
        # list_dict.append(dict7)
        # list_dict.append(dict8)
        # list_name = []
        # list_name.append(name1)
        # list_name.append(name2)
        # list_name.append(name3)
        # list_name.append(name4)
        # list_name.append(name5)
        # list_name.append(name6)
        # list_name.append(name7)
        # list_name.append(name8)
        print(3)
        # print(dict_)
        self.model = QStandardItemModel()
        # self.model = QStandardItemModel(6, 2)
        list = []
        for (key, value) in list_dict[0].items():
            list.append(str(key))
        #print(list)
        print(list_name)
        #最后一行
        list.append('总计')
        list_sum = [0, 0, 0, 0, 0, 0, 0]
        #最后一列
        list_name.append('总计')
        self.model.setHorizontalHeaderLabels(list)
        self.model.setVerticalHeaderLabels(list_name)
        # self.model.setHorizontalHeaderLabels(['mr1', 'mr2', 'mr3', 'mr4', 'mr5', 'mr6'])
        r = 0
        c = 0
        for i in list_dict:
            sum = 0
            for (key, value) in i.items():
                #最后一列的各个数据
                sum = sum + value
                #最后一行的各个数据
                if c <= 7:
                    list_sum[c] = list_sum[c] + value
                # for row in range(6):
                # for column in range(2):
                item = QStandardItem(str(value))
                self.model.setItem(r, c, item)
                c = c + 1
                #print(c)
            #最后一列的数据
            item = QStandardItem(str(sum))
            self.model.setItem(r, c, item)
            r = r + 1
            list_sum[c] = list_sum[c] + sum
            c = 0
        print(list_sum)
        for i in list_sum:
            item = QStandardItem(i.__str__())
            self.model.setItem(r, c, item)
            c = c + 1
        # self.child.label = QLabel()
        # self.child.label.setText('AAAA')
        # self.tableView = QTableView()
        # print(self.model.data())
        self.tableView = QtWidgets.QTableView()
        # self.tableView.setGeometry(QtCore.QRect(30, 81, 551, 231))
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    window = mywindow()

    window.show()
    # child = ChildWindow()
    # child_ui = Ui_Dialog()
    # child_ui.setupUi(child)
    # child_ui = Ui_Dialog()
    # child_ui.setupUi(child)
    sys.exit(app.exec_())
