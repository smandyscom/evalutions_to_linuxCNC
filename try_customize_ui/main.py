
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
sys.path.append(r'.qt_for_python\uic')
sys.path.append(r'.qt_for_python/uic')
import typing

from PyQt5.QtCore import QModelIndex, QObject, pyqtSlot, qAbs, Qt, pyqtSignal, pyqtSlot, QItemSelection
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget,QPushButton,QLineEdit


import pointtable
from random import random

cwd = getcwd()

from mainwindow import Ui_MainWindow
from controller import Controller, JOG_STOP, JOG_CONTINUOUS, JOG_INCREMENT,TaskState

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.setupUi(self) # statical way to load .ui file, have to use pyuic.exe to generate ui.py first
        self.tableView.setModel(pointtable.Model)
        self._controller = Controller(self)

        self.initTab1()
        self.initTab2()
        pass

    def initTab1(self):
        self.pushButton_TEACH.setEnabled(False)
        self.tableView.selectionModel().selectionChanged.connect(self.onTableViewSelected)
        self.tableView.selectionModel().selectionChanged.connect(self._controller.onSelectedItemChanged)

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
        for key in self._dict_join_and_direction.keys():
            key.clicked.connect(self.onJogButtonClicked)
            key.pressed.connect(self.onJogButtonPressed)
            key.released.connect(self.onJogButtonReleased)
        
        """ link signal TO Controller """
        for homebutton in [self.pushButton_JOG_X_H,self.pushButton_JOG_Y_H,self.pushButton_JOG_Z_H]:
            homebutton.clicked.connect(self._controller.onHomeCommand)
        
        self.pushButton_TEACH.clicked.connect(self._controller.onTeachButtonClicked)
        self.pushButton_REPLAY.clicked.connect(self._controller.onReplayButtonClicked)

        self.pushButton_SRV_ON.toggled.connect(self._controller.onEnabledCommand)
        self.pushButton_UNLLOCK.clicked.connect(self._controller.onESTOPCommand)

        self.pushButton_GO.clicked.connect(self.onDirectGoClicked) #TODO, when to enable lineEdit to be changed?
        
        """ link signal FROM Controller """
        self._controller.updateCurrentPositions[0].updatePost.connect(self.lineEdit_CUR_X.setText)
        self._controller.updateCurrentPositions[1].updatePost.connect(self.lineEdit_CUR_Y.setText)
        self._controller.updateCurrentPositions[2].updatePost.connect(self.lineEdit_CUR_Z.setText)

        self._controller.updateNativeStatus['task_mode'].updatePost.connect(lambda x: self.label_TASK_MODE.setText(str(x)))
        self._controller.updateNativeStatus['task_state'].updatePost.connect(lambda x : self.label_TASK_STATE.setText(str(x)))
        self._controller.updateNativeStatus['task_state'].updatePost.connect(lambda x : (self.pushButton_UNLLOCK.setChecked(x==TaskState.STATE_ESTOP.value)))
        self._controller.updateNativeStatus['task_state'].updatePost.connect(lambda x : (self.pushButton_SRV_ON.setChecked(x==TaskState.STATE_ON.value)))
        self._controller.updateNativeStatus['task_state'].updatePost.connect(lambda x : (self.pushButton_SRV_ON.setEnabled(x>=TaskState.STATE_ESTOP_RESET.value)))


        the_list = self.findChildren(QPushButton)
        for excepts in [self.pushButton_SRV_ON,self.pushButton_UNLLOCK,self.pushButton_JOG_X_H,self.pushButton_JOG_Y_H,self.pushButton_JOG_Z_H,self.pushButton_TEACH]:
            the_list.remove(excepts)
        the_list += self.findChildren(QLineEdit)
        for widget in the_list:
            self._controller.updateCombinedStatus['is_mdi_ok'].updatePost.connect(widget.setEnabled)        

        pass

    def initTab2(self):
        #populate attributes
        for item in self._controller._hardware_gate.linuxcnc_stats_attr_list:
            self.comboBox_ATTR_SELECTION.addItem(str(item))

        self._per_connection = None

        self.comboBox_ATTR_SELECTION.currentTextChanged.connect(self.onAttrSelectionChanged)
        pass

    @pyqtSlot(str)
    def onAttrSelectionChanged(self,key : str):
        #disconnect per link
        if self._per_connection is not None :
            QObject.disconnect(self._per_connection)
        
        #create new link
        if key in self._controller.updateNativeStatus.keys():
            self._per_connection = self._controller.updateNativeStatus[key].updatePost.connect(self.onUpdateStatVal)

        pass

    @pyqtSlot(object)
    def onUpdateStatVal(self,text):
        self.label_STAT_VAL.setText(str(text))
        pass

    @pyqtSlot(QItemSelection,QItemSelection)
    def onTableViewSelected(self,selected : QItemSelection,deselected : QItemSelection):
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
    @pyqtSlot()
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
    @pyqtSlot()
    def onJogButtonReleased(self):
        _selected_joint = self._dict_join_and_direction[self.sender()][0]
        self._controller.onJogCommand(JOG_STOP,_selected_joint)
        pass

    @pyqtSlot()
    def onDirectGoClicked(self):
        _coords = [float(x.text()) for x in self.findChildren(QLineEdit)]
        self._controller.onMDIG00(_coords)
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass