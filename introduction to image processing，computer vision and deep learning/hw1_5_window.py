# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw1_5_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(308, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.train_pic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.train_pic_btn.setGeometry(QtCore.QRect(50, 40, 191, 41))
        self.train_pic_btn.setObjectName("train_pic_btn")
        self.hyper_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hyper_btn.setGeometry(QtCore.QRect(50, 110, 191, 41))
        self.hyper_btn.setObjectName("hyper_btn")
        self.str_btn = QtWidgets.QPushButton(self.centralwidget)
        self.str_btn.setGeometry(QtCore.QRect(50, 180, 191, 41))
        self.str_btn.setObjectName("str_btn")
        self.acc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.acc_btn.setGeometry(QtCore.QRect(50, 260, 191, 41))
        self.acc_btn.setObjectName("acc_btn")
        self.test_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_btn.setGeometry(QtCore.QRect(50, 450, 191, 41))
        self.test_btn.setObjectName("test_btn")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 380, 131, 22))
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 350, 161, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HW1_5"))
        self.train_pic_btn.setText(_translate("MainWindow", "1. Show Train Images"))
        self.hyper_btn.setText(_translate("MainWindow", "2. Show Hyperparameters"))
        self.str_btn.setText(_translate("MainWindow", "3. Show Model Structure"))
        self.acc_btn.setText(_translate("MainWindow", "4. Show Accuracy"))
        self.test_btn.setText(_translate("MainWindow", "5. Test"))
        self.label.setText(_translate("MainWindow", "Test Image Index(0~9999) "))
