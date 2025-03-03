import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from window import Ui_MainWindow
from api2 import YandexAPI


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coord = (55.751574, 37.617728)
        self.step = 0.005
        self.karta = YandexAPI()
        self.ready()

    def ready(self):
        self.map.setPixmap(QPixmap(self.karta.get_map()))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Up:
            self.coord = self.coord[0] + self.step, self.coord[1] + self.step
            self.ready()
        elif event.key() == QtCore.Qt.Key.Key_Down:
            self.coord = self.coord[0] - self.step, self.coord[1] - self.step
            self.ready()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())