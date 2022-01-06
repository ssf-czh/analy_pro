# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\welcom2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QMainWindow, QHBoxLayout
from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Gauge
from gui import main_1

class Ui_Temperature(object):
    def setupUi(self, Form):



        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout2 = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout.setSizeConstraint()
        self.hboxlayout_1 = QHBoxLayout()
        self.hboxlayout_2 = QHBoxLayout()


        self.vboxlayout = QVBoxLayout(Form)

        # self.vboxlayout2 = QVBoxLayout(Form)
        self.browser = QWebEngineView()
        self.browser2 = QWebEngineView()
        self.browser3 = QWebEngineView()
        self.browser4 = QWebEngineView()
        self.browser5 = QWebEngineView()
        self.browser6 = QWebEngineView()




        self.hboxlayout_1.addWidget(self.browser)
        self.hboxlayout_1.addWidget(self.browser2)
        self.hboxlayout_1.addWidget(self.browser3)
        self.hboxlayout_2.addWidget(self.browser4)
        self.hboxlayout_2.addWidget(self.browser5)
        self.hboxlayout_2.addWidget(self.browser6)



        self.vboxlayout.addLayout(self.hboxlayout_1)
        self.vboxlayout.addLayout(self.hboxlayout_2)
        # Form.set
        # self.hboxlayout.addWidget(self.browser4)
        # self.hboxlayout.addWidget(self.browser5)
        # self.hboxlayout.addWidget(self.browser6)
        # self.vboxlayout2.addWidget(self.browser2)

        # self.button_init()

        # button1 = QPushButton('冷冻出水温度')
        # button2 = QPushButton('冷冻回水温度')
        # button3 = QPushButton('冷却出水温度')
        # button4 = QPushButton("冷却回水温度")
        # button5 = QPushButton("冷冻水温差")
        # button6 = QPushButton("冷却水温差")
        # self.vboxlayout.addWidget(button1)
        # self.vboxlayout.addWidget(button2)
        # self.vboxlayout.addWidget(button3)
        # self.vboxlayout.addWidget(button4)
        # self.vboxlayout.addWidget(button5)
        # self.vboxlayout.addWidget(button6)

        self.demo_yibiaopan_t1()
        self.demo_yibiaopan_t2()
        self.demo_yibiaopan_t3()
        self.demo_yibiaopan_t4()
        self.demo_yibiaopan_t2_t1()
        self.demo_yibiaopan_t4_t3()

        # button1.clicked.connect(self.demo_yibiaopan_t1)
        # button2.clicked.connect(self.demo_yibiaopan_t2)
        # button3.clicked.connect(self.demo_yibiaopan_t3)
        # button4.clicked.connect(self.demo_yibiaopan_t4)
        # button5.clicked.connect(self.demo_yibiaopan_t2_t1)
        # button6.clicked.connect(self.demo_yibiaopan_t4_t3)

    def retranslateUi(self, Form):
        # _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        # self.label.setText(_translate("Form", "不知名步骤"))
        # self.pushButton.setText(_translate("Form", "第一关"))
        # self.pushButton.clicked.connect(self.demo_pie)
        # self.pushButton_2.setText(_translate("Form", "第二关"))
        pass

    # def demo_bar(self):
    #     """
    #         柱形图
    #     """
    #     bar = Bar('我的第一个表-主标题', '目标题')
    #     bar.add('服务', ['衬衫', '衬衫', 'C语言', 'python'], [5, 7, 8, 9])
    #     bar.show_config()
    #     bar.render(path='render_1.html')
    #     self.browser.load(QUrl("file:///render_1.html"))
    #
    # def demo_pie(self):
    #     """
    #         饼图
    #     """
    #     attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("饼图示例")
    #     pie.add("", attr, v1, is_label_show=True)
    #     print(111)
    #     pie.render(path='render_pie.html')
    #     print(222)
    #     self.browser.load(QUrl("file:///render_pie.html"))
    #
    # def demo_pie_h(self):
    #     """
    #     圆环图
    #     """
    #     attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("饼图-圆环图示例", title_pos='center')
    #     pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
    #             is_label_show=True, legend_orient='vertical',
    #             legend_pos='left')
    #     pie.render(path='render_pie_h.html')
    #     self.browser.load(QUrl("file:///render_pie_h.html"))

    def demo_yibiaopan_t1(self):
        val = float(main_1.temperature_record.t1)
        if val == -1:
            val = 0
        gauge = Gauge("冷冻出水温度仪表盘")
        gauge.add("", attr="冷冻出水温度", value=val,scale_range=(5,15))
        # gauge.
        gauge.render('gauge_t1.html')
        self.browser.load(QUrl("file:///gauge_t1.html"))

    def demo_yibiaopan_t2(self):
        val = float(main_1.temperature_record.t2)
        if val == -1:
            val = 0
        gauge = Gauge("冷冻回水温度仪表盘")
        gauge.add("", attr="冷冻回水温度", value=val,scale_range=(10,20))
        # gauge.
        gauge.render('gauge_t2.html')
        self.browser2.load(QUrl("file:///gauge_t2.html"))

    def demo_yibiaopan_t3(self):
        val = float(main_1.temperature_record.t3)
        if val == -1:
            val = 0
        gauge = Gauge("冷却出水温度仪表盘")
        gauge.add("", attr="冷却出水温度", value=val,scale_range=(5,33))
        # gauge.
        gauge.render('gauge_t3.html')
        self.browser3.load(QUrl("file:///gauge_t3.html"))

    def demo_yibiaopan_t4(self):
        val = float(main_1.temperature_record.t4)
        if val == -1:
            val = 0
        gauge = Gauge("冷却回水温度仪表盘")
        gauge.add("", attr="冷却回水温度", value=val,scale_range=(10,38))
        # gauge.
        gauge.render('gauge_t4.html')
        self.browser4.load(QUrl("file:///gauge_t4.html"))

    def demo_yibiaopan_t2_t1(self):
        val = float(main_1.temperature_record.t2)-float(main_1.temperature_record.t1)
        if main_1.temperature_record.t2 == -1 or main_1.temperature_record.t1 == -1:
            val = 0
        val = round(val,3)
        gauge = Gauge("冷冻水温差仪表盘")
        gauge.add("", attr="冷冻水温差", value=val,scale_range=(4,10))
        # gauge.
        gauge.render('gauge_5.html')
        self.browser5.load(QUrl("file:///gauge_5.html"))

    def demo_yibiaopan_t4_t3(self):
        val = float(main_1.temperature_record.t4)-float(main_1.temperature_record.t3)
        if main_1.temperature_record.t4 == -1 or main_1.temperature_record.t3 == -1:
            val = 0
        val = round(val,3)
        gauge = Gauge("冷却水温差仪表盘")
        gauge.add("", attr="冷却水温差", value=val,scale_range=(4,10))
        # gauge.
        gauge.render('gauge_6.html')
        self.browser6.load(QUrl("file:///gauge_6.html"))