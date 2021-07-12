from PyQt5.QtSql import QSqlRecord, QSqlTableModel,QSqlDatabase
from os.path import exists,join

_db = QSqlDatabase.addDatabase('QSQLITE')
path = 'machine.db'
if not exists(path):
    print('failed')

_db.setDatabaseName(path)
if not _db.open() :
    print('failed')

_model = QSqlTableModel(None)
_model.setTable('pointtable')
_model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
_model.select()

def __getattr__(name):
    if name=='Model':
        return _model
    return None

''' index = model.index(2,3)
row = index.row()
model.setData(index,random(),Qt.EditRole) 

record = model.record(2)
record.setValue('X',random())
model.setRecord(2,record) '''

#Q : why all row were set??
#A : without primary key would result such error.

''' if model.submitAll() :
        model.database().commit()
    else : 
        error = model.lastError().text() '''