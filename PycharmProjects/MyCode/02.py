import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()  #창이 죽지않고 계속 살아있게 해줌  ..event loop
