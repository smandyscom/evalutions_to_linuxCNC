
import os
from os import getcwd
env = os.environ 
env.setdefault("QT_DEBUG_PLUGINS","1")

import sys
sys.path.append(r'.qt_for_python\uic')
sys.path.append(r'.qt_for_python/uic')
import typing

from PyQt5.QtCore import QModelIndex, qAbs
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from os.path import exists,join

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
        model.select()

        self.setupUi(self) # statical way to load .ui file, have to use pyuic.exe to generate ui.py first

        self.tableView.setModel(model)

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() #message loop start running
    sys.exit(app.exec())
    pass