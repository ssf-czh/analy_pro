import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.main_1 import Ui_MainWindow
from model.db import load, init_params, main_fittings
from PyQt5 import QtCore, QtGui, QtWidgets

load(r"template.xlsx")

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)




if __name__ == '__main__':


    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口


    myWin.showMaximized()
    sys.exit(app.exec_())  # 结束进程，退出程序
