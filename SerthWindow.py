from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *
class SerthWindow(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.set_apper()
        self.exp = exp
        self.initUI()
        self.show()

    def results(self):
        self.index = (4*(self.exp.test1 + self.exp.test2 + self.exp.test3) - 200)/10
        if self.exp.age == 7 or  self.exp.age == 8:
            if self.index > 21:
                return txt_res1
            elif self.index <=20.9 and self.index >= 17:
                return txt_res2
            elif self.index <=16.9 and self.index >= 12:
                return txt_res3
            elif self.index <=11.9 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age == 9 or  self.exp.age == 10:
            if self.index > 19.5:
                return txt_res1
            elif self.index <=19.4 and self.index >= 15.5:
                return txt_res2
            elif self.index <=15.4 and self.index >= 10.5:
                return txt_res3
            elif self.index <=10.4 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age == 11 or self.exp.age == 12:
            if self.index > 18:
                return txt_res1
            elif self.index <=17.9 and self.index >= 14:
                return txt_res2
            elif self.index <=13.9 and self.index >= 9:
                return txt_res3
            elif self.index <=8.9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age == 13 or  self.exp.age == 14:
            if self.index > 16.5:
                return txt_res1
            elif self.index <=16.4 and self.index >= 12.5:
                return txt_res2
            elif self.index <=12.4 and self.index >= 7.5:
                return txt_res3
            elif self.index <=7.4 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age >= 15:
            if self.index > 15:
                return txt_res1
            elif self.index <= 14.9 and self.index >= 11:
                return txt_res2
            elif self.index <= 10.9 and self.index >= 6:
                return txt_res3
            elif self.index <= 5.9 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
    
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lb_work = QLabel(txt_workheart + self.results())
        self.lb_index = QLabel(txt_index + str(self.index))
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.lb_index,alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.lb_work,alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)
