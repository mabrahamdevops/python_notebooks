# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/python_notebooks/notebooks/ui/ui_metadata_overlapping_images.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1419, 849)
        MainWindow.setMinimumSize(QtCore.QSize(0, 300))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pyqtgraph_widget = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyqtgraph_widget.sizePolicy().hasHeightForWidth())
        self.pyqtgraph_widget.setSizePolicy(sizePolicy)
        self.pyqtgraph_widget.setObjectName("pyqtgraph_widget")
        self.horizontalLayout_7.addWidget(self.pyqtgraph_widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.previous_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.previous_image_button.setEnabled(False)
        self.previous_image_button.setObjectName("previous_image_button")
        self.horizontalLayout_8.addWidget(self.previous_image_button)
        self.file_slider = QtWidgets.QSlider(self.layoutWidget)
        self.file_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.file_slider.setObjectName("file_slider")
        self.horizontalLayout_8.addWidget(self.file_slider)
        self.image_slider_value = QtWidgets.QLabel(self.layoutWidget)
        self.image_slider_value.setMinimumSize(QtCore.QSize(30, 0))
        self.image_slider_value.setMaximumSize(QtCore.QSize(30, 16777215))
        self.image_slider_value.setBaseSize(QtCore.QSize(50, 0))
        self.image_slider_value.setObjectName("image_slider_value")
        self.horizontalLayout_8.addWidget(self.image_slider_value)
        self.next_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_image_button.setObjectName("next_image_button")
        self.horizontalLayout_8.addWidget(self.next_image_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scale_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.scale_checkbox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scale_checkbox.setObjectName("scale_checkbox")
        self.verticalLayout_4.addWidget(self.scale_checkbox)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.scale_groupbox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.scale_groupbox.setEnabled(False)
        self.scale_groupbox.setMinimumSize(QtCore.QSize(500, 0))
        self.scale_groupbox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.scale_groupbox.setTitle("")
        self.scale_groupbox.setObjectName("scale_groupbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scale_groupbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scale_groupbox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.scale_horizontal_orientation = QtWidgets.QRadioButton(self.scale_groupbox)
        self.scale_horizontal_orientation.setChecked(True)
        self.scale_horizontal_orientation.setObjectName("scale_horizontal_orientation")
        self.horizontalLayout_2.addWidget(self.scale_horizontal_orientation)
        self.scale_vertical_orientation = QtWidgets.QRadioButton(self.scale_groupbox)
        self.scale_vertical_orientation.setObjectName("scale_vertical_orientation")
        self.horizontalLayout_2.addWidget(self.scale_vertical_orientation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.scale_groupbox)
        self.label_3.setMinimumSize(QtCore.QSize(40, 0))
        self.label_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.scale_size_spinbox = QtWidgets.QSpinBox(self.scale_groupbox)
        self.scale_size_spinbox.setMinimum(1)
        self.scale_size_spinbox.setMaximum(10000)
        self.scale_size_spinbox.setProperty("value", 100)
        self.scale_size_spinbox.setObjectName("scale_size_spinbox")
        self.horizontalLayout_3.addWidget(self.scale_size_spinbox)
        self.label_4 = QtWidgets.QLabel(self.scale_groupbox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.scale_real_size = QtWidgets.QLineEdit(self.scale_groupbox)
        self.scale_real_size.setMinimumSize(QtCore.QSize(100, 0))
        self.scale_real_size.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scale_real_size.setObjectName("scale_real_size")
        self.horizontalLayout_3.addWidget(self.scale_real_size)
        self.scale_units_combobox = QtWidgets.QComboBox(self.scale_groupbox)
        self.scale_units_combobox.setObjectName("scale_units_combobox")
        self.horizontalLayout_3.addWidget(self.scale_units_combobox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.scale_groupbox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.scale_color_combobox = QtWidgets.QComboBox(self.scale_groupbox)
        self.scale_color_combobox.setObjectName("scale_color_combobox")
        self.scale_color_combobox.addItem("")
        self.scale_color_combobox.addItem("")
        self.scale_color_combobox.addItem("")
        self.scale_color_combobox.addItem("")
        self.scale_color_combobox.addItem("")
        self.horizontalLayout_5.addWidget(self.scale_color_combobox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.scale_groupbox)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.scale_thickness = QtWidgets.QSpinBox(self.scale_groupbox)
        self.scale_thickness.setMinimum(1)
        self.scale_thickness.setMaximum(50)
        self.scale_thickness.setProperty("value", 4)
        self.scale_thickness.setObjectName("scale_thickness")
        self.horizontalLayout_5.addWidget(self.scale_thickness)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11.addWidget(self.scale_groupbox)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.scale_position_label = QtWidgets.QLabel(self.layoutWidget1)
        self.scale_position_label.setEnabled(False)
        self.scale_position_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scale_position_label.setObjectName("scale_position_label")
        self.verticalLayout_5.addWidget(self.scale_position_label)
        self.scale_position_frame = QtWidgets.QFrame(self.layoutWidget1)
        self.scale_position_frame.setEnabled(False)
        self.scale_position_frame.setMinimumSize(QtCore.QSize(130, 120))
        self.scale_position_frame.setMaximumSize(QtCore.QSize(130, 120))
        self.scale_position_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scale_position_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scale_position_frame.setObjectName("scale_position_frame")
        self.scale_position_y = QtWidgets.QSlider(self.scale_position_frame)
        self.scale_position_y.setGeometry(QtCore.QRect(60, 30, 20, 80))
        self.scale_position_y.setMinimumSize(QtCore.QSize(0, 80))
        self.scale_position_y.setMaximumSize(QtCore.QSize(16777215, 80))
        self.scale_position_y.setOrientation(QtCore.Qt.Vertical)
        self.scale_position_y.setObjectName("scale_position_y")
        self.scale_position_x = QtWidgets.QSlider(self.scale_position_frame)
        self.scale_position_x.setGeometry(QtCore.QRect(20, 50, 100, 22))
        self.scale_position_x.setMinimumSize(QtCore.QSize(100, 0))
        self.scale_position_x.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scale_position_x.setOrientation(QtCore.Qt.Horizontal)
        self.scale_position_x.setObjectName("scale_position_x")
        self.label_8 = QtWidgets.QLabel(self.scale_position_frame)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 16, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.scale_position_frame)
        self.label_9.setGeometry(QtCore.QRect(64, 10, 10, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.scale_position_frame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.metadata_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.metadata_checkbox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.metadata_checkbox.setObjectName("metadata_checkbox")
        self.verticalLayout_6.addWidget(self.metadata_checkbox)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.metadata_groupbox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.metadata_groupbox.setEnabled(False)
        self.metadata_groupbox.setMinimumSize(QtCore.QSize(500, 0))
        self.metadata_groupbox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.metadata_groupbox.setTitle("")
        self.metadata_groupbox.setObjectName("metadata_groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.metadata_groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_metadata_checkbox = QtWidgets.QCheckBox(self.metadata_groupbox)
        self.select_metadata_checkbox.setMinimumSize(QtCore.QSize(130, 0))
        self.select_metadata_checkbox.setMaximumSize(QtCore.QSize(130, 16777215))
        self.select_metadata_checkbox.setObjectName("select_metadata_checkbox")
        self.horizontalLayout_4.addWidget(self.select_metadata_checkbox)
        self.select_metadata_combobox = QtWidgets.QComboBox(self.metadata_groupbox)
        self.select_metadata_combobox.setEnabled(False)
        self.select_metadata_combobox.setMinimumSize(QtCore.QSize(300, 0))
        self.select_metadata_combobox.setObjectName("select_metadata_combobox")
        self.horizontalLayout_4.addWidget(self.select_metadata_combobox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.meta_label = QtWidgets.QLabel(self.metadata_groupbox)
        self.meta_label.setEnabled(False)
        self.meta_label.setObjectName("meta_label")
        self.horizontalLayout_9.addWidget(self.meta_label)
        self.label_7 = QtWidgets.QLabel(self.metadata_groupbox)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.manual_metadata_name = QtWidgets.QLineEdit(self.metadata_groupbox)
        self.manual_metadata_name.setEnabled(False)
        self.manual_metadata_name.setObjectName("manual_metadata_name")
        self.horizontalLayout_9.addWidget(self.manual_metadata_name)
        self.label_12 = QtWidgets.QLabel(self.metadata_groupbox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.manual_metadata_units = QtWidgets.QLineEdit(self.metadata_groupbox)
        self.manual_metadata_units.setObjectName("manual_metadata_units")
        self.horizontalLayout_9.addWidget(self.manual_metadata_units)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.tableWidget = QtWidgets.QTableWidget(self.metadata_groupbox)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.metadata_groupbox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.metadata_color_combobox = QtWidgets.QComboBox(self.metadata_groupbox)
        self.metadata_color_combobox.setObjectName("metadata_color_combobox")
        self.metadata_color_combobox.addItem("")
        self.metadata_color_combobox.addItem("")
        self.metadata_color_combobox.addItem("")
        self.metadata_color_combobox.addItem("")
        self.metadata_color_combobox.addItem("")
        self.horizontalLayout_6.addWidget(self.metadata_color_combobox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.import_table_button = QtWidgets.QPushButton(self.metadata_groupbox)
        self.import_table_button.setObjectName("import_table_button")
        self.horizontalLayout_14.addWidget(self.import_table_button)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13.addWidget(self.metadata_groupbox)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.metadata_position_label = QtWidgets.QLabel(self.layoutWidget1)
        self.metadata_position_label.setEnabled(False)
        self.metadata_position_label.setMinimumSize(QtCore.QSize(0, 30))
        self.metadata_position_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.metadata_position_label.setAlignment(QtCore.Qt.AlignCenter)
        self.metadata_position_label.setObjectName("metadata_position_label")
        self.verticalLayout_8.addWidget(self.metadata_position_label)
        self.metadata_position_frame = QtWidgets.QFrame(self.layoutWidget1)
        self.metadata_position_frame.setEnabled(False)
        self.metadata_position_frame.setMinimumSize(QtCore.QSize(130, 120))
        self.metadata_position_frame.setMaximumSize(QtCore.QSize(130, 120))
        self.metadata_position_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.metadata_position_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.metadata_position_frame.setObjectName("metadata_position_frame")
        self.metadata_position_y = QtWidgets.QSlider(self.metadata_position_frame)
        self.metadata_position_y.setGeometry(QtCore.QRect(60, 30, 20, 80))
        self.metadata_position_y.setMinimumSize(QtCore.QSize(0, 80))
        self.metadata_position_y.setMaximumSize(QtCore.QSize(16777215, 80))
        self.metadata_position_y.setProperty("value", 99)
        self.metadata_position_y.setOrientation(QtCore.Qt.Vertical)
        self.metadata_position_y.setObjectName("metadata_position_y")
        self.metadata_position_x = QtWidgets.QSlider(self.metadata_position_frame)
        self.metadata_position_x.setGeometry(QtCore.QRect(20, 50, 100, 22))
        self.metadata_position_x.setMinimumSize(QtCore.QSize(100, 0))
        self.metadata_position_x.setMaximumSize(QtCore.QSize(100, 16777215))
        self.metadata_position_x.setProperty("value", 0)
        self.metadata_position_x.setOrientation(QtCore.Qt.Horizontal)
        self.metadata_position_x.setObjectName("metadata_position_x")
        self.label_10 = QtWidgets.QLabel(self.metadata_position_frame)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 16, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.metadata_position_frame)
        self.label_11.setGeometry(QtCore.QRect(64, 10, 10, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.metadata_position_frame)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.enable_graph_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.enable_graph_checkbox.setEnabled(False)
        self.enable_graph_checkbox.setObjectName("enable_graph_checkbox")
        self.verticalLayout_8.addWidget(self.enable_graph_checkbox)
        self.graph_groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.graph_groupBox.setEnabled(True)
        self.graph_groupBox.setTitle("")
        self.graph_groupBox.setObjectName("graph_groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.graph_groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.metadata_position_label_4 = QtWidgets.QLabel(self.graph_groupBox)
        self.metadata_position_label_4.setEnabled(True)
        self.metadata_position_label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.metadata_position_label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.metadata_position_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.metadata_position_label_4.setObjectName("metadata_position_label_4")
        self.verticalLayout_9.addWidget(self.metadata_position_label_4)
        self.metadata_position_frame_3 = QtWidgets.QFrame(self.graph_groupBox)
        self.metadata_position_frame_3.setEnabled(True)
        self.metadata_position_frame_3.setMinimumSize(QtCore.QSize(130, 120))
        self.metadata_position_frame_3.setMaximumSize(QtCore.QSize(130, 120))
        self.metadata_position_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.metadata_position_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.metadata_position_frame_3.setObjectName("metadata_position_frame_3")
        self.graph_position_y = QtWidgets.QSlider(self.metadata_position_frame_3)
        self.graph_position_y.setGeometry(QtCore.QRect(60, 30, 20, 80))
        self.graph_position_y.setMinimumSize(QtCore.QSize(0, 80))
        self.graph_position_y.setMaximumSize(QtCore.QSize(16777215, 80))
        self.graph_position_y.setProperty("value", 99)
        self.graph_position_y.setOrientation(QtCore.Qt.Vertical)
        self.graph_position_y.setObjectName("graph_position_y")
        self.graph_position_x = QtWidgets.QSlider(self.metadata_position_frame_3)
        self.graph_position_x.setGeometry(QtCore.QRect(20, 50, 100, 22))
        self.graph_position_x.setMinimumSize(QtCore.QSize(100, 0))
        self.graph_position_x.setMaximumSize(QtCore.QSize(100, 16777215))
        self.graph_position_x.setProperty("value", 0)
        self.graph_position_x.setOrientation(QtCore.Qt.Horizontal)
        self.graph_position_x.setObjectName("graph_position_x")
        self.label_15 = QtWidgets.QLabel(self.metadata_position_frame_3)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 16, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.metadata_position_frame_3)
        self.label_16.setGeometry(QtCore.QRect(64, 10, 10, 21))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.metadata_position_frame_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.graph_groupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.graph_color_combobox = QtWidgets.QComboBox(self.graph_groupBox)
        self.graph_color_combobox.setObjectName("graph_color_combobox")
        self.graph_color_combobox.addItem("")
        self.graph_color_combobox.addItem("")
        self.graph_color_combobox.addItem("")
        self.graph_color_combobox.addItem("")
        self.graph_color_combobox.addItem("")
        self.horizontalLayout_10.addWidget(self.graph_color_combobox)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.metadata_graph_size_label_2 = QtWidgets.QLabel(self.graph_groupBox)
        self.metadata_graph_size_label_2.setObjectName("metadata_graph_size_label_2")
        self.horizontalLayout_12.addWidget(self.metadata_graph_size_label_2)
        self.metadata_graph_size_slider = QtWidgets.QSlider(self.graph_groupBox)
        self.metadata_graph_size_slider.setMinimum(50)
        self.metadata_graph_size_slider.setMaximum(1000)
        self.metadata_graph_size_slider.setSingleStep(1)
        self.metadata_graph_size_slider.setProperty("value", 200)
        self.metadata_graph_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.metadata_graph_size_slider.setObjectName("metadata_graph_size_slider")
        self.horizontalLayout_12.addWidget(self.metadata_graph_size_slider)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.verticalLayout_8.addWidget(self.graph_groupBox)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.horizontalLayout_13.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.verticalLayout_7.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1419, 22))
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
        self.pushButton.clicked.connect(MainWindow.help_button_clicked)
        self.scale_checkbox.clicked['bool'].connect(MainWindow.scale_checkbox_clicked)
        self.metadata_checkbox.clicked['bool'].connect(MainWindow.metadata_checkbox_clicked)
        self.previous_image_button.clicked.connect(MainWindow.previous_image_button_clicked)
        self.next_image_button.clicked.connect(MainWindow.next_image_button_clicked)
        self.file_slider.sliderPressed.connect(MainWindow.slider_file_clicked)
        self.file_slider.valueChanged['int'].connect(MainWindow.slider_file_changed)
        self.select_metadata_checkbox.clicked['bool'].connect(MainWindow.select_metadata_checkbox_clicked)
        self.select_metadata_combobox.currentIndexChanged['int'].connect(MainWindow.metadata_list_changed)
        self.scale_horizontal_orientation.clicked.connect(MainWindow.scale_orientation_clicked)
        self.scale_vertical_orientation.clicked.connect(MainWindow.scale_orientation_clicked)
        self.scale_thickness.valueChanged['int'].connect(MainWindow.scale_thickness_value_changed)
        self.scale_color_combobox.currentIndexChanged['int'].connect(MainWindow.scale_color_changed)
        self.scale_size_spinbox.valueChanged['int'].connect(MainWindow.scale_size_changed)
        self.scale_real_size.returnPressed.connect(MainWindow.scale_real_size_changed)
        self.scale_units_combobox.currentIndexChanged['int'].connect(MainWindow.scale_units_changed)
        self.scale_position_x.sliderMoved['int'].connect(MainWindow.scale_position_moved)
        self.scale_position_x.sliderPressed.connect(MainWindow.scale_position_clicked)
        self.metadata_position_x.sliderMoved['int'].connect(MainWindow.metadata_position_moved)
        self.metadata_position_x.sliderPressed.connect(MainWindow.metadata_position_clicked)
        self.metadata_position_y.sliderMoved['int'].connect(MainWindow.metadata_position_moved)
        self.metadata_position_y.sliderPressed.connect(MainWindow.metadata_position_clicked)
        self.scale_position_y.sliderMoved['int'].connect(MainWindow.scale_position_moved)
        self.scale_position_y.sliderPressed.connect(MainWindow.scale_position_clicked)
        self.metadata_color_combobox.currentIndexChanged['int'].connect(MainWindow.metadata_color_changed)
        self.manual_metadata_name.returnPressed.connect(MainWindow.metadata_name_return_pressed)
        self.manual_metadata_units.returnPressed.connect(MainWindow.metadata_name_return_pressed)
        self.metadata_graph_size_slider.sliderPressed.connect(MainWindow.metadata_graph_size_pressed)
        self.metadata_graph_size_slider.sliderMoved['int'].connect(MainWindow.metadata_graph_size_moved)
        self.import_table_button.clicked.connect(MainWindow.import_table_pressed)
        self.tableWidget.customContextMenuRequested['QPoint'].connect(MainWindow.metadata_table_right_click)
        self.graph_position_y.sliderPressed.connect(MainWindow.graph_position_clicked)
        self.graph_position_x.sliderPressed.connect(MainWindow.graph_position_clicked)
        self.graph_position_x.sliderMoved['int'].connect(MainWindow.graph_position_moved)
        self.graph_position_y.sliderMoved['int'].connect(MainWindow.graph_position_moved)
        self.enable_graph_checkbox.stateChanged['int'].connect(MainWindow.enable_graph_button_clicked)
        self.graph_color_combobox.currentIndexChanged['int'].connect(MainWindow.graph_color_changed)
        self.graph_position_x.sliderReleased.connect(MainWindow.graph_position_clicked)
        self.graph_position_y.sliderReleased.connect(MainWindow.graph_position_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profile"))
        self.previous_image_button.setText(_translate("MainWindow", "Prev. Image"))
        self.image_slider_value.setText(_translate("MainWindow", "0"))
        self.next_image_button.setText(_translate("MainWindow", "Next Image"))
        self.scale_checkbox.setText(_translate("MainWindow", "Scale"))
        self.label_2.setText(_translate("MainWindow", "Orientation:"))
        self.scale_horizontal_orientation.setText(_translate("MainWindow", "horizontal"))
        self.scale_vertical_orientation.setText(_translate("MainWindow", "vertical"))
        self.label_3.setText(_translate("MainWindow", "Size:"))
        self.label_4.setText(_translate("MainWindow", "pixels     =="))
        self.scale_real_size.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "Color:"))
        self.scale_color_combobox.setItemText(0, _translate("MainWindow", "White"))
        self.scale_color_combobox.setItemText(1, _translate("MainWindow", "Red"))
        self.scale_color_combobox.setItemText(2, _translate("MainWindow", "Blue"))
        self.scale_color_combobox.setItemText(3, _translate("MainWindow", "Green"))
        self.scale_color_combobox.setItemText(4, _translate("MainWindow", "Black"))
        self.label.setText(_translate("MainWindow", "Thickness"))
        self.scale_position_label.setText(_translate("MainWindow", "Position"))
        self.label_8.setText(_translate("MainWindow", "x"))
        self.label_9.setText(_translate("MainWindow", "y"))
        self.metadata_checkbox.setText(_translate("MainWindow", "Metadata"))
        self.select_metadata_checkbox.setText(_translate("MainWindow", "Select metadata"))
        self.meta_label.setText(_translate("MainWindow", "Legend:"))
        self.label_12.setText(_translate("MainWindow", "... [Value] ..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.label_6.setText(_translate("MainWindow", "Color:"))
        self.metadata_color_combobox.setItemText(0, _translate("MainWindow", "White"))
        self.metadata_color_combobox.setItemText(1, _translate("MainWindow", "Red"))
        self.metadata_color_combobox.setItemText(2, _translate("MainWindow", "Blue"))
        self.metadata_color_combobox.setItemText(3, _translate("MainWindow", "Green"))
        self.metadata_color_combobox.setItemText(4, _translate("MainWindow", "Black"))
        self.import_table_button.setText(_translate("MainWindow", "Import Table ..."))
        self.metadata_position_label.setText(_translate("MainWindow", "Position"))
        self.label_10.setText(_translate("MainWindow", "x"))
        self.label_11.setText(_translate("MainWindow", "y"))
        self.enable_graph_checkbox.setText(_translate("MainWindow", "Enable Graph"))
        self.metadata_position_label_4.setText(_translate("MainWindow", "Graph Position"))
        self.label_15.setText(_translate("MainWindow", "x"))
        self.label_16.setText(_translate("MainWindow", "y"))
        self.label_13.setText(_translate("MainWindow", "Color:"))
        self.graph_color_combobox.setItemText(0, _translate("MainWindow", "White"))
        self.graph_color_combobox.setItemText(1, _translate("MainWindow", "Red"))
        self.graph_color_combobox.setItemText(2, _translate("MainWindow", "Blue"))
        self.graph_color_combobox.setItemText(3, _translate("MainWindow", "Green"))
        self.graph_color_combobox.setItemText(4, _translate("MainWindow", "Black"))
        self.metadata_graph_size_label_2.setText(_translate("MainWindow", "Size:"))
        self.pushButton.setText(_translate("MainWindow", "Help"))
        self.export_button.setText(_translate("MainWindow", "Export Images ..."))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))
        self.actionDsc_files.setText(_translate("MainWindow", "dsc files ..."))
        self.actionDsc.setText(_translate("MainWindow", "dsc ..."))
        self.actionWater_Intake_2.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionProfiles.setText(_translate("MainWindow", "Profiles ..."))

