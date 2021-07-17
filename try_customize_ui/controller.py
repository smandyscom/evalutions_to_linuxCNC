import typing
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot, QItemSelection
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget

from random import random
import pointtable


JOG_STOP = 0
JOG_CONTINUOUS = 1
JOG_INCREMENT = 2

class SignalCarrier(QObject):
    updatePost = pyqtSignal(str)

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)


class Controller(QObject):

    updateTriggerSignal = pyqtSignal(bool) #QLabel should be promoted to have corrsponding slot
    updatePosIndex = pyqtSignal(str)
    updatePosTable = pyqtSignal(int,str) #index, and position content

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)

        dof3 = range(0,3)
        dof2 = range(0,2)
        self.updateCurrentPositions = [SignalCarrier(self) for x in dof3]
        self.updateVisionPositions = [SignalCarrier(self) for x in dof2]

        # wrong way which would multiple handles to link only one instance 
        # self.updateVisionPositions = [SignalCarrier(self)]*3 
        
        #Timer to update/run sequence
        self.qTimer = QTimer(parent=self)
        self.qTimer.timeout.connect(self.onTimerTimeout_update_ui)
        self.qTimer.setInterval(200)
        self.qTimer.start()

        self._tuple_substract = lambda x,y: (x[0]-y[0],x[1]-y[1])

        self._model = pointtable.Model
        self._dict = {'X': 0,
        'Y':1,
        'Z':2}

        pass

    #When modelview changed modelindex, cache
    @pyqtSlot()
    def onSelectedItemChanged(self,selected : QItemSelection, deselected : QItemSelection):
        self._selectedRow = selected.indexes[0].row()
        self._selectedRecord = self._model.record(self._selectedRow)
        pass

    #Fetch value from machine then write-in
    @pyqtSlot()
    def onTeachButtonClicked(self):
        

        for key in self._dict:
            self._selectedRecord.setValue(key,self._mach_position[self._dict[key]])
        self._model.setRecord(self._selectedRow,self._selectedRecord)
        pass

    @pyqtSlot()
    def onReplayButtonClicked(self):
        for key in self._dict:
            self._command_position[self._dict[key]] = float(self._selectedRecord.value(key))
        #TODO , trigger or MDI to drive
        pass

    """ def onTimerTimeout_dice_values(self):
        self._interface.dice_values()
        pass """

    def onTimerTimeout_update_ui(self):
        #self._mach_positions = self._interface.read_pos_current_mach()
        for index in range(len(self.updateCurrentPositions)):
            value = self._mach_position[index]
            self.updateCurrentPositions[index].updatePost.emit(str(value))
        
        self.updatePosIndex.emit(str(self._interface.read_pos_index()))
        self.updateTriggerSignal.emit(self._interface.read_trigger())
        pass


    def onJogCommand(self,mode,joint,velocity=0,distance=0):
        pass

    """  #event handler to QTimer
    def onTimerTimeout_run_handshake(self):
        if self._state == 0 and self._interface.read_trigger():
            self._state = 100

        elif self._state == 100 and self._interface.read_ackowledge():

            pos_index = self._interface.read_pos_index() #read from CNC
            self._mach_position = self._interface.read_pos_current_mach()
            #Simulation to TRIGGER Vision capture process
            vision_pos = self.onSimuTriggerVision()

            #write into MODEL according to POS_INDEX
            if pos_index >= 0:
                given_tuple = tuple(self._mach_position[0:2]+vision_pos[0:2])
                self.model.points = (int(pos_index),given_tuple)

            #update to see if any have positve result
            result = []
            update_to = self.updateWkCoord
            if pos_index in range(0,9):
                result = self.evaluateToolCoordinate()
                update_to = self.updateToolCoord
            elif pos_index in range(9,13):
                result =  self.evaluateWorkpieceCoordinate()
                update_to = self.updateWkCoord
                

            self._interface.write_pos_comp_mach(list(result))
            [update_to[x].updatePost.emit(str(result[x])) for x in range(len(result))]

            self._state = 200

        elif self._state == 200 and self._interface.read_trigger()==False:
            self._interface.write_acknowledge(False)
            self._state = 0 # to await signal rewind
        pass """

    
