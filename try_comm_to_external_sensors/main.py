
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
sys.path.append(r'.\try_comm_to_external_sensors')
import typing

from PyQt5.QtCore import qAbs 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PyQt5.uic import loadUi
cwd = getcwd()
#loadUi(r'.\mainwindow.ui')

from mainwindow_ui import Ui_MainWindow
from controller import Controller


class Window(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.main_widget = loadUi(r'.\mainwindow.ui',self) #dynamically way to load .ui file

        #self.setupUi(self) # statical way to load .ui file, have to use pyuic.exe to generate ui.py first

        #self.main_widget.tableWidget.setItem(0,0,QTableWidgetItem('hello'))

        #Mount controller
        self.__controler = Controller(parent=self)
        self.__controler.updatePosIndex.connect(self.main_widget.label_POS_INDEX.setText)

        self.__controler.updateCurrentPostions[0].updatePost.connect(self.main_widget.lineEdit_CP_MACH_X.setText)
        self.__controler.updateCurrentPostions[1].updatePost.connect(self.main_widget.lineEdit_CP_MACH_Y.setText)
        self.__controler.updateCurrentPostions[2].updatePost.connect(self.main_widget.lineEdit_CP_MACH_THETA.setText)
        
        self.__controler.updatePosIndex.connect(self.main_widget.label_POS_INDEX.setText)
        self.__controler.tableWidget= self.main_widget.tableWidget
        
        self.main_widget.pushButton_ACK.clicked.connect(self.__controler.onButtonAckClicked)

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass