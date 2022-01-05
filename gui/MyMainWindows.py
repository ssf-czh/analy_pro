import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_1 import Ui_MainWindow
from model.db import load, init_params, main_fittings
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.chart import  Ui_Temperature
from gui import main_1

load(r"template.xlsx")


class Ui_Dialog(QtWidgets.QWidget,Ui_Temperature):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义登录按钮的功能

    def show_temperature_chart(self):
        # self.hide()
        # print(main_1.a)
        self.temperature_chart = Ui_Dialog()
        self.temperature_chart.resize(870,570)
        self.temperature_chart.show()
        # print("yyyy")

        # app = QApplication(sys.argv)
        # mainwindow = QMainWindow()
        # mainwindow.setWindowTitle('demo')
        # mainwindow.resize(870, 570)
        #
        # my_demo = DEMO(mainwindow)
        #
        # sys.exit(app.exec_())




if __name__ == '__main__':


    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口   first=login()
    myWin.showMaximized()  #first.show()

    myWin.pushButton_533.clicked.connect(myWin.show_temperature_chart)

    sys.exit(app.exec_())  # 结束进程，退出程序
