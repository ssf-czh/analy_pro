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
import pyecharts
from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Gauge
from gui import main_1
import time

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

        # button1 = QPushButton('??????????????????')
        # button2 = QPushButton('??????????????????')
        # button3 = QPushButton('??????????????????')
        # button4 = QPushButton("??????????????????")
        # button5 = QPushButton("???????????????")
        # button6 = QPushButton("???????????????")
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
        # self.label.setText(_translate("Form", "???????????????"))
        # self.pushButton.setText(_translate("Form", "?????????"))
        # self.pushButton.clicked.connect(self.demo_pie)
        # self.pushButton_2.setText(_translate("Form", "?????????"))
        pass
    # def test(self):
    #     self.demo_yibiaopan_t1(1)
    #     print("===")
    #     time.sleep(4)
    #     print("*****===")
    #     self.demo_yibiaopan_t1(2)

    # def demo_bar(self):
    #     """
    #         ?????????
    #     """
    #     bar = Bar('??????????????????-?????????', '?????????')
    #     bar.add('??????', ['??????', '??????', 'C??????', 'python'], [5, 7, 8, 9])
    #     bar.show_config()
    #     bar.render(path='render_1.html')
    #     self.browser.load(QUrl("file:///render_1.html"))
    #
    # def demo_pie(self):
    #     """
    #         ??????
    #     """
    #     attr = ["??????", "?????????", "?????????", "??????", "?????????", "??????"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("????????????")
    #     pie.add("", attr, v1, is_label_show=True)
    #     print(111)
    #     pie.render(path='render_pie.html')
    #     print(222)
    #     self.browser.load(QUrl("file:///render_pie.html"))
    #
    # def demo_pie_h(self):
    #     """
    #     ?????????
    #     """
    #     attr = ["??????", "?????????", "?????????", "??????", "?????????", "??????"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("??????-???????????????", title_pos='center')
    #     pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
    #             is_label_show=True, legend_orient='vertical',
    #             legend_pos='left')
    #     pie.render(path='render_pie_h.html')
    #     self.browser.load(QUrl("file:///render_pie_h.html"))

    def demo_yibiaopan_t1(self):
        val = float(main_1.temperature_record[0].t1)
        if val == -1:
            val = 0
        gauge = Gauge("???????????????????????????")
        gauge.add("", attr="??????????????????", value=val,scale_range=(5,15))
        # gauge.
        gauge.render('./templates/gauge_t1.html')
        self.browser.load(QUrl("file:///./templates/gauge_t1.html"))



    def demo_yibiaopan_t2(self):
        val = float(main_1.temperature_record[0].t2)
        if val == -1:
            val = 0
        gauge = Gauge("???????????????????????????")
        gauge.add("", attr="??????????????????", value=val,scale_range=(10,20))
        # gauge.
        gauge.render('./templates/gauge_t2.html')
        self.browser2.load(QUrl("file:///./templates/gauge_t2.html"))
    def demo_yibiaopan_t3(self):
        val = float(main_1.temperature_record[0].t3)
        if val == -1:
            val = 0
        gauge = Gauge("???????????????????????????")
        gauge.add("", attr="??????????????????", value=val,scale_range=(5,33))
        # gauge.
        gauge.render('./templates/gauge_t3.html')
        self.browser3.load(QUrl("file:///./templates/gauge_t3.html"))

    def demo_yibiaopan_t4(self):
        val = float(main_1.temperature_record[0].t4)
        if val == -1:
            val = 0
        gauge = Gauge("???????????????????????????")
        gauge.add("", attr="??????????????????", value=val,scale_range=(10,38))
        # gauge.
        gauge.render('./templates/gauge_t4.html')
        self.browser4.load(QUrl("file:///./templates/gauge_t4.html"))

    def demo_yibiaopan_t2_t1(self):
        val = float(main_1.temperature_record[0].t2)-float(main_1.temperature_record[0].t1)
        if main_1.temperature_record[0].t2 == -1 or main_1.temperature_record[0].t1 == -1:
            val = 0
        val = round(val,3)
        gauge = Gauge("????????????????????????")
        gauge.add("", attr="???????????????", value=val,scale_range=(4,10))
        # gauge.
        gauge.render('./templates/gauge_5.html')
        self.browser5.load(QUrl("file:///./templates/gauge_5.html"))

    def demo_yibiaopan_t4_t3(self):
        val = float(main_1.temperature_record[0].t4)-float(main_1.temperature_record[0].t3)
        if main_1.temperature_record[0].t4 == -1 or main_1.temperature_record[0].t3 == -1:
            val = 0
        val = round(val,3)
        gauge = Gauge("????????????????????????")
        gauge.add("", attr="???????????????", value=val,scale_range=(4,10))
        # gauge.
        gauge.render('./templates/gauge_6.html')
        self.browser6.load(QUrl("file:///./templates/gauge_6.html"))

