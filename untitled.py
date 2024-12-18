# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1817, 855)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/logo.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 801, 831))
        self.widget.setStyleSheet("border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.995174, y2:0.336, stop:0.0543478 rgba(15, 1, 1, 255), stop:1 rgba(24, 0, 48, 255));")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 680, 141, 131))
        self.label_3.setStyleSheet("background-color: None")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("data/img/background1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(810, 20, 141, 31))
        self.lineEdit.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.0543478 rgba(74, 27, 110, 255), stop:1 rgba(24, 0, 48, 255));\n"
"font: 75 9pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(980, 20, 141, 31))
        self.lineEdit_2.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.0543478 rgba(74, 27, 110, 255), stop:1 rgba(24, 0, 48, 255));\n"
"font: 75 9pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1140, 10, 131, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("border: None")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/img/login.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(120, 150))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1400, 20, 261, 31))
        self.lineEdit_3.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.0543478 rgba(74, 27, 110, 255), stop:1 rgba(24, 0, 48, 255));\n"
"font: 75 9pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1670, 10, 101, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border: None")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("data/img/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 130))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(810, 80, 991, 101))
        self.groupBox.setStyleSheet("font: 75 10pt \"Cascadia Mono\";")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 40, 51, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/img/email.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 40, 201, 41))
        self.lineEdit_4.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px  \n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(790, 40, 161, 41))
        self.lineEdit_9.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px  \n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(480, 40, 171, 41))
        self.lineEdit_8.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px  \n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(730, 40, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("data/img/balance.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(410, 30, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("data/img/id.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 210, 991, 611))
        self.groupBox_2.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.groupBox_2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 971, 581))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.group_last_session = QtWidgets.QGroupBox(parent=self.tab_2)
        self.group_last_session.setGeometry(QtCore.QRect(150, 280, 281, 211))
        self.group_last_session.setStyleSheet("")
        self.group_last_session.setObjectName("group_last_session")
        self.label_12 = QtWidgets.QLabel(parent=self.group_last_session)
        self.label_12.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_15 = QtWidgets.QLineEdit(parent=self.group_last_session)
        self.lineEdit_15.setGeometry(QtCore.QRect(180, 90, 71, 31))
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_13 = QtWidgets.QLabel(parent=self.group_last_session)
        self.label_13.setGeometry(QtCore.QRect(40, 150, 81, 21))
        self.label_13.setObjectName("label_13")
        self.lineEdit_16 = QtWidgets.QLineEdit(parent=self.group_last_session)
        self.lineEdit_16.setGeometry(QtCore.QRect(160, 140, 91, 31))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_20 = QtWidgets.QLineEdit(parent=self.group_last_session)
        self.lineEdit_20.setGeometry(QtCore.QRect(100, 41, 151, 31))
        self.lineEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_20.setText("")
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_17 = QtWidgets.QLabel(parent=self.group_last_session)
        self.label_17.setGeometry(QtCore.QRect(40, 50, 51, 21))
        self.label_17.setObjectName("label_17")
        self.group_now_session = QtWidgets.QGroupBox(parent=self.tab_2)
        self.group_now_session.setGeometry(QtCore.QRect(560, 280, 281, 211))
        self.group_now_session.setObjectName("group_now_session")
        self.label_14 = QtWidgets.QLabel(parent=self.group_now_session)
        self.label_14.setGeometry(QtCore.QRect(30, 50, 111, 21))
        self.label_14.setObjectName("label_14")
        self.lineEdit_17 = QtWidgets.QLineEdit(parent=self.group_now_session)
        self.lineEdit_17.setGeometry(QtCore.QRect(100, 41, 151, 31))
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_15 = QtWidgets.QLabel(parent=self.group_now_session)
        self.label_15.setGeometry(QtCore.QRect(30, 100, 121, 21))
        self.label_15.setObjectName("label_15")
        self.lineEdit_18 = QtWidgets.QLineEdit(parent=self.group_now_session)
        self.lineEdit_18.setGeometry(QtCore.QRect(160, 90, 91, 31))
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_16 = QtWidgets.QLabel(parent=self.group_now_session)
        self.label_16.setGeometry(QtCore.QRect(30, 150, 71, 21))
        self.label_16.setObjectName("label_16")
        self.lineEdit_19 = QtWidgets.QLineEdit(parent=self.group_now_session)
        self.lineEdit_19.setGeometry(QtCore.QRect(160, 140, 91, 31))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(70, 49, 71, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 130, 121, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet("font: 75 10pt \"Cascadia Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgb(0, 255, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(40, 110, 101, 31))
        self.label_9.setObjectName("label_9")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(160, 110, 71, 31))
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(160, 170, 71, 31))
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 170, 121, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit_21 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(352, 40, 591, 41))
        self.lineEdit_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(163, 163, 163);\n"
"font: 9pt \"Cascadia Mono\";")
        self.lineEdit_21.setText("")
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.checkBox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(570, 90, 71, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(630, 90, 91, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 40, 51, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: None ")
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("data/img/infobot.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1817, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIPredict"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Key"))
        self.groupBox.setTitle(_translate("MainWindow", "Account"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Control"))
        self.group_last_session.setTitle(_translate("MainWindow", "Last Session"))
        self.label_12.setText(_translate("MainWindow", "Close Price"))
        self.label_13.setText(_translate("MainWindow", "Signal"))
        self.label_17.setText(_translate("MainWindow", "Time"))
        self.group_now_session.setTitle(_translate("MainWindow", "Now Session"))
        self.label_14.setText(_translate("MainWindow", "Session"))
        self.label_15.setText(_translate("MainWindow", "Price Feed"))
        self.label_16.setText(_translate("MainWindow", "Signal"))
        self.label_8.setText(_translate("MainWindow", "Amount"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Bot"))
        self.label_9.setText(_translate("MainWindow", "Stop Loss"))
        self.label_10.setText(_translate("MainWindow", "Take Profit"))
        self.checkBox.setText(_translate("MainWindow", "UP"))
        self.checkBox_2.setText(_translate("MainWindow", "DOWN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
