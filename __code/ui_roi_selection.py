# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/notebooks/ui/ui_roi_selection.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(800, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_roi = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_roi.sizePolicy().hasHeightForWidth())
        self.table_roi.setSizePolicy(sizePolicy)
        self.table_roi.setMinimumSize(QtCore.QSize(300, 0))
        self.table_roi.setMaximumSize(QtCore.QSize(300, 16777215))
        self.table_roi.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_roi.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_roi.setObjectName("table_roi")
        self.table_roi.setColumnCount(4)
        self.table_roi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_roi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_roi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_roi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_roi.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.table_roi)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.remove_roi_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.remove_roi_button.setFont(font)
        self.remove_roi_button.setObjectName("remove_roi_button")
        self.horizontalLayout_3.addWidget(self.remove_roi_button)
        self.add_roi_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.add_roi_button.setFont(font)
        self.add_roi_button.setObjectName("add_roi_button")
        self.horizontalLayout_3.addWidget(self.add_roi_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout.addWidget(self.apply_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1227, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cancel_button.clicked.connect(MainWindow.cancel_clicked)
        self.apply_button.clicked.connect(MainWindow.apply_clicked)
        self.remove_roi_button.clicked.connect(MainWindow.remove_roi_button_clicked)
        self.add_roi_button.clicked.connect(MainWindow.add_roi_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_roi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x0"))
        item = self.table_roi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y0"))
        item = self.table_roi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x1"))
        item = self.table_roi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "y1"))
        self.remove_roi_button.setText(_translate("MainWindow", "-"))
        self.add_roi_button.setText(_translate("MainWindow", "+"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.apply_button.setText(_translate("MainWindow", "OK"))