# # == pump
class Ui_Pump(object):
    def setupUi(self, Form):



        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout2 = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout.setSizeConstraint()
        self.hboxlayout_1 = QHBoxLayout()
        # self.hboxlayout_2 = QHBoxLayout()


        self.vboxlayout = QVBoxLayout(Form)

        # self.vboxlayout2 = QVBoxLayout(Form)
        self.browser = QWebEngineView()
        self.browser2 = QWebEngineView()





        self.hboxlayout_1.addWidget(self.browser)
        self.hboxlayout_1.addWidget(self.browser2)
        self.vboxlayout.addLayout(self.hboxlayout_1)





        self.demo_pump_pie()
        self.demo_pump_bar()
        # self.demo_yibiaopan_t2()
        # self.demo_yibiaopan_t3()
        # self.demo_yibiaopan_t4()
        # self.demo_yibiaopan_t2_t1()
        # self.demo_yibiaopan_t4_t3()

        # button1.clicked.connect(self.demo_yibiaopan_t1)
        # button2.clicked.connect(self.demo_yibiaopan_t2)
        # button3.clicked.connect(self.demo_yibiaopan_t3)
        # button4.clicked.connect(self.demo_yibiaopan_t4)
        # button5.clicked.connect(self.demo_yibiaopan_t2_t1)
        # button6.clicked.connect(self.demo_yibiaopan_t4_t3)

    def retranslateUi(self, Form):
        # _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        # self.label.setText(_translate("Form", "???????????????"))
        # self.pushButton.setText(_translate("Form", "?????????"))
        # self.pushButton.clicked.connect(self.demo_pie)
        # self.pushButton_2.setText(_translate("Form", "?????????"))
        pass

    # def demo_bar(self):
    #     """
    #         ?????????
    #     """
    #     bar = Bar('??????????????????-?????????', '?????????')
    #     bar.add('??????', ['??????', '??????', 'C??????', 'python'], [5, 7, 8, 9])
    #     bar.show_config()
    #     bar.render(path='render_1.html')
    #     self.browser.load(QUrl("file:///render_1.html"))
    #
    # def demo_pie(self):
    #     """
    #         ??????
    #     """
    #     attr = ["??????", "?????????", "?????????", "??????", "?????????", "??????"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("????????????")
    #     pie.add("", attr, v1, is_label_show=True)
    #     print(111)
    #     pie.render(path='render_pie.html')
    #     print(222)
    #     self.browser.load(QUrl("file:///render_pie.html"))
    #
    # def demo_pie_h(self):
    #     """
    #     ?????????
    #     """
    #     attr = ["??????", "?????????", "?????????", "??????", "?????????", "??????"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("??????-???????????????", title_pos='center')
    #     pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
    #             is_label_show=True, legend_orient='vertical',
    #             legend_pos='left')
    #     pie.render(path='render_pie_h.html')
    #     self.browser.load(QUrl("file:///render_pie_h.html"))

    def demo_pump_pie(self):
        # val = float(main_1.temperature_record.t1)
        # if val == -1:
        #     val = 0
        # gauge = Gauge("???????????????????????????")
        # gauge.add("", attr="??????????????????", value=val,scale_range=(5,15))
        # # gauge.
        # gauge.render('gauge_t1.html')
        # self.browser.load(QUrl("file:///gauge_t1.html"))
        attr = ["????????????/Kw/%", "??????????????????/Kw", "??????????????????/Kw", "???????????????/Kw"]
        p1 = main_1.pump_record.p1
        p2 = main_1.pump_record.p2
        p3 = main_1.pump_record.p3
        p4 = main_1.pump_record.p4

        v1 = [p1, p2, p3, p4]
        pie = Pie("???????????????")
        pie.add("", attr, v1, is_label_show=True)
        # print(111)
        pie.render(path='./templates/render_pie.html')
        # print(222)
        self.browser.load(QUrl("file:///./templates/render_pie.html"))

    def demo_pump_bar(self):
        attr = []
        v1 = []
        v2 = []
        v3 = []
        v4 = []
        for data in main_1.table_54_records:
            year = data.year
            month = data.mon
            day = data.day
            hour = data.hour
            attr.append(str(year)+"???"+str(month)+"???"+str(day)+"???"+str(hour)+"???")
            v1.append(float(data.p1))
            v2.append(float(data.p2))
            v3.append(float(data.p3))
            v4.append(float(data.p4))

        # attr = ['??????', '?????????', '?????????', '??????', '?????????', '??????']
        # v1 = [5, 20, 36, 10, 75, 90]
        # v2 = [10, 25, 8, 60, 20, 80]
        bar = Bar('????????????????????????')
        bar.add('????????????/Kw', attr, v1, is_stack=True, is_datazoom_show=True)  # is_stack = True????????????????????????
        bar.add('??????????????????/Kw', attr, v2, is_stack=True, is_datazoom_show=True)
        bar.add('??????????????????/Kw', attr, v3, is_stack=True, is_datazoom_show=True)
        bar.add('???????????????/Kw', attr, v4, is_stack=True, is_datazoom_show=True)
        bar.render('./templates/pump_bar.html')
        self.browser2.load(QUrl("file:///./templates/pump_bar.html"))

