from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 281, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("index.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(474, 360, 81, 31))
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.customer = QtWidgets.QPushButton(self.centralwidget)
        self.customer.setGeometry(QtCore.QRect(270, 360, 81, 31))
        self.customer.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.customer.setObjectName("customer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "فروشنده"))
        self.customer.setText(_translate("MainWindow", "مشتری"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
