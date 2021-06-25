import typing
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


from random import random

from switcher import Swither


class SignalCarrier(QObject):
    updatePost  = pyqtSignal(str)

class Controller(QObject):

    #Signals to update UI (Need to shared among instances?)
    '''updateCurrentPostions = [pyqtSignal(str)]*3 #wrong way'''
    updateCurrentPositions = [SignalCarrier()]*3
    updateVisionPositions = [SignalCarrier()]*3
    updateCalculatedPositions = [SignalCarrier()]*3

    updateTriggerSignal = pyqtSignal(bool) #QLabel should be promoted to have corrsponding slot
    updatePosIndex = pyqtSignal(str)

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)

        self.__interface__ = Swither()
        self.__state__ = 0

        self.tableWidget=QTableWidget() #dummy one, need to be linked

        #Timer to update/run sequence
        self.qTimer = QTimer(parent=self)
        #self.qTimer.timeout.connect(self.onTimerTimeout_run_handshake)
        #self.qTimer.timeout.connect(self.onTimerTimeout_dice_values)
        self.qTimer.timeout.connect(self.onTimerTimeout_update_ui)
        self.qTimer.setInterval(200)
        self.qTimer.start()

        #Slot to received changes from UI

        pass

    @pyqtSlot()
    def onButtonAckClicked(self):
        self.__interface__.write_acknowledge(not self.__interface__.read_ackowledge()) # flip the signal
        pass

    def onTimerTimeout_dice_values(self):
        self.__interface__.dice_values()
        pass

    def onTimerTimeout_update_ui(self):
        self.__mach_positions = self.__interface__.read_pos_current_mach()
        for index in range(len(self.updateCurrentPositions)):
            value = self.__mach_positions[index]
            self.updateCurrentPositions[index].updatePost.emit(str(value))
        self.updatePosIndex.emit(str(self.__interface__.read_pos_index()))
        self.updateTriggerSignal.emit(self.__interface__.read_trigger())
        

    #event handler to QTimer
    def onTimerTimeout_run_handshake(self):
        if self.__state__ == 0 and self.__interface__.read_trigger():
            self.__state__ = 100

        elif self.__state__ == 100 and self.__interface__.read_ackowledge():
            pos_index = self.__interface__.read_pos_index() #read from CNC
            if pos_index == -1:
                self.onTriggerToOperation()
            else:
                self.onTriggerToCalibration(pos_index)

            #self.__interface__.write_acknowledge(True)
            self.__state__ = 200

        elif self.__state__ == 200 and self.__interface__.read_trigger()==False:
            self.__interface__.write_acknowledge(False)
            self.__state__ = 0 # to await signal rewind
        pass

    def onTriggerToCalibration(self,pos_index=0):
        #when received pos_index from 0-8
        #To change model?
        self.__mach_positions = self.__interface__.read_pos_current_mach()

        for i in range(len(self.__mach_positions)):
            self.tableWidget.setItem(pos_index,i,QTableWidgetItem(str(self.__mach_positions[i])))

        #Simulation to TRIGGER Vision capture process
        self.onSimuTriggerVision(self.__mach_positions)
        for i in range(len(self.__vision_positions)):
            self.tableWidget.setItem(pos_index,i+3,QTableWidgetItem(str(self.__vision_positions[i])))

        pass

    def onTriggerToOperation(self):
        self.__mach_positions = self.__interface__.read_pos_current_mach()
        self.onSimuTriggerVision()
        self.onSimuTriggerCalculated()
        pass

    def onSimuTriggerVision(self):
        self.__vision_positions = [x+random() for x in self.__mach_positions]
        #TO update Vision Position
        for index in range(len(self.updateVisionPositions)):
            self.updateVisionPositions[index].updatePost.emit(str(self.__vision_positions[index]))
        pass

    def onSimuTriggerCalculated(self):
        self.__calculated = [x+random() for x in self.__vision_positions]
        #TO update Calculated Position
        for index in range(len(self.updateCalculatedPositions)):
            self.updateCalculatedPositions[index].updatePost.emit(str(self.__calculated[index]))
        pass