# === lengqueta

class Ui_Lengqueta(object):
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


        self.hboxlayout_1.addWidget(self.browser)
        self.hboxlayout_1.addWidget(self.browser2)

        self.hboxlayout_2.addWidget(self.browser3)
        self.hboxlayout_2.addWidget(self.browser4)


        self.vboxlayout.addLayout(self.hboxlayout_1)
        self.vboxlayout.addLayout(self.hboxlayout_2)
        # Form.set
        # self.hboxlayout.addWidget(self.browser4)
        # self.hboxlayout.addWidget(self.browser5)
        # self.hboxlayout.addWidget(self.browser6)
        # self.vboxlayout2.addWidget(self.browser2)

        # self.button_init()

        # button1 = QPushButton('??????????????????')
        # button2 = QPushButton('??????????????????')
        # button3 = QPushButton('??????????????????')
        # button4 = QPushButton("??????????????????")
        # button5 = QPushButton("???????????????")
        # button6 = QPushButton("???????????????")
        # self.vboxlayout.addWidget(button1)
        # self.vboxlayout.addWidget(button2)
        # self.vboxlayout.addWidget(button3)
        # self.vboxlayout.addWidget(button4)
        # self.vboxlayout.addWidget(button5)
        # self.vboxlayout.addWidget(button6)

        self.demo_yibiaopan_jinshui()
        self.demo_yibiaopan_huishui()
        self.demo_yibiaopan_lengfu()
        self.demo_yibiaopan_lengqueta()


        # button1.clicked.connect(self.demo_yibiaopan_t1)
        # button2.clicked.connect(self.demo_yibiaopan_t2)
        # button3.clicked.connect(self.demo_yibiaopan_t3)
        # button4.clicked.connect(self.demo_yibiaopan_t4)
        # button5.clicked.connect(self.demo_yibiaopan_t2_t1)
        # button6.clicked.connect(self.demo_yibiaopan_t4_t3)

    def retranslateUi(self, Form):
        # _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        # self.label.setText(_translate("Form", "???????????????"))
        # self.pushButton.setText(_translate("Form", "?????????"))
        # self.pushButton.clicked.connect(self.demo_pie)
        # self.pushButton_2.setText(_translate("Form", "?????????"))
        pass

    # def test(self):
    #     self.demo_yibiaopan_t1(1)
    #     print("===")
    #     time.sleep(4)
    #     print("*****===")
    #     self.demo_yibiaopan_t1(2)

    # def demo_bar(self):
    #     """
    #         ?????????
    #     """
    #     bar = Bar('??????????????????-?????????', '?????????')
    #     bar.add('??????', ['??????', '??????', 'C??????', 'python'], [5, 7, 8, 9])
    #     bar.show_config()
    #     bar.render(path='render_1.html')
    #     self.browser.load(QUrl("file:///render_1.html"))
    #
    # def demo_pie(self):
    #     """
    #         ??????
    #     """
    #     attr = ["??????", "?????????", "?????????", "??????", "?????????", "??????"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("????????????")
    #     pie.add("", attr, v1, is_label_show=True)
    #     print(111)
    #     pie.render(path='render_pie.html')
    #     print(222)
    #     self.browser.load(QUrl("file:///render_pie.html"))
    #
    # def demo_pie_h(self):
    #     """
    #     ?????????
    #     """
    #     attr = ["??????", "?????????", "?????????", "??????", "?????????", "??????"]
    #     v1 = [11, 12, 13, 10, 10, 10]
    #     pie = Pie("??????-???????????????", title_pos='center')
    #     pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
    #             is_label_show=True, legend_orient='vertical',
    #             legend_pos='left')
    #     pie.render(path='render_pie_h.html')
    #     self.browser.load(QUrl("file:///render_pie_h.html"))

    def demo_yibiaopan_jinshui(self):
        val = float(main_1.lengqueta_record[0].t3)
        if val == -1:
            val = 0
        gauge = Gauge("???????????????????????????")
        gauge.add("", attr="??????????????????", value=val, scale_range=(5, 33))
        # gauge.
        gauge.render('./templates/gauge_jinshui.html')
        self.browser.load(QUrl("file:///./templates/gauge_jinshui.html"))

    def demo_yibiaopan_huishui(self):
        val = float(main_1.lengqueta_record[0].t4)
        if val == -1:
            val = 0
        gauge = Gauge("???????????????????????????")
        gauge.add("", attr="??????????????????", value=val, scale_range=(10, 38))
        # gauge.
        gauge.render('./templates/gauge_huishui.html')
        self.browser2.load(QUrl("file:///./templates/gauge_huishui.html"))

    def demo_yibiaopan_lengfu(self):
        val = float(main_1.lengqueta_record[0].delta_t)
        if val == -1:
            val = 0
        gauge = Gauge("????????????????????????")
        gauge.add("", attr="???????????????", value=val, scale_range=(0, 20))
        # gauge.
        gauge.render('./templates/gauge_lengfu.html')
        self.browser3.load(QUrl("file:///./templates/gauge_lengfu.html"))

    def demo_yibiaopan_lengqueta(self):
        val = float(main_1.lengqueta_record[0].t4)-float(main_1.lengqueta_record[0].t3)
        val = round(val,3)
        if val == -1:
            val = 0
        gauge = Gauge("?????????????????????????????????")
        gauge.add("", attr="????????????????????????", value=val, scale_range=(4,10))
        # gauge.
        gauge.render('./templates/gauge_lengqueta.html')
        self.browser4.load(QUrl("file:///./templates/gauge_lengqueta.html"))


