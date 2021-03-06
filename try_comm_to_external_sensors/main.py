
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
#sys.path.append(r'.\try_comm_to_external_sensors')
sys.path.append(r'.qt_for_python\uic')
sys.path.append(r'.qt_for_python/uic')
import typing

from PyQt5.QtCore import QModelIndex, qAbs
from PyQt5 import QtCore, QtGui
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

        self.__controler.updateToolCoord[0].updatePost.connect(self.lineEdit_TOOL_X.setText)
        self.__controler.updateToolCoord[1].updatePost.connect(self.lineEdit_TOOL_Y.setText)

        self.__controler.updateWkCoord[0].updatePost.connect(self.lineEdit_WK_X.setText)
        self.__controler.updateWkCoord[1].updatePost.connect(self.lineEdit_WK_Y.setText)
        self.__controler.updateWkCoord[2].updatePost.connect(self.lineEdit_WK_THETA.setText)

        
        self.__controler.updatePosIndex.connect(self.label_POS_INDEX.setText)

        self.__controler.updateTriggerSignal.connect(self.label_TRIGGERD.onStateChanged)
        self.__controler.updateTriggerSignal.connect(self.pushButton_ACK.setEnabled)
        
        self.pushButton_ACK.clicked.connect(self.__controler.onButtonAckClicked)

        self.tableViewCalibration.setModel(self.__controler.model)
        [self.tableViewCalibration.setRowHidden(x,True) for x in range(0,16)]
        [self.tableViewCalibration.setRowHidden(x,False) for x in range(0,9)] #Open

        self.tableViewOperation.setModel(self.__controler.model)
        [self.tableViewOperation.setRowHidden(x,True) for x in range(0,16)]
        [self.tableViewOperation.setRowHidden(x,False) for x in range(9,13)] #Open

        self.label_3.setPixmap(QtGui.QPixmap("demo_scenerio.png"))
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass