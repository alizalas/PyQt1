import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setWindowTitle("Жёлтые круги")
        self.pushButton.setToolTip("Нажмите на кнопку, и появятся жёлтые круги")
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.begin(self)
        pen = QPen(QColor(255, 255, 0), 1)
        painter.setPen(pen)
        painter.setBrush(QColor(255, 255, 0))

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
