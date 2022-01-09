import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_1 import Ui_MainWindow
from model.db import load, init_params, main_fittings
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.chart import Ui_Temperature, Ui_Pump, Ui_Cop, Ui_Lengqueta
from gui import main_1

load(r"template.xlsx")


class Ui_Dialog(QtWidgets.QWidget,Ui_Temperature):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)

class Ui_Dialog_Pump(QtWidgets.QWidget,Ui_Pump):
    def __init__(self):
        super(Ui_Dialog_Pump,self).__init__()
        self.setupUi(self)

class Ui_Dialog_Lengqueta(QtWidgets.QWidget,Ui_Lengqueta):
    def __init__(self):
        super(Ui_Dialog_Lengqueta,self).__init__()
        self.setupUi(self)

class Ui_Dialog_COP(QtWidgets.QWidget,Ui_Cop):
    def __init__(self):
        super(Ui_Dialog_COP,self).__init__()
        self.setupUi(self)

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义登录按钮的功能

    def show_temperature_chart(self):
        self.temperature_chart = Ui_Dialog()
        self.temperature_chart.showMaximized()
        print("***********")
        # self.temperature_chart.test()

    def show_pump_chart(self):
        self.pump_chart = Ui_Dialog_Pump()
        self.pump_chart.resize(1700,600)
        self.pump_chart.show()


        # pass
    def show_lengqueta_chart(self):
        self.lengqueta_chart = Ui_Dialog_Lengqueta()
        self.lengqueta_chart.resize(1700, 800)
        self.lengqueta_chart.show()

    def show_cop(self):
        self.cop_chart = Ui_Dialog_COP()
        self.cop_chart.resize(1700,600)
        self.cop_chart.show()
        # pass


if __name__ == '__main__':


    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口   first=login()
    myWin.showMaximized()  #first.show()

    myWin.pushButton_533.clicked.connect(myWin.show_temperature_chart)
    myWin.pushButton_543.clicked.connect(myWin.show_pump_chart)
    myWin.pushButton_553.clicked.connect(myWin.show_lengqueta_chart)

    myWin.pushButton_563.clicked.connect(myWin.show_cop)



    sys.exit(app.exec_())  # 结束进程，退出程序
