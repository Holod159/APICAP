import sys

from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QImage
from window import Ui_MainWindow
from api2 import YandexAPI


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coord = (55.751574, 37.617728)
        self.delta = 17
        self.step = 0.005
        self.karta = YandexAPI()
        self.ready()

    def param_creater(self, coord, zoom):
        img = QImage.fromData(self.karta.get_map({"ll": ','.join(map(str, coord)), 'z': zoom}))
        return img

    def ready(self):
        self.map.setPixmap(QPixmap(self.param_creater(self.coord, self.delta)))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Up and self.delta < 17:
            self.delta += 1
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_Down and self.delta > 1:
            self.delta -= 1
            self.ready()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
