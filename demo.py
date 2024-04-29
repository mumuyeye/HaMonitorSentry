from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Ui_step1 import Ui_MainWindow as ui_step1
from Ui_step2 import Ui_MainWindow as ui_step2
from Ui_step2 import Video
from Ui_step3 import Ui_MainWindow as ui_step3
from Ui_step4 import Ui_MainWindow as ui_step4
from Ui_step5 import Ui_MainWindow as ui_step5
from model import Model as md

model = md()

class step1UI(QtWidgets.QMainWindow, ui_step1):
    def __init__(self):
        super(step1UI, self).__init__()
        self.setupUi(self)

class step2UI(QtWidgets.QMainWindow, ui_step2):
    def __init__(self):
        super(step2UI, self).__init__()
        self.setupUi(self)

class step3UI(QtWidgets.QMainWindow, ui_step3):
    def __init__(self):
        super(step3UI, self).__init__()
        self.setupUi(self, model)

class step4UI(QtWidgets.QMainWindow, ui_step4):
    def __init__(self):
        super(step4UI, self).__init__()
        self.setupUi(self, model)

class step5UI(QtWidgets.QMainWindow, ui_step5):
    def __init__(self):
        super(step5UI, self).__init__()
        self.setupUi(self)

def main():
    
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    step1 = step1UI()
    step2 = step2UI()

    step4 = step4UI()
    step3 = step3UI()
    step5 = step5UI()
    v = Video()
    step1.show()
    step1.pushButton.clicked.connect(step3.show)
    step3.pushButton_2.clicked.connect(v.show)
    step3.pushButton_3.clicked.connect(step4.show)
    step3.pushButton_5.clicked.connect(step1.show)
    v.ui.pushButton.clicked.connect(step3.show)
    step4.pushButton.clicked.connect(step3.show)
    step1.pushButton2.clicked.connect(step5.show)
    step5.pushButton.clicked.connect(step1.show)
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
