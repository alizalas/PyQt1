import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Разноцветные круги")
        self.pushButton.setToolTip("Нажмите на кнопку, и появятся разноцветные круги")
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.begin(self)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        pen = QPen(color, 1)
        painter.setPen(pen)
        painter.setBrush(color)

        size = randint(10, 50)
        painter.drawEllipse(randint(50, 350), randint(80, 250), size, size)
        painter.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
