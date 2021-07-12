
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
sys.path.append(r'.qt_for_python\uic')
sys.path.append(r'.qt_for_python/uic')
import typing

from PyQt5.QtCore import QModelIndex, qAbs, Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PyQt5.QtSql import QSqlRecord, QSqlTableModel,QSqlDatabase
from os.path import exists,join

from random import random

cwd = getcwd()

from mainwindow import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        db = QSqlDatabase.addDatabase('QSQLITE')
        path = 'machine.db'
        if not exists(path):
            print('failed')

        db.setDatabaseName(path)
        if not db.open() :
            print('failed')

        model = QSqlTableModel(self)
        model.setTable('pointtable')
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        model.select()

        self.setupUi(self) # statical way to load .ui file, have to use pyuic.exe to generate ui.py first

        #self.tableView.setModel(model)

        ''' model.setRecord(0,model.record(0).setValue('X',random()))
        model.setRecord(0,model.record(1).setValue('Y',random())) '''
        index = model.index(1,2)
        row = index.row()
        model.setData(index,random(),Qt.EditRole) 
        #Q : why all row were set??
        #A : without primary key would result such error.

        if model.submitAll() :
            model.database().commit()
        else : 
            error = model.lastError().text()

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass