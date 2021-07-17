
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
sys.path.append(r'.qt_for_python\uic')
sys.path.append(r'.qt_for_python/uic')
import typing

from PyQt5.QtCore import QModelIndex, pyqtSlot, qAbs, Qt, pyqtSignal, pyqtSlot, QItemSelection
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget


import pointtable
from random import random

cwd = getcwd()

from mainwindow import Ui_MainWindow
from controller import Controller, JOG_STOP, JOG_CONTINUOUS, JOG_INCREMENT

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.setupUi(self) # statical way to load .ui file, have to use pyuic.exe to generate ui.py first
        self.tableView.setModel(pointtable.Model)
        self._controller = Controller(self)

        self.initTabl1()

        self.comboBox_MODE_SEL.setItemData(0,(JOG_CONTINUOUS,0))
        self.comboBox_MODE_SEL.setItemData(1,(JOG_INCREMENT,float(1)))
        self.comboBox_MODE_SEL.setItemData(2,(JOG_INCREMENT,float(0.1)))
        self.comboBox_MODE_SEL.setItemData(3,(JOG_INCREMENT,float(0.01)))
        self.comboBox_MODE_SEL.setItemData(4,(JOG_INCREMENT,float(0.001)))
        self._dict_join_and_direction = {
            self.pushButton_JOG_X_P : (0,1),
            self.pushButton_JOG_Y_P : (1,1),
            self.pushButton_JOG_Z_P : (2,1),
            self.pushButton_JOG_X_N : (0,-1),
            self.pushButton_JOG_Y_N : (1,-1),
            self.pushButton_JOG_Z_N : (2,-1),
        }

        pass

    def initTabl1(self):
        self.pushButton_TEACH.setEnabled(False)
        self.tableView.selectionModel().selectionChanged.connect(self.onTableViewSelected)
        pass

    @pyqtSlot()
    def onTableViewSelected(self,selected : QItemSelection,deselected):
        self.pushButton_TEACH.setEnabled(len(selected.indexes())>0)
        pass

    #The incremental mode
    @pyqtSlot()
    def onJogButtonClicked(self):
        if self.comboBox_MODE_SEL.currentData()[0] == JOG_CONTINUOUS :
            return 

        _selected_joint = self._dict_join_and_direction[self.sender()][0]
        _selected_direction = self._dict_join_and_direction[self.sender()][1]

        _selected_velocity = self.horizontalSlider_FEEDRATE.value()
        _velocity = _selected_velocity * _selected_direction #choosed by sender
        _selected_distance = self.comboBox_MODE_SEL()[1]

        #raise JOG command - incremental
        self._controller.onJogCommand(JOG_INCREMENT, _selected_joint,_selected_velocity,_selected_distance)
        pass

    #The continoues mode - GO
    def onJogButtonPressed(self):
        if self.comboBox_MODE_SEL.currentData()[0] == JOG_INCREMENT :
            return 

        _selected_joint = self._dict_join_and_direction[self.sender()][0]
        _selected_direction = self._dict_join_and_direction[self.sender()][1]

        _selected_velocity = self.horizontalSlider_FEEDRATE.value()
        _velocity = _selected_velocity * _selected_direction #choosed by sender
        #raise JOG command - incremental
        self._controller.onJogCommand(JOG_CONTINUOUS,_selected_joint,_selected_velocity)
        pass

    #The continuoues mode - Stop
    def onJogButtonReleased(self):
        _selected_joint = self._dict_join_and_direction[self.sender()][0]
        self._controller.onJogCommand(JOG_STOP,_selected_joint)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass