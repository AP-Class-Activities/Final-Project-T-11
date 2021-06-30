# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saller.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"background-color: rgb(170, 170, 255);\n"
"background-color: rgb(170, 170, 255);\n"
"background-color: rgb(85, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(476, 140, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(506, 180, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(496, 220, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(506, 260, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(506, 300, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(142, 100, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 140, 331, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(142, 180, 331, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(142, 220, 331, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(142, 260, 331, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 300, 331, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 420, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 420, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "صفحه فروشنده"))
        self.label_2.setText(_translate("MainWindow", "نام"))
        self.label_3.setText(_translate("MainWindow", "نام خانوادگی"))
        self.label_4.setText(_translate("MainWindow", "آدرس"))
        self.label_5.setText(_translate("MainWindow", "شماره تلقن"))
        self.label_6.setText(_translate("MainWindow", "ایمیل"))
        self.label_7.setText(_translate("MainWindow", "رمز ورود"))
        self.pushButton.setText(_translate("MainWindow", "ورود"))
        self.pushButton_2.setText(_translate("MainWindow", "انصراف"))


#category
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 658)
        Form.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 130, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 130, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 310, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 310, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "میوه و سبزیجات"))
        self.pushButton_2.setText(_translate("Form", "مواد غذایی"))
        self.pushButton_3.setText(_translate("Form", "پوشاک"))
        self.pushButton_4.setText(_translate("Form", "آرایشی و بهداشتی"))


#cosmetic
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 689)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(630, 20, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 61, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 0, 0);\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " آرایشی و بهداشتی :"))
        self.label_2.setText(_translate("Form", "قیمت "))
        self.label_3.setText(_translate("Form", "نام محصول "))
        self.pushButton_6.setText(_translate("Form", "بازگشت"))


#fruits and vegetables
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 689)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(660, 20, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 61, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 0, 0);\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " میوه و سبزیجات :"))
        self.label_2.setText(_translate("Form", "قیمت "))
        self.label_3.setText(_translate("Form", "نام محصول "))
        self.pushButton_6.setText(_translate("Form", "بازگشت"))


#wearings
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 689)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(740, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 20, 61, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 0, 0);\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " پوشاک :"))
        self.label_2.setText(_translate("Form", "قیمت "))
        self.label_3.setText(_translate("Form", "نام محصول "))
        self.pushButton_6.setText(_translate("Form", "بازگشت"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
