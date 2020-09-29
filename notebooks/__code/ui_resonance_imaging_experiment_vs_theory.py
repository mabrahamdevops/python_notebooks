# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/python_notebooks/notebooks/ui/ui_resonance_imaging_experiment_vs_theory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1162, 863)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 500))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.file_index_ratio_button = QtWidgets.QRadioButton(self.groupBox)
        self.file_index_ratio_button.setChecked(True)
        self.file_index_ratio_button.setObjectName("file_index_ratio_button")
        self.horizontalLayout_8.addWidget(self.file_index_ratio_button)
        self.tof_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.tof_radio_button.setObjectName("tof_radio_button")
        self.horizontalLayout_8.addWidget(self.tof_radio_button)
        self.lambda_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.lambda_radio_button.setObjectName("lambda_radio_button")
        self.horizontalLayout_8.addWidget(self.lambda_radio_button)
        self.energy_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.energy_radio_button.setObjectName("energy_radio_button")
        self.horizontalLayout_8.addWidget(self.energy_radio_button)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.list_to_plot_widget = QtWidgets.QListWidget(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_to_plot_widget.sizePolicy().hasHeightForWidth())
        self.list_to_plot_widget.setSizePolicy(sizePolicy)
        self.list_to_plot_widget.setMinimumSize(QtCore.QSize(200, 100))
        self.list_to_plot_widget.setMaximumSize(QtCore.QSize(300, 300))
        self.list_to_plot_widget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_to_plot_widget.setObjectName("list_to_plot_widget")
        self.verticalLayout.addWidget(self.list_to_plot_widget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.distance_source_detector_value = QtWidgets.QLineEdit(self.widget1)
        self.distance_source_detector_value.setMinimumSize(QtCore.QSize(80, 0))
        self.distance_source_detector_value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.distance_source_detector_value.setObjectName("distance_source_detector_value")
        self.horizontalLayout.addWidget(self.distance_source_detector_value)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.detector_offset_value = QtWidgets.QLineEdit(self.widget1)
        self.detector_offset_value.setMinimumSize(QtCore.QSize(80, 0))
        self.detector_offset_value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.detector_offset_value.setObjectName("detector_offset_value")
        self.horizontalLayout_2.addWidget(self.detector_offset_value)
        self.detector_offset_units = QtWidgets.QLabel(self.widget1)
        self.detector_offset_units.setObjectName("detector_offset_units")
        self.horizontalLayout_2.addWidget(self.detector_offset_units)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.time_spectra_file = QtWidgets.QLabel(self.widget1)
        self.time_spectra_file.setObjectName("time_spectra_file")
        self.horizontalLayout_3.addWidget(self.time_spectra_file)
        self.time_spectra_file_browse_button = QtWidgets.QPushButton(self.widget1)
        self.time_spectra_file_browse_button.setMinimumSize(QtCore.QSize(100, 0))
        self.time_spectra_file_browse_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.time_spectra_file_browse_button.setObjectName("time_spectra_file_browse_button")
        self.horizontalLayout_3.addWidget(self.time_spectra_file_browse_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.done_button = QtWidgets.QPushButton(self.widget1)
        self.done_button.setObjectName("done_button")
        self.verticalLayout_2.addWidget(self.done_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.done_button.clicked.connect(MainWindow.done_button_clicked)
        self.distance_source_detector_value.editingFinished.connect(MainWindow.distance_source_detector_validated)
        self.detector_offset_value.returnPressed.connect(MainWindow.detector_offset_validated)
        self.time_spectra_file_browse_button.clicked.connect(MainWindow.time_spectra_file_browse_button_clicked)
        self.file_index_ratio_button.clicked.connect(MainWindow.radio_button_clicked)
        self.tof_radio_button.clicked.connect(MainWindow.radio_button_clicked)
        self.lambda_radio_button.clicked.connect(MainWindow.radio_button_clicked)
        self.list_to_plot_widget.itemClicked['QListWidgetItem*'].connect(MainWindow.plot_selection_changed)
        self.energy_radio_button.clicked.connect(MainWindow.radio_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Xaxis"))
        self.file_index_ratio_button.setText(_translate("MainWindow", "File Index"))
        self.tof_radio_button.setText(_translate("MainWindow", "TOF (us)"))
        self.lambda_radio_button.setText(_translate("MainWindow", "lambda (A)"))
        self.energy_radio_button.setText(_translate("MainWindow", "Energy (eV)"))
        self.label_4.setText(_translate("MainWindow", "Plot Selection"))
        self.label.setText(_translate("MainWindow", "Distance Source-Detector"))
        self.label_2.setText(_translate("MainWindow", "m"))
        self.label_3.setText(_translate("MainWindow", "Detector Offset"))
        self.detector_offset_units.setText(_translate("MainWindow", "us"))
        self.label_5.setText(_translate("MainWindow", "Time Spectra File:"))
        self.time_spectra_file.setText(_translate("MainWindow", "N/A"))
        self.time_spectra_file_browse_button.setText(_translate("MainWindow", "Browse ..."))
        self.done_button.setText(_translate("MainWindow", "DONE"))

