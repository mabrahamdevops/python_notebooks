# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/python_notebooks/ui/ui_water_intake_profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 1265)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 600))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.file_index_slider = QtWidgets.QSlider(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_index_slider.sizePolicy().hasHeightForWidth())
        self.file_index_slider.setSizePolicy(sizePolicy)
        self.file_index_slider.setMinimumSize(QtCore.QSize(400, 40))
        self.file_index_slider.setMaximumSize(QtCore.QSize(40, 40))
        self.file_index_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_index_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.file_index_slider.setTickInterval(1)
        self.file_index_slider.setObjectName("file_index_slider")
        self.horizontalLayout_2.addWidget(self.file_index_slider)
        self.file_index_value = QtWidgets.QLabel(self.widget1)
        self.file_index_value.setObjectName("file_index_value")
        self.horizontalLayout_2.addWidget(self.file_index_value)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_8.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.add_radioButton.setChecked(True)
        self.add_radioButton.setObjectName("add_radioButton")
        self.verticalLayout_2.addWidget(self.add_radioButton)
        self.mean_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.mean_radioButton.setObjectName("mean_radioButton")
        self.verticalLayout_2.addWidget(self.mean_radioButton)
        self.median_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.median_radioButton.setObjectName("median_radioButton")
        self.verticalLayout_2.addWidget(self.median_radioButton)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sort_files_by_time_radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.sort_files_by_time_radioButton.setChecked(True)
        self.sort_files_by_time_radioButton.setObjectName("sort_files_by_time_radioButton")
        self.horizontalLayout_7.addWidget(self.sort_files_by_time_radioButton)
        self.sort_files_by_name_radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.sort_files_by_name_radioButton.setObjectName("sort_files_by_name_radioButton")
        self.horizontalLayout_7.addWidget(self.sort_files_by_name_radioButton)
        self.time_between_runs_label = QtWidgets.QLabel(self.groupBox_3)
        self.time_between_runs_label.setEnabled(False)
        self.time_between_runs_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.time_between_runs_label.setObjectName("time_between_runs_label")
        self.horizontalLayout_7.addWidget(self.time_between_runs_label)
        self.time_between_runs_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.time_between_runs_spinBox.setEnabled(False)
        self.time_between_runs_spinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.time_between_runs_spinBox.setDecimals(2)
        self.time_between_runs_spinBox.setMinimum(0.1)
        self.time_between_runs_spinBox.setMaximum(500.0)
        self.time_between_runs_spinBox.setSingleStep(0.1)
        self.time_between_runs_spinBox.setProperty("value", 30.0)
        self.time_between_runs_spinBox.setObjectName("time_between_runs_spinBox")
        self.horizontalLayout_7.addWidget(self.time_between_runs_spinBox)
        self.time_between_runs_units_label = QtWidgets.QLabel(self.groupBox_3)
        self.time_between_runs_units_label.setEnabled(False)
        self.time_between_runs_units_label.setMinimumSize(QtCore.QSize(20, 0))
        self.time_between_runs_units_label.setMaximumSize(QtCore.QSize(20, 16777215))
        self.time_between_runs_units_label.setObjectName("time_between_runs_units_label")
        self.horizontalLayout_7.addWidget(self.time_between_runs_units_label)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 30))
        self.cancel_button.setMaximumSize(QtCore.QSize(100, 30))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(408, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setMinimumSize(QtCore.QSize(100, 30))
        self.help_button.setMaximumSize(QtCore.QSize(100, 30))
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setMinimumSize(QtCore.QSize(100, 30))
        self.ok_button.setMaximumSize(QtCore.QSize(100, 30))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Profile = QtWidgets.QAction(MainWindow)
        self.actionExport_Profile.setObjectName("actionExport_Profile")
        self.actionWater_Intake = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake.setObjectName("actionWater_Intake")
        self.actionImportedFilesMetadata = QtWidgets.QAction(MainWindow)
        self.actionImportedFilesMetadata.setObjectName("actionImportedFilesMetadata")
        self.actionBy_Time_Stamp = QtWidgets.QAction(MainWindow)
        self.actionBy_Time_Stamp.setObjectName("actionBy_Time_Stamp")
        self.actionBy_File_Name = QtWidgets.QAction(MainWindow)
        self.actionBy_File_Name.setObjectName("actionBy_File_Name")
        self.menuFile.addAction(self.actionExport_Profile)
        self.menuFile.addAction(self.actionWater_Intake)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.file_index_slider.valueChanged['int'].connect(MainWindow.slider_changed)
        self.ok_button.clicked.connect(MainWindow.ok_button_clicked)
        self.cancel_button.clicked.connect(MainWindow.cancel_button_clicked)
        self.help_button.clicked.connect(MainWindow.help_button_clicked)
        self.actionExport_Profile.triggered.connect(MainWindow.export_profile_clicked)
        self.actionWater_Intake.triggered.connect(MainWindow.export_water_intake_clicked)
        self.add_radioButton.clicked.connect(MainWindow.profile_algo_changed)
        self.mean_radioButton.clicked.connect(MainWindow.profile_algo_changed)
        self.median_radioButton.clicked.connect(MainWindow.profile_algo_changed)
        self.sort_files_by_time_radioButton.clicked.connect(MainWindow.sorting_files_checkbox_clicked)
        self.sort_files_by_name_radioButton.clicked.connect(MainWindow.sorting_files_checkbox_clicked)
        self.time_between_runs_spinBox.valueChanged['double'].connect(MainWindow.time_between_runs_spinBox_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Index"))
        self.file_index_value.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "NB: First image is ignored"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time Stamp (unix format)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time Stamp (user format)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Profile Algorithms"))
        self.add_radioButton.setText(_translate("MainWindow", "Add"))
        self.mean_radioButton.setText(_translate("MainWindow", "Mean"))
        self.median_radioButton.setText(_translate("MainWindow", "Median"))
        self.pushButton.setText(_translate("MainWindow", "Export Table ..."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sorting Files"))
        self.sort_files_by_time_radioButton.setText(_translate("MainWindow", "by Time Stamp"))
        self.sort_files_by_name_radioButton.setText(_translate("MainWindow", "by Name"))
        self.time_between_runs_label.setText(_translate("MainWindow", "-> Time Between Runs"))
        self.time_between_runs_units_label.setText(_translate("MainWindow", "s"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.help_button.setText(_translate("MainWindow", "HELP"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "Export"))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))

