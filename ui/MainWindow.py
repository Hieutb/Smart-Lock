# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        MainWindow.setMinimumSize(QtCore.QSize(350, 350))
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(50, -1, 50, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.unlockButton = QtWidgets.QPushButton(self.frame_3)
        self.unlockButton.setMinimumSize(QtCore.QSize(0, 50))
        self.unlockButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.unlockButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/unlock_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unlockButton.setIcon(icon)
        self.unlockButton.setIconSize(QtCore.QSize(25, 25))
        self.unlockButton.setObjectName("unlockButton")
        self.horizontalLayout.addWidget(self.unlockButton)
        self.unlockOptionsComboBox = QtWidgets.QComboBox(self.frame_3)
        self.unlockOptionsComboBox.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.unlockOptionsComboBox.setFont(font)
        self.unlockOptionsComboBox.setObjectName("unlockOptionsComboBox")
        self.unlockOptionsComboBox.addItem("")
        self.unlockOptionsComboBox.addItem("")
        self.horizontalLayout.addWidget(self.unlockOptionsComboBox)
        self.verticalLayout.addWidget(self.frame_3)
        self.loginAdminButton = QtWidgets.QPushButton(self.frame_2)
        self.loginAdminButton.setMinimumSize(QtCore.QSize(0, 50))
        self.loginAdminButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/images/admin_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginAdminButton.setIcon(icon1)
        self.loginAdminButton.setIconSize(QtCore.QSize(25, 25))
        self.loginAdminButton.setObjectName("loginAdminButton")
        self.verticalLayout.addWidget(self.loginAdminButton)
        self.verticalLayout_3.addWidget(self.frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BK Smart Lock"))
        self.unlockButton.setText(_translate("MainWindow", "Unlock"))
        self.unlockOptionsComboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Unlock Options</p></body></html>"))
        self.unlockOptionsComboBox.setItemText(0, _translate("MainWindow", "Face Regconition"))
        self.unlockOptionsComboBox.setItemText(1, _translate("MainWindow", "UserID/Password"))
        self.loginAdminButton.setText(_translate("MainWindow", "Login (Admin Only)"))
