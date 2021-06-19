
import os
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
sys.path.append(r'.\try_comm_to_external_sensors')
import typing

from PyQt5.QtCore import qAbs 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QWidget
from PyQt5.uic import loadUi

from mainwindow_ui import Ui_MainWindow


class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass