import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 Window'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        # self, QtGui.QIcon("image/icon.png")
        self.InitWindow()


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width,self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
temp = App.exec_()
sys.exit(temp)