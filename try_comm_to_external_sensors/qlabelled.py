from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QLabel

#Inspired by
#https://forum.qt.io/topic/101648/how-to-create-simply-virtual-led-indicator/3

class QLabelLed(QLabel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

    @pyqtSlot(bool)
    def onStateChanged(self,state):
        if state :
            self.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:1, y2:1, stop:0 rgba(20, 252, 7, 255), stop:1 rgba(25, 134, 5, 255));')
            pass
        else :
            self.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:0.92, y2:0.988636, stop:0 rgba(255, 12, 12, 255), stop:0.869347 rgba(103, 0, 0, 255));')
            pass
        pass

    pass