import typing
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


from random import random

from switcher import Swither
from qmymodel import qMyPosTableModel

class SignalCarrier(QObject):
    updatePost = pyqtSignal(str)

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)


class Controller(QObject):

    #Signals to update UI (Need to shared among instances?)
    '''updateCurrentPostions = [pyqtSignal(str)]*3 #wrong way'''
    """ updateCurrentPositions = [SignalCarrier()]*3
    updateVisionPositions = [SignalCarrier()]*3
    updateCalculatedPositions = [SignalCarrier()]*3
 """
    updateTriggerSignal = pyqtSignal(bool) #QLabel should be promoted to have corrsponding slot
    updatePosIndex = pyqtSignal(str)
    updatePosTable = pyqtSignal(int,str) #index, and position content

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)

        self._interface = Swither()
        self._state = 0

        self.model = qMyPosTableModel()
        #model.points = (1,(1,2,3,4))

        dof3 = range(0,3)
        dof2 = range(0,2)
        self.updateCurrentPositions = [SignalCarrier(self) for x in dof3]
        self.updateVisionPositions = [SignalCarrier(self) for x in dof2]
        self.updateWkCoord = [SignalCarrier(self) for x in dof3]
        # wrong way which would multiple handles to link only one instance 
        # self.updateVisionPositions = [SignalCarrier(self)]*3 
        

        #Timer to update/run sequence
        self.qTimer = QTimer(parent=self)
        self.qTimer.timeout.connect(self.onTimerTimeout_run_handshake)
        self.qTimer.timeout.connect(self.onTimerTimeout_dice_values)
        self.qTimer.timeout.connect(self.onTimerTimeout_update_ui)
        self.qTimer.setInterval(200)
        self.qTimer.start()

        

        pass

    @pyqtSlot()
    def onButtonAckClicked(self):
        self._interface.write_acknowledge(not self._interface.read_ackowledge()) # flip the signal
        pass

    def onTimerTimeout_dice_values(self):
        self._interface.dice_values()
        pass

    def onTimerTimeout_update_ui(self):
        self._mach_positions = self._interface.read_pos_current_mach()
        for index in range(len(self.updateCurrentPositions)):
            value = self._mach_positions[index]
            self.updateCurrentPositions[index].updatePost.emit(str(value))
        
        self.updatePosIndex.emit(str(self._interface.read_pos_index()))
        self.updateTriggerSignal.emit(self._interface.read_trigger())
        

    #event handler to QTimer
    def onTimerTimeout_run_handshake(self):
        if self._state == 0 and self._interface.read_trigger():
            self._state = 100

        elif self._state == 100 and self._interface.read_ackowledge():

            pos_index = self._interface.read_pos_index() #read from CNC
            self._mach_positions = self._interface.read_pos_current_mach()
            #Simulation to TRIGGER Vision capture process
            vision_pos = self.onSimuTriggerVision()

            #write into MODEL according to POS_INDEX
            if pos_index >= 0:
                given_tuple = tuple(self._mach_positions[0:2]+vision_pos[0:2])
                self.model.points = (int(pos_index),given_tuple)

            #update to see if any have positve result
            result = self.evaluateToolCoordinate()
            result = result or self.evaluateWorkpieceCoordinate()

            #TODO, result set flag

            self._state = 200

        elif self._state == 200 and self._interface.read_trigger()==False:
            self._interface.write_acknowledge(False)
            self._state = 0 # to await signal rewind
        pass

    def onSimuTriggerVision(self):
        self.__vision_positions = [x+random() for x in self._mach_positions]
        #TO update Vision Position
        for index in range(len(self.updateVisionPositions)):
            self.updateVisionPositions[index].updatePost.emit(str(self.__vision_positions[index]))
        return self.__vision_positions

    #From WK table to evaluate
    def evaluateWorkpieceCoordinate(self):
        ''' self._calculated = [x+random() for x in self.__vision_positions]
        #TO update Calculated Position
        for index in range(len(self.updateWkCoord)):
            self.updateWkCoord[index].updatePost.emit(str(self._calculated[index])) '''
        pass

    #From CALI table to evaluate
    def evaluateToolCoordinate(self):
        pass
    
