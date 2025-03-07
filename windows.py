import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from window import Ui_MainWindow
from api2 import YandexAPI


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coord = (50.842588, 58.846908)
        self.delta = 17
        self.step = 0.005
        self.karta = YandexAPI()
        self.ready()

    def param_creater(self):
        return {"ll": ','.join(map(str, self.coord)), 'z': self.delta}

    def ready(self):
        pix = self.karta.get_map(self.param_creater())
        if pix != 'result.png':
            self.map.setText(pix)
        else:
            pix = QPixmap(pix)
            self.map.setPixmap(pix)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Up and self.delta < 17:
            self.delta += 1
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_Down and self.delta > 1:
            self.delta -= 1
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_D:
            self.coord = (self.coord[0] + self.step) % 360, self.coord[1]
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_A:
            self.coord = (self.coord[0] - self.step) % 360, self.coord[1]
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_S:
            self.coord = self.coord[0], (self.coord[1] - self.step / 2) % 180
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_W:
            self.coord = self.coord[0], (self.coord[1] + self.step / 2) % 180
            self.ready()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
