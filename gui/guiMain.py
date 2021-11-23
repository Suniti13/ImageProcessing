# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/guiMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputImageLabel.setGeometry(QtCore.QRect(10, 10, 531, 531))
        self.inputImageLabel.setText("")
        self.inputImageLabel.setScaledContents(True)
        self.inputImageLabel.setObjectName("inputImageLabel")
        self.outputImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputImageLabel.setGeometry(QtCore.QRect(550, 10, 531, 531))
        self.outputImageLabel.setText("")
        self.outputImageLabel.setScaledContents(True)
        self.outputImageLabel.setObjectName("outputImageLabel")
        self.msgLabel = QtWidgets.QLabel(self.centralwidget)
        self.msgLabel.setGeometry(QtCore.QRect(10, 560, 1071, 31))
        self.msgLabel.setObjectName("msgLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 36))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExpt2 = QtWidgets.QMenu(self.menubar)
        self.menuExpt2.setObjectName("menuExpt2")
        self.menuExpt3 = QtWidgets.QMenu(self.menubar)
        self.menuExpt3.setObjectName("menuExpt3")
        self.menuExpt4 = QtWidgets.QMenu(self.menubar)
        self.menuExpt4.setObjectName("menuExpt4")
        self.menuExpt5 = QtWidgets.QMenu(self.menubar)
        self.menuExpt5.setObjectName("menuExpt5")
        self.menuExpt6 = QtWidgets.QMenu(self.menubar)
        self.menuExpt6.setObjectName("menuExpt6")
        self.menuExpt7 = QtWidgets.QMenu(self.menubar)
        self.menuExpt7.setObjectName("menuExpt7")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionRGB_to_Grey = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_Grey.setObjectName("actionRGB_to_Grey")
        self.actionNegative = QtWidgets.QAction(MainWindow)
        self.actionNegative.setObjectName("actionNegative")
        self.actionWith_Background = QtWidgets.QAction(MainWindow)
        self.actionWith_Background.setObjectName("actionWith_Background")
        self.actionWithout_Background = QtWidgets.QAction(MainWindow)
        self.actionWithout_Background.setObjectName("actionWithout_Background")
        self.actionBit_Plane_0 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_0.setObjectName("actionBit_Plane_0")
        self.actionBit_Plane_1 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_1.setObjectName("actionBit_Plane_1")
        self.actionBit_Plane_2 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_2.setObjectName("actionBit_Plane_2")
        self.actionBit_Plane_3 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_3.setObjectName("actionBit_Plane_3")
        self.actionBit_Plane_4 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_4.setObjectName("actionBit_Plane_4")
        self.actionBit_Plane_5 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_5.setObjectName("actionBit_Plane_5")
        self.actionBit_Plane_6 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_6.setObjectName("actionBit_Plane_6")
        self.actionBit_Plane_7 = QtWidgets.QAction(MainWindow)
        self.actionBit_Plane_7.setObjectName("actionBit_Plane_7")
        self.actionGrey_Level_Slicing = QtWidgets.QAction(MainWindow)
        self.actionGrey_Level_Slicing.setObjectName("actionGrey_Level_Slicing")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuExpt2.addAction(self.actionRGB_to_Grey)
        self.menuExpt3.addAction(self.actionNegative)
        self.menuExpt4.addAction(self.actionGrey_Level_Slicing)
        self.menuExpt5.addAction(self.actionBit_Plane_0)
        self.menuExpt5.addAction(self.actionBit_Plane_1)
        self.menuExpt5.addAction(self.actionBit_Plane_2)
        self.menuExpt5.addAction(self.actionBit_Plane_3)
        self.menuExpt5.addAction(self.actionBit_Plane_4)
        self.menuExpt5.addAction(self.actionBit_Plane_5)
        self.menuExpt5.addAction(self.actionBit_Plane_6)
        self.menuExpt5.addAction(self.actionBit_Plane_7)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExpt2.menuAction())
        self.menubar.addAction(self.menuExpt3.menuAction())
        self.menubar.addAction(self.menuExpt4.menuAction())
        self.menubar.addAction(self.menuExpt5.menuAction())
        self.menubar.addAction(self.menuExpt6.menuAction())
        self.menubar.addAction(self.menuExpt7.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing"))
        self.msgLabel.setText(_translate("MainWindow", "Open Image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExpt2.setTitle(_translate("MainWindow", "Expt2"))
        self.menuExpt3.setTitle(_translate("MainWindow", "Expt3"))
        self.menuExpt4.setTitle(_translate("MainWindow", "Expt4"))
        self.menuExpt5.setTitle(_translate("MainWindow", "Expt5"))
        self.menuExpt6.setTitle(_translate("MainWindow", "Expt6"))
        self.menuExpt7.setTitle(_translate("MainWindow", "Expt7"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionRGB_to_Grey.setText(_translate("MainWindow", "RGB to Grey"))
        self.actionNegative.setText(_translate("MainWindow", "Negative"))
        self.actionWith_Background.setText(_translate("MainWindow", "With Background"))
        self.actionWithout_Background.setText(_translate("MainWindow", "Without Background"))
        self.actionBit_Plane_0.setText(_translate("MainWindow", "Bit Plane 0"))
        self.actionBit_Plane_1.setText(_translate("MainWindow", "Bit Plane 1"))
        self.actionBit_Plane_2.setText(_translate("MainWindow", "Bit Plane 2"))
        self.actionBit_Plane_3.setText(_translate("MainWindow", "Bit Plane 3"))
        self.actionBit_Plane_4.setText(_translate("MainWindow", "Bit Plane 4"))
        self.actionBit_Plane_5.setText(_translate("MainWindow", "Bit Plane 5"))
        self.actionBit_Plane_6.setText(_translate("MainWindow", "Bit Plane 6"))
        self.actionBit_Plane_7.setText(_translate("MainWindow", "Bit Plane 7"))
        self.actionGrey_Level_Slicing.setText(_translate("MainWindow", "Grey Level Slicing"))
