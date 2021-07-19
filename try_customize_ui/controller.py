import typing
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot, QItemSelection
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget

from random import random
import pointtable
from hardwaregate import HardwardGate


JOG_STOP = 0
JOG_CONTINUOUS = 1
JOG_INCREMENT = 2

class SignalCarrier(QObject):
    updatePost = pyqtSignal(object)

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)


class Controller(QObject):

    updateInPosition = pyqtSignal(bool)

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)

        self._hardware_gate = HardwardGate()


        dof3 = range(0,3)
        dof2 = range(0,2)
        self.updateCurrentPositions = [SignalCarrier(self) for x in dof3]
        
        #Timer to update/run sequence
        self.qTimer = QTimer(parent=self)
        self.qTimer.timeout.connect(self.onUpdate)
        self.qTimer.setInterval(200)
        self.qTimer.start()

        self._tuple_substract = lambda x,y: (x[0]-y[0],x[1]-y[1])

        self._model = pointtable.Model
        self._coordinate_dict = {
            'X':    0,
            'Y':    1,
            'Z':    2,
            }
        
        self._status_dict = {}
        self.updateStatus = {}
        for x in ['estop','enabled','homed','joints','interp_state']:
            self._status_dict[x] = None
        for key in self._status_dict.keys():
            self.updateStatus[key] = SignalCarrier(self)


        pass

    #When modelview changed modelindex, cache
    @pyqtSlot(QItemSelection,QItemSelection)
    def onSelectedItemChanged(self,selected : QItemSelection, deselected : QItemSelection):
        self._selectedRow = selected.indexes()[0].row() #choose the first of selected row
        self._selectedRecord = self._model.record(self._selectedRow)
        pass

    #Fetch value from machine then write-in
    @pyqtSlot()
    def onTeachButtonClicked(self):
        for key in self._coordinate_dict:
            self._selectedRecord.setValue(key,self._mach_positions[self._coordinate_dict[key]])
        self._model.setRecord(self._selectedRow,self._selectedRecord)
        pass

    @pyqtSlot()
    def onReplayButtonClicked(self):
        commandPosition = [float()]*3
        for key in self._coordinate_dict:
            commandPosition[self._coordinate_dict[key]] = float(self._selectedRecord.value(key))
        #trigger or MDI to drive
        self.onMDIG00(commandPosition)
        pass

    @pyqtSlot()
    def onUpdate(self):
        self._mach_positions = [self._hardware_gate.hal_read_pin('joint.{}.pos-fb'.format(x)) for x in range(0,3)]

        [self.updateCurrentPositions[self._mach_positions.index(x)].updatePost.emit(str(x)) for x in self._mach_positions]

        '''Timed signals'''
        #raise in position signal
        self.updateInPosition.emit(bool(self._hardware_gate.linuxcnc_read_stat('inpos')))

        #update status values
        for key in self._status_dict.keys():
            self._status_dict[key] = self._hardware_gate.linuxcnc_read_stat(key)
            self.updateStatus[key].updatePost.emit(self._status_dict[key])
        pass

        """ for index in range(len(self.updateCurrentPositions)):
            value = self._mach_position[index]
            self.updateCurrentPositions[index].updatePost.emit(str(value)) """
        
        pass

    @pyqtSlot(list)
    def onMDIG00(self,command_pos=[0,0,0]):
        """ def ok_for_mdi():
        s.poll()
            return not s.estop and s.enabled and (s.homed.count(1) == s.joints) and (s.interp_state == linuxcnc.INTERP_IDLE) """

        if self._ismdiok():
            mdi_command = 'G00 X{} Y{} Z{}'.format(*command_pos)
            self._hardware_gate.linuxcnc_write_command('mdi',mdi_command)
        pass

    def onJogCommand(self,mode,joint,velocity=0,distance=0):
        self._hardware_gate.linuxcnc_write_command('jog',mode,True,joint,velocity,distance)
        pass

    def _ismdiok(self):
        return bool(self._status_dict['estop']) and bool(self._status_dict['enabled']) and (len(self._status_dict['homed']) == self._status_dict['joints']) and self._status_dict['interp_state']==0    

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

    
