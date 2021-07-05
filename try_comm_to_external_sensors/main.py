
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
#sys.path.append(r'.\try_comm_to_external_sensors')
sys.path.append(r'.qt_for_python\uic')
import typing

from PyQt5.QtCore import qAbs 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PyQt5.uic import loadUi
cwd = getcwd()
#loadUi(r'.\mainwindow.ui')

from controller import Controller
from mainwindow import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        #self.main_widget = loadUi(r'mainwindow.ui',self) #dynamically way to load .ui file

        self.setupUi(self) # statical way to load .ui file, have to use pyuic.exe to generate ui.py first

        #self.main_widget.tableWidget.setItem(0,0,QTableWidgetItem('hello'))

        #Mount controller
        self.__controler = Controller(parent=self)
        self.__controler.updatePosIndex.connect(self.label_POS_INDEX.setText)

        self.__controler.updateCurrentPositions[0].updatePost.connect(self.lineEdit_CP_MACH_X.setText)
        self.__controler.updateCurrentPositions[1].updatePost.connect(self.lineEdit_CP_MACH_Y.setText)
        self.__controler.updateCurrentPositions[2].updatePost.connect(self.lineEdit_CP_MACH_Z.setText)
        
        self.__controler.updateVisionPositions[0].updatePost.connect(self.lineEdit_CP_VI_X.setText)
        self.__controler.updateVisionPositions[1].updatePost.connect(self.lineEdit_CP_VI_Y.setText)
        
        self.__controler.updatePosIndex.connect(self.label_POS_INDEX.setText)
        self.__controler.tableWidget= self.tableWidget_CALI

        self.__controler.updateTriggerSignal.connect(self.label_TRIGGERD.onStateChanged)
        self.__controler.updateTriggerSignal.connect(self.pushButton_ACK.setEnabled)
        
        self.pushButton_ACK.clicked.connect(self.__controler.onButtonAckClicked)

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass