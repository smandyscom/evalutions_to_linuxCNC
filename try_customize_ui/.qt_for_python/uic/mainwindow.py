# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\smand\OneDrive\文件\GitHub\evalutions_to_linuxCNC\try_customize_ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_TASK_MODE = QtWidgets.QLabel(self.tab)
        self.label_TASK_MODE.setObjectName("label_TASK_MODE")
        self.gridLayout_4.addWidget(self.label_TASK_MODE, 0, 1, 1, 1)
        self.label_TASK_STATE = QtWidgets.QLabel(self.tab)
        self.label_TASK_STATE.setObjectName("label_TASK_STATE")
        self.gridLayout_4.addWidget(self.label_TASK_STATE, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_MOTION_MODE = QtWidgets.QLabel(self.tab)
        self.label_MOTION_MODE.setObjectName("label_MOTION_MODE")
        self.gridLayout_4.addWidget(self.label_MOTION_MODE, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.horizontalLayout_10.addLayout(self.gridLayout_4)
        self.pushButton_UNLLOCK = QtWidgets.QPushButton(self.tab)
        self.pushButton_UNLLOCK.setCheckable(True)
        self.pushButton_UNLLOCK.setChecked(False)
        self.pushButton_UNLLOCK.setObjectName("pushButton_UNLLOCK")
        self.horizontalLayout_10.addWidget(self.pushButton_UNLLOCK)
        self.pushButton_SRV_ON = QtWidgets.QPushButton(self.tab)
        self.pushButton_SRV_ON.setCheckable(True)
        self.pushButton_SRV_ON.setObjectName("pushButton_SRV_ON")
        self.horizontalLayout_10.addWidget(self.pushButton_SRV_ON)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_TEACH = QtWidgets.QPushButton(self.tab)
        self.pushButton_TEACH.setObjectName("pushButton_TEACH")
        self.horizontalLayout_3.addWidget(self.pushButton_TEACH)
        self.pushButton_REPLAY = QtWidgets.QPushButton(self.tab)
        self.pushButton_REPLAY.setObjectName("pushButton_REPLAY")
        self.horizontalLayout_3.addWidget(self.pushButton_REPLAY)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEdit_CUR_X = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_CUR_X.setObjectName("lineEdit_CUR_X")
        self.horizontalLayout_2.addWidget(self.lineEdit_CUR_X)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lineEdit_CUR_Y = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_CUR_Y.setObjectName("lineEdit_CUR_Y")
        self.horizontalLayout_7.addWidget(self.lineEdit_CUR_Y)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lineEdit_CUR_Z = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_CUR_Z.setObjectName("lineEdit_CUR_Z")
        self.horizontalLayout_6.addWidget(self.lineEdit_CUR_Z)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.pushButton_GO = QtWidgets.QPushButton(self.tab)
        self.pushButton_GO.setObjectName("pushButton_GO")
        self.verticalLayout_2.addWidget(self.pushButton_GO)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.comboBox_MODE_SEL = QtWidgets.QComboBox(self.tab)
        self.comboBox_MODE_SEL.setObjectName("comboBox_MODE_SEL")
        self.comboBox_MODE_SEL.addItem("")
        self.comboBox_MODE_SEL.addItem("")
        self.comboBox_MODE_SEL.addItem("")
        self.comboBox_MODE_SEL.addItem("")
        self.comboBox_MODE_SEL.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_MODE_SEL)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.horizontalSlider_FEEDRATE = QtWidgets.QSlider(self.tab)
        self.horizontalSlider_FEEDRATE.setProperty("value", 50)
        self.horizontalSlider_FEEDRATE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_FEEDRATE.setObjectName("horizontalSlider_FEEDRATE")
        self.horizontalLayout_9.addWidget(self.horizontalSlider_FEEDRATE)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_JOG_X_N = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_X_N.setObjectName("pushButton_JOG_X_N")
        self.horizontalLayout.addWidget(self.pushButton_JOG_X_N)
        self.pushButton_JOG_X_P = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_X_P.setObjectName("pushButton_JOG_X_P")
        self.horizontalLayout.addWidget(self.pushButton_JOG_X_P)
        self.pushButton_JOG_X_H = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_X_H.setObjectName("pushButton_JOG_X_H")
        self.horizontalLayout.addWidget(self.pushButton_JOG_X_H)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.pushButton_JOG_Y_N = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_Y_N.setObjectName("pushButton_JOG_Y_N")
        self.horizontalLayout_4.addWidget(self.pushButton_JOG_Y_N)
        self.pushButton_JOG_Y_P = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_Y_P.setObjectName("pushButton_JOG_Y_P")
        self.horizontalLayout_4.addWidget(self.pushButton_JOG_Y_P)
        self.pushButton_JOG_Y_H = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_Y_H.setObjectName("pushButton_JOG_Y_H")
        self.horizontalLayout_4.addWidget(self.pushButton_JOG_Y_H)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.pushButton_JOG_Z_N = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_Z_N.setObjectName("pushButton_JOG_Z_N")
        self.horizontalLayout_5.addWidget(self.pushButton_JOG_Z_N)
        self.pushButton_JOG_Z_P = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_Z_P.setObjectName("pushButton_JOG_Z_P")
        self.horizontalLayout_5.addWidget(self.pushButton_JOG_Z_P)
        self.pushButton_JOG_Z_H = QtWidgets.QPushButton(self.tab)
        self.pushButton_JOG_Z_H.setObjectName("pushButton_JOG_Z_H")
        self.horizontalLayout_5.addWidget(self.pushButton_JOG_Z_H)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.comboBox_ATTR_SELECTION = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ATTR_SELECTION.sizePolicy().hasHeightForWidth())
        self.comboBox_ATTR_SELECTION.setSizePolicy(sizePolicy)
        self.comboBox_ATTR_SELECTION.setObjectName("comboBox_ATTR_SELECTION")
        self.horizontalLayout_12.addWidget(self.comboBox_ATTR_SELECTION)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.label_STAT_VAL = QtWidgets.QLabel(self.tab_2)
        self.label_STAT_VAL.setObjectName("label_STAT_VAL")
        self.horizontalLayout_11.addWidget(self.label_STAT_VAL)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_TASK_MODE.setText(_translate("MainWindow", "TextLabel"))
        self.label_TASK_STATE.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TASK_MODE"))
        self.label_4.setText(_translate("MainWindow", "TASK_STATE"))
        self.label_MOTION_MODE.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "MOTION_MODE"))
        self.pushButton_UNLLOCK.setText(_translate("MainWindow", "ESTOP"))
        self.pushButton_SRV_ON.setText(_translate("MainWindow", "ENABLE"))
        self.label_12.setText(_translate("MainWindow", "POINTS_TABLE"))
        self.pushButton_TEACH.setText(_translate("MainWindow", "TEACH"))
        self.pushButton_REPLAY.setText(_translate("MainWindow", "REPLAY"))
        self.label_8.setText(_translate("MainWindow", "MONITOR_DIRECT_GO"))
        self.label_9.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.label_10.setText(_translate("MainWindow", "Z"))
        self.pushButton_GO.setText(_translate("MainWindow", "GO"))
        self.label_7.setText(_translate("MainWindow", "JOG_PANEL"))
        self.label_13.setText(_translate("MainWindow", "MODE"))
        self.comboBox_MODE_SEL.setItemText(0, _translate("MainWindow", "Continous"))
        self.comboBox_MODE_SEL.setItemText(1, _translate("MainWindow", "1mm"))
        self.comboBox_MODE_SEL.setItemText(2, _translate("MainWindow", "0.1mm"))
        self.comboBox_MODE_SEL.setItemText(3, _translate("MainWindow", "0.01mm"))
        self.comboBox_MODE_SEL.setItemText(4, _translate("MainWindow", "0.001mm"))
        self.label_14.setText(_translate("MainWindow", "FEEDRATE"))
        self.label.setText(_translate("MainWindow", "X"))
        self.pushButton_JOG_X_N.setText(_translate("MainWindow", "-"))
        self.pushButton_JOG_X_P.setText(_translate("MainWindow", "+"))
        self.pushButton_JOG_X_H.setText(_translate("MainWindow", "HOME"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.pushButton_JOG_Y_N.setText(_translate("MainWindow", "-"))
        self.pushButton_JOG_Y_P.setText(_translate("MainWindow", "+"))
        self.pushButton_JOG_Y_H.setText(_translate("MainWindow", "HOME"))
        self.label_6.setText(_translate("MainWindow", "Z"))
        self.pushButton_JOG_Z_N.setText(_translate("MainWindow", "-"))
        self.pushButton_JOG_Z_P.setText(_translate("MainWindow", "+"))
        self.pushButton_JOG_Z_H.setText(_translate("MainWindow", "HOME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ControlPanel"))
        self.label_15.setText(_translate("MainWindow", "Attribute"))
        self.label_16.setText(_translate("MainWindow", "Value"))
        self.label_STAT_VAL.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Attributes"))
