# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/python_notebooks/ui/ui_radial_profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 793)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.circle_y = QtWidgets.QLabel(self.groupBox_2)
        self.circle_y.setMinimumSize(QtCore.QSize(50, 0))
        self.circle_y.setMaximumSize(QtCore.QSize(50, 16777215))
        self.circle_y.setText("")
        self.circle_y.setObjectName("circle_y")
        self.gridLayout.addWidget(self.circle_y, 1, 1, 1, 1)
        self.circle_x = QtWidgets.QLabel(self.groupBox_2)
        self.circle_x.setMinimumSize(QtCore.QSize(50, 0))
        self.circle_x.setMaximumSize(QtCore.QSize(50, 16777215))
        self.circle_x.setText("")
        self.circle_x.setObjectName("circle_x")
        self.gridLayout.addWidget(self.circle_x, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sector_full_circle = QtWidgets.QRadioButton(self.groupBox_3)
        self.sector_full_circle.setChecked(True)
        self.sector_full_circle.setObjectName("sector_full_circle")
        self.verticalLayout_2.addWidget(self.sector_full_circle)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.sector_sector = QtWidgets.QRadioButton(self.groupBox_3)
        self.sector_sector.setObjectName("sector_sector")
        self.verticalLayout_2.addWidget(self.sector_sector)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sector_from_value = QtWidgets.QLabel(self.groupBox_3)
        self.sector_from_value.setMinimumSize(QtCore.QSize(30, 0))
        self.sector_from_value.setMaximumSize(QtCore.QSize(30, 16777215))
        self.sector_from_value.setText("")
        self.sector_from_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sector_from_value.setObjectName("sector_from_value")
        self.gridLayout_2.addWidget(self.sector_from_value, 0, 2, 1, 1)
        self.sector_to_label = QtWidgets.QLabel(self.groupBox_3)
        self.sector_to_label.setObjectName("sector_to_label")
        self.gridLayout_2.addWidget(self.sector_to_label, 1, 0, 1, 1)
        self.sector_from_label = QtWidgets.QLabel(self.groupBox_3)
        self.sector_from_label.setObjectName("sector_from_label")
        self.gridLayout_2.addWidget(self.sector_from_label, 0, 0, 1, 1)
        self.from_angle_slider = QtWidgets.QScrollBar(self.groupBox_3)
        self.from_angle_slider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_angle_slider.sizePolicy().hasHeightForWidth())
        self.from_angle_slider.setSizePolicy(sizePolicy)
        self.from_angle_slider.setMaximum(360)
        self.from_angle_slider.setOrientation(QtCore.Qt.Horizontal)
        self.from_angle_slider.setObjectName("from_angle_slider")
        self.gridLayout_2.addWidget(self.from_angle_slider, 0, 1, 1, 1)
        self.sector_to_value = QtWidgets.QLabel(self.groupBox_3)
        self.sector_to_value.setText("")
        self.sector_to_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sector_to_value.setObjectName("sector_to_value")
        self.gridLayout_2.addWidget(self.sector_to_value, 1, 2, 1, 1)
        self.to_angle_slider = QtWidgets.QScrollBar(self.groupBox_3)
        self.to_angle_slider.setEnabled(False)
        self.to_angle_slider.setMaximum(360)
        self.to_angle_slider.setOrientation(QtCore.Qt.Horizontal)
        self.to_angle_slider.setObjectName("to_angle_slider")
        self.gridLayout_2.addWidget(self.to_angle_slider, 1, 1, 1, 1)
        self.sector_from_units = QtWidgets.QLabel(self.groupBox_3)
        self.sector_from_units.setMinimumSize(QtCore.QSize(10, 0))
        self.sector_from_units.setMaximumSize(QtCore.QSize(10, 16777215))
        self.sector_from_units.setText("")
        self.sector_from_units.setObjectName("sector_from_units")
        self.gridLayout_2.addWidget(self.sector_from_units, 0, 3, 1, 1)
        self.sector_to_units = QtWidgets.QLabel(self.groupBox_3)
        self.sector_to_units.setText("")
        self.sector_to_units.setObjectName("sector_to_units")
        self.gridLayout_2.addWidget(self.sector_to_units, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.guide_red_slider = QtWidgets.QSlider(self.groupBox_4)
        self.guide_red_slider.setMaximum(255)
        self.guide_red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.guide_red_slider.setObjectName("guide_red_slider")
        self.gridLayout_3.addWidget(self.guide_red_slider, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.guide_blue_slider = QtWidgets.QSlider(self.groupBox_4)
        self.guide_blue_slider.setMaximum(255)
        self.guide_blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.guide_blue_slider.setObjectName("guide_blue_slider")
        self.gridLayout_3.addWidget(self.guide_blue_slider, 2, 1, 1, 1)
        self.guide_green_slider = QtWidgets.QSlider(self.groupBox_4)
        self.guide_green_slider.setMaximum(255)
        self.guide_green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.guide_green_slider.setObjectName("guide_green_slider")
        self.gridLayout_3.addWidget(self.guide_green_slider, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.guide_alpha_slider = QtWidgets.QSlider(self.groupBox_4)
        self.guide_alpha_slider.setMaximum(255)
        self.guide_alpha_slider.setOrientation(QtCore.Qt.Horizontal)
        self.guide_alpha_slider.setObjectName("guide_alpha_slider")
        self.gridLayout_3.addWidget(self.guide_alpha_slider, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.grid_size_slider = QtWidgets.QSlider(self.groupBox_4)
        self.grid_size_slider.setMinimum(1)
        self.grid_size_slider.setMaximum(100)
        self.grid_size_slider.setProperty("value", 50)
        self.grid_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.grid_size_slider.setObjectName("grid_size_slider")
        self.gridLayout_3.addWidget(self.grid_size_slider, 4, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 85))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 85))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 40))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.calculate_profiles_button = QtWidgets.QPushButton(self.tab)
        self.calculate_profiles_button.setObjectName("calculate_profiles_button")
        self.verticalLayout_6.addWidget(self.calculate_profiles_button)
        self.widget_profile = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_profile.sizePolicy().hasHeightForWidth())
        self.widget_profile.setSizePolicy(sizePolicy)
        self.widget_profile.setObjectName("widget_profile")
        self.verticalLayout_6.addWidget(self.widget_profile)
        self.export_profiles_button = QtWidgets.QPushButton(self.tab)
        self.export_profiles_button.setEnabled(False)
        self.export_profiles_button.setObjectName("export_profiles_button")
        self.verticalLayout_6.addWidget(self.export_profiles_button)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
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
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.cancel_button.clicked.connect(MainWindow.cancel_clicked)
        self.apply_button.clicked.connect(MainWindow.apply_clicked)
        self.sector_full_circle.clicked.connect(MainWindow.sector_radio_button_changed)
        self.sector_sector.clicked.connect(MainWindow.sector_radio_button_changed)
        self.guide_red_slider.sliderMoved['int'].connect(MainWindow.guide_color_changed)
        self.guide_green_slider.sliderMoved['int'].connect(MainWindow.guide_color_changed)
        self.guide_blue_slider.sliderMoved['int'].connect(MainWindow.guide_color_changed)
        self.guide_alpha_slider.sliderMoved['int'].connect(MainWindow.guide_color_changed)
        self.grid_size_slider.sliderMoved['int'].connect(MainWindow.grid_slider_moved)
        self.grid_size_slider.sliderPressed.connect(MainWindow.grid_slider_pressed)
        self.from_angle_slider.sliderMoved['int'].connect(MainWindow.sector_from_angle_moved)
        self.to_angle_slider.sliderMoved['int'].connect(MainWindow.sector_to_angle_moved)
        self.from_angle_slider.sliderPressed.connect(MainWindow.sector_from_angle_clicked)
        self.to_angle_slider.sliderPressed.connect(MainWindow.sector_to_angle_clicked)
        self.from_angle_slider.sliderReleased.connect(MainWindow.sector_from_angle_clicked)
        self.to_angle_slider.sliderReleased.connect(MainWindow.sector_to_angle_clicked)
        self.guide_red_slider.sliderPressed.connect(MainWindow.guide_color_clicked)
        self.guide_red_slider.sliderReleased.connect(MainWindow.guide_color_released)
        self.guide_green_slider.sliderPressed.connect(MainWindow.guide_color_clicked)
        self.guide_green_slider.sliderReleased.connect(MainWindow.guide_color_released)
        self.guide_blue_slider.sliderPressed.connect(MainWindow.guide_color_clicked)
        self.guide_blue_slider.sliderReleased.connect(MainWindow.guide_color_released)
        self.guide_alpha_slider.sliderPressed.connect(MainWindow.guide_color_clicked)
        self.guide_alpha_slider.sliderReleased.connect(MainWindow.guide_color_released)
        self.grid_size_slider.sliderReleased.connect(MainWindow.grid_slider_pressed)
        self.from_angle_slider.valueChanged['int'].connect(MainWindow.sector_from_angle_moved)
        self.to_angle_slider.valueChanged['int'].connect(MainWindow.sector_to_angle_moved)
        self.calculate_profiles_button.clicked.connect(MainWindow.calculate_profiles_clicked)
        self.apply_button.clicked.connect(MainWindow.export_profiles_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Circle Center"))
        self.label.setText(_translate("MainWindow", "x"))
        self.label_2.setText(_translate("MainWindow", "y"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sector"))
        self.sector_full_circle.setText(_translate("MainWindow", "Full circle"))
        self.label_3.setText(_translate("MainWindow", "or"))
        self.sector_sector.setText(_translate("MainWindow", "Sector"))
        self.sector_to_label.setText(_translate("MainWindow", "to"))
        self.sector_from_label.setText(_translate("MainWindow", "from"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Guide Color"))
        self.label_6.setText(_translate("MainWindow", "Green"))
        self.label_8.setText(_translate("MainWindow", "Transparency"))
        self.label_7.setText(_translate("MainWindow", "Blue"))
        self.label_5.setText(_translate("MainWindow", "Red"))
        self.label_9.setText(_translate("MainWindow", "Grid Size"))
        self.groupBox.setTitle(_translate("MainWindow", "Instructions"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Define <span style=\" font-weight:600;\">center of circle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Define <span style=\" font-weight:600;\">radial sector</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Initialization"))
        self.calculate_profiles_button.setText(_translate("MainWindow", "Calculate Profiles"))
        self.export_profiles_button.setText(_translate("MainWindow", "Export ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Profile"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.apply_button.setText(_translate("MainWindow", "OK"))

