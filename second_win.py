# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults)
        self.btn1 = QPushButton(txt_test1)
        self.btn2 = QPushButton(txt_test2)
        self.btn3 = QPushButton(txt_test3)
        self.timer = QLabel("0.00.00")
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.btn1)
        self.l_line.addWidget(self.btn2)
        self.l_line.addWidget(self.btn3)
        self.l_line.addWidget(self.btn_next)
        self.r_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)       
    def next_click(self):
        self.hide()
        #self.tw = FinalWin()
app = QApplication([])
mw = TestWin()
app.exec_()