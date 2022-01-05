import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QMainWindow
from pyecharts import Bar
from pyecharts import Pie

a = 11

class DEMO:
    def __init__(self, mainwindow):
        widget = QWidget()
        self.vboxlayout = QVBoxLayout(widget)

        self.browser = QWebEngineView()
        self.vboxlayout.addWidget(self.browser)

        self.button_init()

        mainwindow.setCentralWidget(widget)
        mainwindow.show()

    def button_init(self):
        button1 = QPushButton('柱形图')
        button2 = QPushButton('饼行图')
        button3 = QPushButton('环行图')
        self.vboxlayout.addWidget(button1)
        self.vboxlayout.addWidget(button2)
        self.vboxlayout.addWidget(button3)
        button1.clicked.connect(self.demo_bar)
        button2.clicked.connect(self.demo_pie)
        button3.clicked.connect(self.demo_pie_h)

    def demo_bar(self):
        """
            柱形图
        """
        bar = Bar('我的第一个表-主标题', '目标题')
        bar.add('服务', ['衬衫', '衬衫', 'C语言', 'python'], [5, 7, 8, 9])
        bar.show_config()
        bar.render(path='render_1.html')
        self.browser.load(QUrl("file:///render_1.html"))

    def demo_pie(self):
        """
            饼图
        """
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        pie = Pie("饼图示例")
        pie.add("", attr, v1, is_label_show=True)
        pie.render(path='render_pie.html')
        self.browser.load(QUrl("file:///render_pie.html"))

    def demo_pie_h(self):
        """
        圆环图
        """
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        pie = Pie("饼图-圆环图示例", title_pos='center')
        pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
                is_label_show=True, legend_orient='vertical',
                legend_pos='left')
        pie.render(path='render_pie_h.html')
        self.browser.load(QUrl("file:///render_pie_h.html"))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainwindow = QMainWindow()
#     mainwindow.setWindowTitle('demo')
#     mainwindow.resize(870, 570)
#
#     my_demo = DEMO(mainwindow)
#
#     sys.exit(app.exec_())