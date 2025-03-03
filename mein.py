# from PyQt6 import
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.uic.properties import QtCore

from windows import MainWindow
from api import YandexAPI


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    # win.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
    win.show()
    sys.exit(app.exec())
