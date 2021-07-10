from PyQt5.QtCore import QAbstractTableModel,QModelIndex, QVariant,Qt
from random import random



class qMyPosTableModel(QAbstractTableModel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        #Customed data structure, list with entity of tuple-4

        self._section = {0:'X_MACH',
        1:'Y_MACH',
        2:'X_VISION',
        3:'Y_VISION'}
        self._points = [tuple([float()]*4)]*16
        self._points[10] = (5,5,5,5) # for test

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self,index_point=(0,tuple([random()]*4))):
        self._points[index_point[0]]= index_point[1]

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self._points)

    def columnCount(self, parent: QModelIndex) -> int:
        return len(self._points[0])

    def data(self, index: QModelIndex, role: int):
        #return super().data(index, role=role)
        if role == Qt.DisplayRole:
            return self._points[index.row()][index.column()]
        return QVariant()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) :
        #return super().headerData(section, orientation, role=role)
        ''' if section<len(self._section):
            return self._section[section] '''

        if orientation==Qt.Horizontal and role ==Qt.DisplayRole:
            return self._section[section]
        return super().headerData(section, orientation, role=role)
