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
            'Z':    2
            }
        
        self._native_status_dict = {}
        self.updateNativeStatus = {}
        self.updateCombinedStatus = {}

        #TODO , should follow the hardward linuxcnc attributes given
        for x in self._hardware_gate.linuxcnc_stats_attr_list:
            self._native_status_dict[x] = None
        for key in self._native_status_dict.keys():
            self.updateNativeStatus[key] = SignalCarrier(self)

        self._combined_status_dict = {
            'is_mdi_ok' : self._ismdiok
        }
        for key in self._combined_status_dict.keys():
            self.updateCombinedStatus[key] = SignalCarrier(self)

        pass

    #When modelview changed modelindex, cache
    @pyqtSlot(QItemSelection,QItemSelection)
    def onSelectedItemChanged(self,selected : QItemSelection, deselected : QItemSelection):
        if len(selected.indexes()) > 0:
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
        #update status values
        for key in self._native_status_dict.keys():
            self._native_status_dict[key] = self._hardware_gate.linuxcnc_read_stat(key)
            self.updateNativeStatus[key].updatePost.emit(self._native_status_dict[key])
            pass

        for key in self._combined_status_dict.keys():
            self.updateCombinedStatus[key].updatePost.emit(self._combined_status_dict[key]())
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

    @pyqtSlot(int,int,float,float)
    def onJogCommand(self,mode,joint,velocity=0,distance=0):
        self._hardware_gate.linuxcnc_write_command('jog',mode,True,joint,velocity,distance)
        pass

    @pyqtSlot()
    def onHomeCommand(self):
        #pick first occurance
        _key = next(key for key in self._coordinate_dict.keys() if key in self.sender().objectName())
        _joint = self._coordinate_dict[_key]
        self._hardware_gate.linuxcnc_write_command('home',_joint)
        pass

    """ def onESTOPCommand(self):
        pass

    def onAllEnabledCommand(self):
        pass """

    def _ismdiok(self):
        return bool(self._native_status_dict['estop']) and bool(self._native_status_dict['enabled']) and (len(self._native_status_dict['homed']) == self._native_status_dict['joints']) and self._native_status_dict['interp_state']==0    
