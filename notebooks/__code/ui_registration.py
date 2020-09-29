# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/python_notebooks/notebooks/ui/ui_registration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 1149)
        MainWindow.setMinimumSize(QtCore.QSize(0, 300))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.auto_registration_button = QtWidgets.QPushButton(self.groupBox_2)
        self.auto_registration_button.setMinimumSize(QtCore.QSize(200, 0))
        self.auto_registration_button.setObjectName("auto_registration_button")
        self.horizontalLayout_5.addWidget(self.auto_registration_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.manual_registration_button = QtWidgets.QPushButton(self.groupBox_2)
        self.manual_registration_button.setMinimumSize(QtCore.QSize(200, 0))
        self.manual_registration_button.setObjectName("manual_registration_button")
        self.horizontalLayout_5.addWidget(self.manual_registration_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.marker_registration_button = QtWidgets.QPushButton(self.groupBox_2)
        self.marker_registration_button.setMinimumSize(QtCore.QSize(200, 0))
        self.marker_registration_button.setObjectName("marker_registration_button")
        self.horizontalLayout_5.addWidget(self.marker_registration_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.profiler_registration_button = QtWidgets.QPushButton(self.groupBox_2)
        self.profiler_registration_button.setMinimumSize(QtCore.QSize(200, 0))
        self.profiler_registration_button.setObjectName("profiler_registration_button")
        self.horizontalLayout_5.addWidget(self.profiler_registration_button)
        spacerItem4 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.grid_display_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.grid_display_checkBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.grid_display_checkBox.setObjectName("grid_display_checkBox")
        self.horizontalLayout_6.addWidget(self.grid_display_checkBox)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.grid_size_slider = QtWidgets.QSlider(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_size_slider.sizePolicy().hasHeightForWidth())
        self.grid_size_slider.setSizePolicy(sizePolicy)
        self.grid_size_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.grid_size_slider.setMinimum(1)
        self.grid_size_slider.setMaximum(200)
        self.grid_size_slider.setProperty("value", 100)
        self.grid_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.grid_size_slider.setObjectName("grid_size_slider")
        self.horizontalLayout_6.addWidget(self.grid_size_slider)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selection_groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.selection_groupBox.setEnabled(True)
        self.selection_groupBox.setMinimumSize(QtCore.QSize(70, 0))
        self.selection_groupBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.selection_groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selection_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.selection_groupBox.setObjectName("selection_groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.selection_groupBox)
        self.verticalLayout_5.setContentsMargins(-1, -1, 19, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.selection_all = QtWidgets.QCheckBox(self.selection_groupBox)
        self.selection_all.setChecked(True)
        self.selection_all.setObjectName("selection_all")
        self.verticalLayout_5.addWidget(self.selection_all)
        self.top_row_label = QtWidgets.QLabel(self.selection_groupBox)
        self.top_row_label.setEnabled(False)
        self.top_row_label.setMinimumSize(QtCore.QSize(50, 0))
        self.top_row_label.setObjectName("top_row_label")
        self.verticalLayout_5.addWidget(self.top_row_label)
        self.opacity_selection_slider = QtWidgets.QSlider(self.selection_groupBox)
        self.opacity_selection_slider.setEnabled(False)
        self.opacity_selection_slider.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.opacity_selection_slider.setAccessibleDescription("")
        self.opacity_selection_slider.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.opacity_selection_slider.setMaximum(100)
        self.opacity_selection_slider.setSingleStep(1)
        self.opacity_selection_slider.setPageStep(10)
        self.opacity_selection_slider.setProperty("value", 100)
        self.opacity_selection_slider.setOrientation(QtCore.Qt.Vertical)
        self.opacity_selection_slider.setInvertedAppearance(True)
        self.opacity_selection_slider.setInvertedControls(True)
        self.opacity_selection_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.opacity_selection_slider.setTickInterval(100)
        self.opacity_selection_slider.setObjectName("opacity_selection_slider")
        self.verticalLayout_5.addWidget(self.opacity_selection_slider)
        self.bottom_row_label = QtWidgets.QLabel(self.selection_groupBox)
        self.bottom_row_label.setEnabled(False)
        self.bottom_row_label.setMinimumSize(QtCore.QSize(50, 0))
        self.bottom_row_label.setObjectName("bottom_row_label")
        self.verticalLayout_5.addWidget(self.bottom_row_label)
        self.horizontalLayout_2.addWidget(self.selection_groupBox)
        self.pyqtgraph_widget = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyqtgraph_widget.sizePolicy().hasHeightForWidth())
        self.pyqtgraph_widget.setSizePolicy(sizePolicy)
        self.pyqtgraph_widget.setObjectName("pyqtgraph_widget")
        self.horizontalLayout_2.addWidget(self.pyqtgraph_widget)
        self.selection_reference_opacity_groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.selection_reference_opacity_groupBox.setMinimumSize(QtCore.QSize(70, 0))
        self.selection_reference_opacity_groupBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.selection_reference_opacity_groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selection_reference_opacity_groupBox.setTitle("")
        self.selection_reference_opacity_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.selection_reference_opacity_groupBox.setObjectName("selection_reference_opacity_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.selection_reference_opacity_groupBox)
        self.verticalLayout.setContentsMargins(-1, -1, 19, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.selection_reference_opacity_groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.opacity_slider = QtWidgets.QSlider(self.selection_reference_opacity_groupBox)
        self.opacity_slider.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.opacity_slider.setAccessibleDescription("")
        self.opacity_slider.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setProperty("value", 100)
        self.opacity_slider.setOrientation(QtCore.Qt.Vertical)
        self.opacity_slider.setInvertedAppearance(False)
        self.opacity_slider.setInvertedControls(False)
        self.opacity_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.opacity_slider.setObjectName("opacity_slider")
        self.verticalLayout.addWidget(self.opacity_slider)
        self.label_3 = QtWidgets.QLabel(self.selection_reference_opacity_groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.selection_reference_opacity_groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previous_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.previous_image_button.setEnabled(False)
        self.previous_image_button.setObjectName("previous_image_button")
        self.horizontalLayout_3.addWidget(self.previous_image_button)
        self.file_slider = QtWidgets.QSlider(self.layoutWidget)
        self.file_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.file_slider.setObjectName("file_slider")
        self.horizontalLayout_3.addWidget(self.file_slider)
        self.next_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_image_button.setObjectName("next_image_button")
        self.horizontalLayout_3.addWidget(self.next_image_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.reference_image_label = QtWidgets.QLabel(self.layoutWidget1)
        self.reference_image_label.setObjectName("reference_image_label")
        self.horizontalLayout_4.addWidget(self.reference_image_label)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.help_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.help_button.setMinimumSize(QtCore.QSize(100, 30))
        self.help_button.setMaximumSize(QtCore.QSize(100, 30))
        self.help_button.setObjectName("help_button")
        self.horizontalLayout.addWidget(self.help_button)
        spacerItem5 = QtWidgets.QSpacerItem(408, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.export_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.export_button.setMinimumSize(QtCore.QSize(100, 30))
        self.export_button.setMaximumSize(QtCore.QSize(100, 30))
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 22))
        self.menubar.setObjectName("menubar")
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
        self.actionDsc_files = QtWidgets.QAction(MainWindow)
        self.actionDsc_files.setObjectName("actionDsc_files")
        self.actionDsc = QtWidgets.QAction(MainWindow)
        self.actionDsc.setObjectName("actionDsc")
        self.actionWater_Intake_2 = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake_2.setObjectName("actionWater_Intake_2")
        self.actionProfiles = QtWidgets.QAction(MainWindow)
        self.actionProfiles.setObjectName("actionProfiles")

        self.retranslateUi(MainWindow)
        self.export_button.clicked.connect(MainWindow.export_button_clicked)
        self.help_button.clicked.connect(MainWindow.help_button_clicked)
        self.file_slider.sliderMoved['int'].connect(MainWindow.slider_file_changed)
        self.file_slider.valueChanged['int'].connect(MainWindow.slider_file_changed)
        self.tableWidget.itemSelectionChanged.connect(MainWindow.table_row_clicked)
        self.opacity_slider.valueChanged['int'].connect(MainWindow.opacity_changed)
        self.previous_image_button.clicked.connect(MainWindow.previous_image_button_clicked)
        self.next_image_button.clicked.connect(MainWindow.next_image_button_clicked)
        self.selection_all.clicked.connect(MainWindow.selection_all_clicked)
        self.opacity_selection_slider.sliderPressed.connect(MainWindow.selection_slider_changed)
        self.opacity_selection_slider.sliderMoved['int'].connect(MainWindow.selection_slider_moved)
        self.manual_registration_button.clicked.connect(MainWindow.manual_registration_button_clicked)
        self.tableWidget.cellChanged['int','int'].connect(MainWindow.table_cell_modified)
        self.auto_registration_button.clicked.connect(MainWindow.auto_registration_button_clicked)
        self.grid_display_checkBox.clicked.connect(MainWindow.grid_display_checkBox_clicked)
        self.grid_size_slider.sliderMoved['int'].connect(MainWindow.grid_size_slider_moved)
        self.grid_size_slider.sliderPressed.connect(MainWindow.grid_size_slider_pressed)
        self.marker_registration_button.clicked.connect(MainWindow.markers_registration_button_clicked)
        self.profiler_registration_button.clicked.connect(MainWindow.profiler_registration_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registration Tool"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Registration Methods"))
        self.auto_registration_button.setText(_translate("MainWindow", "Auto ..."))
        self.manual_registration_button.setText(_translate("MainWindow", "Manual ..."))
        self.marker_registration_button.setText(_translate("MainWindow", "Markers ..."))
        self.profiler_registration_button.setText(_translate("MainWindow", "Profiler ..."))
        self.groupBox.setTitle(_translate("MainWindow", "Grid"))
        self.grid_display_checkBox.setText(_translate("MainWindow", "Display"))
        self.label_5.setText(_translate("MainWindow", "Size"))
        self.selection_groupBox.setTitle(_translate("MainWindow", "Selection"))
        self.selection_all.setText(_translate("MainWindow", "All"))
        self.top_row_label.setText(_translate("MainWindow", "Row 0"))
        self.bottom_row_label.setText(_translate("MainWindow", "Row 1"))
        self.label_2.setText(_translate("MainWindow", "Selec."))
        self.label_3.setText(_translate("MainWindow", "Ref."))
        self.previous_image_button.setText(_translate("MainWindow", "Prev. Image"))
        self.next_image_button.setText(_translate("MainWindow", "Next Image"))
        self.label.setText(_translate("MainWindow", "Reference Image:"))
        self.reference_image_label.setText(_translate("MainWindow", "N/A"))
        self.pushButton_3.setText(_translate("MainWindow", "Change ..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Xoffset"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yoffset"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rotation"))
        self.help_button.setText(_translate("MainWindow", "HELP"))
        self.export_button.setText(_translate("MainWindow", "Export ..."))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))
        self.actionDsc_files.setText(_translate("MainWindow", "dsc files ..."))
        self.actionDsc.setText(_translate("MainWindow", "dsc ..."))
        self.actionWater_Intake_2.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionProfiles.setText(_translate("MainWindow", "Profiles ..."))