# == cop
class Ui_Cop(object):
    def setupUi(self, Form):



        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout2 = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout = QVBoxLayout(Form)
        # self.vboxlayout.setSizeConstraint()
        self.hboxlayout_1 = QHBoxLayout()
        # self.hboxlayout_2 = QHBoxLayout()


        self.vboxlayout = QVBoxLayout(Form)

        # self.vboxlayout2 = QVBoxLayout(Form)
        self.browser = QWebEngineView()
        self.browser2 = QWebEngineView()





        self.hboxlayout_1.addWidget(self.browser)
        self.hboxlayout_1.addWidget(self.browser2)
        self.vboxlayout.addLayout(self.hboxlayout_1)





        self.demo_time_copBar()
        self.demo_q_copBar()


    def retranslateUi(self, Form):
        pass



    def demo_time_copBar(self):

        # //????????????

        columns = []
        pump_cop = []
        system_cop = []
        for data in main_1.table_56_records:
            year = data.year
            month = data.mon
            day = data.day
            hour = data.hour
            columns.append(str(year)+"???"+str(month)+"???"+str(day)+"???"+str(hour)+"???")
            pump_cop.append(round(float(data.q/data.p1),3))
            system_cop.append(float(data.cop))

        # //????????????

        # //???????????????????????????????????????
        bar = Bar("COP???????????????")
        # //????????????????????????????????????
        bar.add("??????COP", columns, pump_cop, mark_line=["average"], mark_point=["max", "min"],is_datazoom_show=True)
        bar.add("??????COP", columns, system_cop, mark_line=["average"], mark_point=["max", "min"],is_datazoom_show=True)
        # //??????????????????????????????.html?????????
        bar.render("./templates/timeBar.html")
        self.browser.load(QUrl("file:///./templates/timeBar.html"))

    def demo_q_copBar(self):
        columns = []
        pump_cop = []
        system_cop = []
        for data in main_1.table_56_records:

            columns.append(str(data.q) + "Kw")
            pump_cop.append(round(float(data.q / data.p1),3))
            system_cop.append(float(data.cop))

        # //????????????

        # //???????????????????????????????????????
        bar = Bar("COP???????????????")
        # //????????????????????????????????????
        bar.add("??????COP", columns, pump_cop, mark_line=["average"], mark_point=["max", "min"], is_datazoom_show=True)
        bar.add("??????COP", columns, system_cop, mark_line=["average"], mark_point=["max", "min"], is_datazoom_show=True)
        # //??????????????????????????????.html?????????
        bar.render("./templates/qBar.html")
        self.browser2.load(QUrl("file:///./templates/qBar.html"))



import random
# attr = ["{}???".format(i) for i in range(30)]
# v1 = [random.randint(1, 30) for _ in range(30)]
# bar = Bar("Bar - datazoom - slider ??????")
# bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
# bar.render("test.html")
