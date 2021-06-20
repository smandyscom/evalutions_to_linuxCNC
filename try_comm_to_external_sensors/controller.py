import typing
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


from random import random

from switcher import Swither

class Controller(QObject):
    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)

        self.__interface__ = Swither()
        self.__state__ = 0

        self.tableWidget=QTableWidget(self) #dummy one, need to be linked
        
        #Signals to update UI
        self.updateCurrentPostions = [pyqtSignal(str)]*3
        self.updateTriggerSignal = pyqtSignal(bool)

        pass

    def onTimerTimeout_update_ui(self):
        pass

    #event handler to QTimer
    def onTimerTimeout_run_handshake(self):
        if self.__state__ == 0 and self.__interface__.read_trigger():
            self.__state__ = 100

        elif self.__state__ == 100:
            pos_index = self.__interface__.read_pos_index() #read from CNC
            if pos_index == -1:
                pass
            else:
                self.onTriggerToCalibration(self,pos_index)

            self.__interface__.write_acknowledge(True)
            self.__state__ = 200

        elif self.__state__ == 200 and self.__interface__.read_trigger==False:
            self.__interface__.write_acknowledge(False)
            self.__state__ = 0 # to await signal rewind
        pass

    def onTriggerToCalibration(self,pos_index=0):
        #when received pos_index from 0-8
        #To change model?
        mach_positions = self.__interface__.read_pos_current_mach()

        for i in range(0,2):
            self.tableWidget.setItem(pos_index,i,QTableWidgetItem(mach_positions[i]))

        #Simulation to TRIGGER Vision capture process
        vision_positions = [x+random() for x in mach_positions ]

        for i in range(3,5):
            self.tableWidget.setItem(pos_index,i,QTableWidgetItem(vision_positions[i]))

        pass