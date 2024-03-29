from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 80, 321, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Downloads/index.jpg"))
        self.label.setObjectName("label")
        self.saller = QtWidgets.QPushButton(self.centralwidget)
        self.saller.setGeometry(QtCore.QRect(270, 410, 81, 31))
        self.saller.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.saller.setObjectName("saller")
        self.saller.clicked.connect(self.toaccountpage2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 410, 81, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toaccountpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def toaccountpage(self):
        self.account = QtWidgets.QMainWindow()
        self.ui = Ui_account()
        self.ui.setupUi(self.account)
        Form.hide()
        self.account.show()
    
    def toaccountpage2(self):
        self.accountt = QtWidgets.QMainWindow()
        self.ui = Ui_accountt()
        self.ui.setupUi(self.accountt)
        Form.hide()
        self.accountt.show()
        





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saller.setText(_translate("MainWindow", "فروشنده"))
        self.pushButton_2.setText(_translate("MainWindow", "مشتری"))


class Ui_account(object):
    def setupUi(self, account):
        account.setObjectName("account")
        account.resize(800, 600)
        account.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(account)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 50, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 361, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Downloads/photo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 280, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 370, 75, 31))
        self.pushButton.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tostartcus)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 370, 75, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(5, 189, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.tologin)
        account.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(account)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        account.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(account)
        self.statusbar.setObjectName("statusbar")
        account.setStatusBar(self.statusbar)

        self.retranslateUi(account)
        QtCore.QMetaObject.connectSlotsByName(account)
        
        

    def tologin(self):
            self.login = QtWidgets.QMainWindow()
            self.ui = Ui_login()
            self.ui.setupUi(self.login)
            self.login.show()
        
        
    def tostartcus(self):
        self.start = QtWidgets.QMainWindow()
        self.ui = Ui_start()
        self.ui.setupUi(self.start)
        self.start.show()
        
            
        

    def retranslateUi(self, account):
        _translate = QtCore.QCoreApplication.translate
        account.setWindowTitle(_translate("account", "MainWindow"))
        self.label_3.setText(_translate("account", "آیا قبلا عضو شدید؟"))
        self.pushButton.setText(_translate("account", "خیر"))
        self.pushButton_2.setText(_translate("account", "بله"))


class Ui_accountt(object):
    def setupUi(self, account):
        account.setObjectName("account")
        account.resize(800, 600)
        account.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(account)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 50, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 361, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Downloads/photo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 280, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 370, 75, 31))
        self.pushButton.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tostartsal)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 370, 75, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(5, 189, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.tologin)
        account.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(account)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        account.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(account)
        self.statusbar.setObjectName("statusbar")
        account.setStatusBar(self.statusbar)

        self.retranslateUi(account)
        QtCore.QMetaObject.connectSlotsByName(account)


    def tologin(self):
            self.login2 = QtWidgets.QMainWindow()
            self.ui = Ui_login2()
            self.ui.setupUi(self.login2)
            self.login2.show()


    def tostartsal(self):
        self.starts = QtWidgets.QMainWindow()
        self.ui = Ui_starts()
        self.ui.setupUi(self.starts)
        self.starts.show()
    
    
    def retranslateUi(self, account):
        _translate = QtCore.QCoreApplication.translate
        account.setWindowTitle(_translate("account", "MainWindow"))
        self.label_3.setText(_translate("account", "آیا قبلا عضو شدید؟"))
        self.pushButton.setText(_translate("account", "خیر"))
        self.pushButton_2.setText(_translate("account", "بله"))


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(800, 600)
        login.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 351, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Downloads/images.jpg"))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 340, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(212, 300, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(212, 340, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 440, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tocategory)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 440, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toaccountpage)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(506, 300, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

        #f = open('database.txt', 'r+')
        #username = input()
        #password = input()
        #s = f.write("\n"+username+" "+password)
        #f.close()
        
    def tocategory(self):
        self.category = QtWidgets.QMainWindow()
        self.ui = Ui_category()
        self.ui.setupUi(self.category)
        Form.hide()
        self.category.show()

        
    def toaccountpage(self):
        self.account = QtWidgets.QMainWindow()
        self.ui = Ui_account()
        self.ui.setupUi(self.account)
        Form.hide()
        self.account.show()

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.label_4.setText(_translate("login", "رمز ورود"))
        self.pushButton.setText(_translate("login", "تایید"))
        self.pushButton_2.setText(_translate("login","بازگشت"))
        self.label_2.setText(_translate("login", "نام کاربری"))


class Ui_login2(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(800, 600)
        login.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 351, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Downloads/images.jpg"))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 340, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(212, 300, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(212, 340, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 440, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tocategories)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 440, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toaccountpage2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(506, 300, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

        #f = open('database.txt', 'r+')
        #username = input()
        #password = input()
        #s = f.write("\n"+username+" "+password)
        #f.close()
        
    def tocategories(self):
        self.categories = QtWidgets.QMainWindow()
        self.ui = Ui_categories()
        self.ui.setupUi(self.categories)
        Form.hide()
        self.categories.show()

    def toaccountpage2(self):
        self.accountt = QtWidgets.QMainWindow()
        self.ui = Ui_accountt()
        self.ui.setupUi(self.accountt)
        Form.hide()
        self.accountt.show()
    
    
    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.label_4.setText(_translate("login", "رمز ورود"))
        self.pushButton.setText(_translate("login", "تایید"))
        self.pushButton_2.setText(_translate("login", "بازگشت"))
        self.label_2.setText(_translate("login", "نام کاربری"))
                      
                
class Ui_start(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(800, 600)
        start.setStyleSheet("background-color: rgb(255, 170, 255);\n"
    "background-color: rgb(255, 255, 127);\n"
    "background-color: rgb(255, 255, 0);\n"
    "background-color: rgb(255, 255, 127);\n"
    "background-color: rgb(255, 255, 127);\n"
    "background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(start)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(496, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 190, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 230, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 270, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 310, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 340, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 150, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 381, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 190, 381, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 230, 381, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 270, 381, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 310, 381, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 470, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tocategory)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 470, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toaccountpage)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 350, 381, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        start.setCentralWidget(self.centralwidget)

        self.retranslateUi(start)
        QtCore.QMetaObject.connectSlotsByName(start)

        #f = open('database.txt', 'r+')
        #password = input()
        #password = input()
        #s = f.readlines()
        #s = [j for i in s for j in i.split()]
        #emkanSabtnam = True
        #for k in range(0, len(s), 2):
        #    if username == s[k]:
        #        emkanSabtnam = False
        #        print('in name karbari tekrari ast!')
        #    break
        #f.close()
        #if emkanSabtnam:
        #    f = open('database.txt', 'a+')
        #    f.write(f'{username} {password}\n')
        #    print('sabtname ba mofaghiat anjam shod!')
        #    f.close()



    def tocategory(self):
        self.category = QtWidgets.QMainWindow()
        self.ui = Ui_category()
        self.ui.setupUi(self.category)
        Form.hide()
        self.category.show()

    def toaccountpage(self):
        self.account = QtWidgets.QMainWindow()
        self.ui = Ui_account()
        self.ui.setupUi(self.account)
        Form.hide()
        self.account.show()
    
    
    
    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "MainWindow"))
        self.label.setText(_translate("start", "صفحه مشتری"))
        self.label_2.setText(_translate("start", "نام"))
        self.label_3.setText(_translate("start", "نام خانوادگی"))
        self.label_4.setText(_translate("start", "آدرس"))
        self.label_5.setText(_translate("start", "شماره تلفن"))
        self.label_6.setText(_translate("start", "ایمیل"))
        self.label_7.setText(_translate("start", "جنسیت"))
        self.label_8.setText(_translate("start", "رمز ورود"))
        self.pushButton.setText(_translate("start", "تایید"))
        self.pushButton_2.setText(_translate("start", "انصراف"))


class Ui_starts(object):
    def setupUi(self, starts):
        starts.setObjectName("starts")
        starts.resize(800, 600)
        starts.setStyleSheet("background-color: rgb(255, 170, 255);\n"
    "background-color: rgb(255, 255, 127);\n"
    "background-color: rgb(255, 255, 0);\n"
    "background-color: rgb(255, 255, 127);\n"
    "background-color: rgb(255, 255, 127);\n"
    "background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(starts)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(496, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 190, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 230, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 270, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 310, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 340, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 150, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 381, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 190, 381, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 230, 381, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 270, 381, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 310, 381, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 470, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tocategories)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 470, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toaccountpage2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 350, 381, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        starts.setCentralWidget(self.centralwidget)

        self.retranslateUi(starts)
        QtCore.QMetaObject.connectSlotsByName(starts)

        #f = open('database.txt', 'r+')
        #password = input()
        #password = input()
        #s = f.readlines()
        #s = [j for i in s for j in i.split()]
        #emkanSabtnam = True
        #for k in range(0, len(s), 2):
        #    if username == s[k]:
        #        emkanSabtnam = False
        #        print('in name karbari tekrari ast!')
        #    break
        #f.close()
        #if emkanSabtnam:
        #    f = open('database.txt', 'a+')
        #    f.write(f'{username} {password}\n')
        #    print('sabtname ba mofaghiat anjam shod!')
        #    f.close()


    
    
    def tocategories(self):
        self.categories = QtWidgets.QMainWindow()
        self.ui = Ui_categories()
        self.ui.setupUi(self.categories)
        Form.hide()
        self.categories.show()
    
    
    def toaccountpage2(self):
        self.accountt = QtWidgets.QMainWindow()
        self.ui = Ui_accountt()
        self.ui.setupUi(self.accountt)
        Form.hide()
        self.accountt.show()
    
    
    
    def retranslateUi(self, starts):
        _translate = QtCore.QCoreApplication.translate
        starts.setWindowTitle(_translate("starts", "MainWindow"))
        self.label.setText(_translate("starts", "صفحه فروشنده"))
        self.label_2.setText(_translate("starts", "نام"))
        self.label_3.setText(_translate("starts", "نام خانوادگی"))
        self.label_4.setText(_translate("starts", "آدرس"))
        self.label_5.setText(_translate("starts", "شماره تلفن"))
        self.label_6.setText(_translate("starts", "ایمیل"))
        self.label_7.setText(_translate("starts", "جنسیت"))
        self.label_8.setText(_translate("starts", "رمز ورود"))
        self.pushButton.setText(_translate("starts", "تایید"))
        self.pushButton_2.setText(_translate("starts", "انصراف"))









class Ui_categories(object):
    def setupUi(self, category):
        category.setObjectName("category")
        category.resize(800, 595)
        category.setStyleSheet("\n"
    "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(category)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 110, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.toFruitsAndVegetables)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
    "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 380, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.tocosmetics)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
    "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 380, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(self.toclothes)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
    "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 110, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);\n"
    "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.tofood)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 542, 81, 31))
        self.pushButton_5.setStyleSheet("background-color:rgb(255, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.tologin)
        category.setCentralWidget(self.centralwidget)

        self.retranslateUi(category)
        QtCore.QMetaObject.connectSlotsByName(category)
      
      
      
      
      
      
        
    def toFruitsAndVegetables(self):
        self.FruitsAndVegetables = QtWidgets.QMainWindow()
        self.ui = Ui_FruitsAndVegetables()
        self.ui.setupUi(self.FruitsAndVegetables)
        Form.hide()
        self.FruitsAndVegetables.show()
        
    def tofood(self):
        self.food = QtWidgets.QMainWindow()
        self.ui = Ui_food()
        self.ui.setupUi(self.food)
        Form.hide()
        self.food.show()
        
    def toclothes(self):
        self.clothes = QtWidgets.QMainWindow()
        self.ui = Ui_clothes()
        self.ui.setupUi(self.clothes)
        Form.hide()
        self.clothes.show()    
        
    def tocosmetics(self):
        self.cosmetics = QtWidgets.QMainWindow()
        self.ui = Ui_cosmetics()
        self.ui.setupUi(self.cosmetics)
        Form.hide()
        self.cosmetics.show()    
        
    def tologin(self):
            self.login2 = QtWidgets.QMainWindow()
            self.ui = Ui_login2()
            self.ui.setupUi(self.login2)
            self.login2.show()
    
    
    

    def retranslateUi(self, category):
        _translate = QtCore.QCoreApplication.translate
        category.setWindowTitle(_translate("category", "MainWindow"))
        self.pushButton.setText(_translate("category", "میوه و سبزیجات"))
        self.pushButton_2.setText(_translate("category", "آرایشی و بهداشتی"))
        self.pushButton_3.setText(_translate("category", "پوشاک"))
        self.pushButton_4.setText(_translate("category", "مواد غذایی"))
        self.pushButton_5.setText(_translate("category", "بازگشت"))



class Ui_food(object):
    def setupUi(self, food):
        food.setObjectName("food")
        food.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        food.setFont(font)
        food.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(food)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.tocategories)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 81, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 230, 81, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 81, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 451, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 230, 451, 41))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 302, 451, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 372, 451, 41))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 370, 81, 41))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(696, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        food.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(food)
        self.statusbar.setObjectName("statusbar")
        food.setStatusBar(self.statusbar)

        self.retranslateUi(food)
        QtCore.QMetaObject.connectSlotsByName(food)
        
    def tocategories(self):
        self.categories = QtWidgets.QMainWindow()
        self.ui = Ui_categories()
        self.ui.setupUi(self.categories)
        Form.hide()
        self.categories.show()

    def retranslateUi(self, food):
        _translate = QtCore.QCoreApplication.translate
        food.setWindowTitle(_translate("food", "MainWindow"))
        self.pushButton.setText(_translate("food", "بازگشت"))
        self.label.setText(_translate("food", "قیمت"))
        self.label_11.setText(_translate("food", "نام محصول "))
        self.label_12.setText(_translate("food", "مواد غذایی"))


class Ui_FruitsAndVegetables(object):
    def setupUi(self, FruitsAndVegetables):
        FruitsAndVegetables.setObjectName("FruitsAndVegetables")
        FruitsAndVegetables.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        FruitsAndVegetables.setFont(font)
        FruitsAndVegetables.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(FruitsAndVegetables)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.tocategories)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 81, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 230, 81, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 81, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 451, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 230, 451, 41))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 302, 451, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 372, 451, 41))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 370, 81, 41))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(656, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        FruitsAndVegetables.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FruitsAndVegetables)
        self.statusbar.setObjectName("statusbar")
        FruitsAndVegetables.setStatusBar(self.statusbar)

        self.retranslateUi(FruitsAndVegetables)
        QtCore.QMetaObject.connectSlotsByName(FruitsAndVegetables)
        
        
    def tocategories(self):
        self.categories = QtWidgets.QMainWindow()
        self.ui = Ui_categories()
        self.ui.setupUi(self.categories)
        Form.hide()
        self.categories.show()

    def retranslateUi(self, FruitsAndVegetables):
        _translate = QtCore.QCoreApplication.translate
        FruitsAndVegetables.setWindowTitle(_translate("FruitsAndVegetables", "MainWindow"))
        self.pushButton.setText(_translate("FruitsAndVegetables", "بازگشت"))
        self.label.setText(_translate("FruitsAndVegetables", "قیمت"))
        self.label_11.setText(_translate("FruitsAndVegetables", "نام محصول "))
        self.label_12.setText(_translate("FruitsAndVegetables", "میوه و سبزیجات"))


class Ui_clothes(object):
    def setupUi(self, clothes):
        clothes.setObjectName("clothes")
        clothes.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        clothes.setFont(font)
        clothes.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(clothes)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.tocategories)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 81, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 230, 81, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 81, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 451, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 230, 451, 41))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 302, 451, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 372, 451, 41))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 370, 81, 41))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(696, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        clothes.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(clothes)
        self.statusbar.setObjectName("statusbar")
        clothes.setStatusBar(self.statusbar)

        self.retranslateUi(clothes)
        QtCore.QMetaObject.connectSlotsByName(clothes)
        
        
    def tocategories(self):
        self.categories = QtWidgets.QMainWindow()
        self.ui = Ui_categories()
        self.ui.setupUi(self.categories)
        Form.hide()
        self.categories.show()
    
    

    def retranslateUi(self, clothes):
        _translate = QtCore.QCoreApplication.translate
        clothes.setWindowTitle(_translate("clothes", "MainWindow"))
        self.pushButton.setText(_translate("clothes", "بازگشت"))
        self.label.setText(_translate("clothes", "قیمت"))
        self.label_11.setText(_translate("clothes", "نام محصول "))
        self.label_12.setText(_translate("clothes", "پوشاک"))


class Ui_cosmetics(object):
    def setupUi(self, cosmetics):
        cosmetics.setObjectName("cosmetics")
        cosmetics.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        cosmetics.setFont(font)
        cosmetics.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(cosmetics)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.tocategories)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 81, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 230, 81, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 81, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 451, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 230, 451, 41))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 302, 451, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 372, 451, 41))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 370, 81, 41))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(616, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 0, 0);\n"
    "\n"
    "")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        cosmetics.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cosmetics)
        self.statusbar.setObjectName("statusbar")
        cosmetics.setStatusBar(self.statusbar)

        self.retranslateUi(cosmetics)
        QtCore.QMetaObject.connectSlotsByName(cosmetics)


    def tocategories(self):
        self.categories = QtWidgets.QMainWindow()
        self.ui = Ui_categories()
        self.ui.setupUi(self.categories)
        Form.hide()
        self.categories.show()

    def retranslateUi(self, cosmetics):
        _translate = QtCore.QCoreApplication.translate
        cosmetics.setWindowTitle(_translate("cosmetics", "MainWindow"))
        self.pushButton.setText(_translate("cosmetics", "بازگشت"))
        self.label.setText(_translate("cosmetics", "قیمت"))
        self.label_11.setText(_translate("cosmetics", "نام محصول "))
        self.label_12.setText(_translate("cosmetics", "آرایشی و بهداشتی"))
        
















class Ui_category(object):
    def setupUi(self, categories):
        categories.setObjectName("categories")
        categories.resize(800, 600)
        categories.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(categories)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 120, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 420, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.tologin)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(16, 10, 291, 291))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Downloads/index2.jpg"))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 210, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.tofoods)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 260, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.tofruts)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 310, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.tocosmetic)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 360, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.toshirts)
        categories.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(categories)
        self.statusbar.setObjectName("statusbar")
        categories.setStatusBar(self.statusbar)

        self.retranslateUi(categories)
        QtCore.QMetaObject.connectSlotsByName(categories)


    def tologin(self):
            self.login = QtWidgets.QMainWindow()
            self.ui = Ui_login()
            self.ui.setupUi(self.login)
            self.login.show()
            
            
    def tocosmetic(self):
            self.cosmetic = QtWidgets.QMainWindow()
            self.ui = Ui_cosmetic()
            self.ui.setupUi(self.cosmetic)
            self.cosmetic.show()
            
    def toshirts(self):
            self.shirts = QtWidgets.QMainWindow()
            self.ui = Ui_shirts()
            self.ui.setupUi(self.shirts)
            self.shirts.show()

    def tofoods(self):
            self.foods = QtWidgets.QMainWindow()
            self.ui = Ui_foods()
            self.ui.setupUi(self.foods)
            self.foods.show()
            
            
    def tofruts(self):
            self.fruts = QtWidgets.QMainWindow()
            self.ui = Ui_fruts()
            self.ui.setupUi(self.fruts)
            self.fruts.show()
            
            
            
    

    def retranslateUi(self, categories):
        _translate = QtCore.QCoreApplication.translate
        categories.setWindowTitle(_translate("categories", "MainWindow"))
        self.label.setText(_translate("categories", "خرید محصول"))
        self.label_2.setText(_translate("categories", "قصد خرید چه کالایی را دارید؟"))
        self.pushButton_2.setText(_translate("categories", "بازگشت"))
        self.pushButton_3.setText(_translate("categories", "مواد غذایی"))
        self.pushButton_4.setText(_translate("categories", "میوه و سبزیجات"))
        self.pushButton_5.setText(_translate("categories", "آرایشی و بهداشتی"))
        self.pushButton_6.setText(_translate("categories", "پوشاک"))
       

class Ui_cosmetic(object):
    def setupUi(self, cosmetic):
        cosmetic.setObjectName("cosmetic")
        cosmetic.resize(800, 600)
        cosmetic.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(cosmetic)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, -10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 40, 431, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Downloads/استند طبقه ای لوازم آرایش.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 100, 101, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 150, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 340, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 370, 581, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 400, 491, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 450, 301, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 500, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.tocart)
        cosmetic.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cosmetic)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        cosmetic.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cosmetic)
        self.statusbar.setObjectName("statusbar")
        cosmetic.setStatusBar(self.statusbar)

        self.retranslateUi(cosmetic)
        QtCore.QMetaObject.connectSlotsByName(cosmetic)
        
        
    def tocart(self):
        self.cart = QtWidgets.QMainWindow()
        self.ui = Ui_cart()
        self.ui.setupUi(self.cart)
        Form.hide()
        self.cart.show()

    def retranslateUi(self, cosmetic):
        _translate = QtCore.QCoreApplication.translate
        cosmetic.setWindowTitle(_translate("cosmetic", "MainWindow"))
        self.label.setText(_translate("cosmetic", "آرایشی بهداشتی"))
        self.label_3.setText(_translate("cosmetic", "استند لوازم آرایشی"))
        self.label_4.setText(_translate("cosmetic", "قیمت:29900"))
        self.pushButton.setText(_translate("cosmetic", "+"))
        self.label_5.setText(_translate("cosmetic", "نظرات کاربران:"))
        self.label_6.setText(_translate("cosmetic", "وقتی برای من فرستادن قشنگ بسته بندی کرده بودن داخل جعبه گزاشته بودن و محکم و سالم بود من که خیلی دوسش دارم"))
        self.label_7.setText(_translate("cosmetic", "جنس محکمی داره شفاف بود کوچیکه ولی کار راه اندازه. برا مرتب چیدن وسایل آرایشی کوچیک خوبه"))
        self.pushButton_2.setText(_translate("cosmetic", "دیدگاه و نظر شما کاربر عزیز"))
        self.pushButton_3.setText(_translate("cosmetic", "تایید"))


class Ui_shirts(object):
    def setupUi(self, shirts):
        shirts.setObjectName("shirts")
        shirts.resize(800, 600)
        shirts.setStyleSheet("background-color: rgb(85, 85, 255);\n"
    "background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(shirts)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(366, 0, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 70, 561, 411))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Downloads/تی-شرت-ارزان-4.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 151, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 190, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 290, 191, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(146, 270, 121, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 310, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 150, 101, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(64, 410, 201, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 520, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.tocart)
        shirts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(shirts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        shirts.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(shirts)
        self.statusbar.setObjectName("statusbar")
        shirts.setStatusBar(self.statusbar)

        self.retranslateUi(shirts)
        QtCore.QMetaObject.connectSlotsByName(shirts)
        
        
    def tocart(self):
        self.cart = QtWidgets.QMainWindow()
        self.ui = Ui_cart()
        self.ui.setupUi(self.cart)
        Form.hide()
        self.cart.show()
        

    def retranslateUi(self, shirts):
        _translate = QtCore.QCoreApplication.translate
        shirts.setWindowTitle(_translate("shirts", "MainWindow"))
        self.label.setText(_translate("shirts", "پوشاک"))
        self.label_3.setText(_translate("shirts", "تیشرت مردانه"))
        self.label_4.setText(_translate("shirts", "در 11 رنگ"))
        self.label_5.setText(_translate("shirts", "دارای سه سایز x.xl.xxl"))
        self.pushButton.setText(_translate("shirts", "+"))
        self.label_6.setText(_translate("shirts", "نظرات کاربران:"))
        self.label_7.setText(_translate("shirts", "جنس خوب نداره "))
        self.label_8.setText(_translate("shirts", "از جنس راضی نبودم"))
        self.label_9.setText(_translate("shirts", "خیلی خنکه"))
        self.label_10.setText(_translate("shirts", "قیمت:30000"))
        self.pushButton_2.setText(_translate("shirts", "ثبت دیدگاه و نظر شما کاربر عزیز"))
        self.pushButton_3.setText(_translate("shirts", "تایید"))


class Ui_foods(object):
    def setupUi(self, foods):
        foods.setObjectName("foods")
        foods.resize(801, 600)
        foods.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(foods)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -10, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 10, 151, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Downloads/index3.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 60, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 140, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(676, 260, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 290, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 320, 161, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(710, 340, 81, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 50, 241, 211))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Downloads/Untitled-17-min-1-300x300.jpg"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-10, 60, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(106, 110, 91, 20))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 140, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(296, 290, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(350, 320, 101, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(390, 340, 61, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 370, 431, 20))
        self.label_15.setObjectName("label_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(344, 460, 281, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 520, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.tocart)
        foods.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(foods)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        foods.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(foods)
        self.statusbar.setObjectName("statusbar")
        foods.setStatusBar(self.statusbar)

        self.retranslateUi(foods)
        QtCore.QMetaObject.connectSlotsByName(foods)
        
        
    def tocart(self):
        self.cart = QtWidgets.QMainWindow()
        self.ui = Ui_cart()
        self.ui.setupUi(self.cart)
        Form.hide()
        self.cart.show()

    def retranslateUi(self, foods):
        _translate = QtCore.QCoreApplication.translate
        foods.setWindowTitle(_translate("foods", "MainWindow"))
        self.label.setText(_translate("foods", "مواد غذایی"))
        self.label_3.setText(_translate("foods", "روغن سرخ کردنی غنچه"))
        self.label_4.setText(_translate("foods", "قیمت: 13000"))
        self.pushButton.setText(_translate("foods", "+"))
        self.label_5.setText(_translate("foods", "نظرات کاربران:"))
        self.label_6.setText(_translate("foods", "کیفیت عالی"))
        self.label_7.setText(_translate("foods", "قیمت مناسب اما مثل روغنای دیگه"))
        self.label_8.setText(_translate("foods", "بد نبود"))
        self.label_10.setText(_translate("foods", "ماکارونی سدانو"))
        self.label_11.setText(_translate("foods", "قیمت: 7360"))
        self.pushButton_2.setText(_translate("foods", "+"))
        self.label_12.setText(_translate("foods", "نظرات کاربران:"))
        self.label_13.setText(_translate("foods", "برای خونه لازمه"))
        self.label_14.setText(_translate("foods", "خوبه"))
        self.label_15.setText(_translate("foods", "خیلی خوب بود راضی بودم دنبال تک‌ماکارون بودم ولی پیدا نکردم زر سفارش دادم"))
        self.pushButton_3.setText(_translate("foods", "ثبت دیدگاه و نظر شما کاربر عزیز"))
        self.pushButton_4.setText(_translate("foods", "تایید"))


class Ui_fruts(object):
    def setupUi(self, fruts):
        fruts.setObjectName("fruts")
        fruts.resize(800, 600)
        fruts.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(fruts)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, -10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 30, 271, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Downloads/index4.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(436, 60, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(456, 100, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 150, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(666, 260, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 300, 201, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 340, 411, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 370, 211, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 50, 261, 241))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Downloads/هلو.jpg"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 60, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 90, 71, 20))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 140, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(170, 310, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(166, 340, 131, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(140, 370, 161, 20))
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 480, 271, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 510, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.tocart)
        fruts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fruts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        fruts.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fruts)
        self.statusbar.setObjectName("statusbar")
        fruts.setStatusBar(self.statusbar)

        self.retranslateUi(fruts)
        QtCore.QMetaObject.connectSlotsByName(fruts)


    def tocart(self):
        self.cart = QtWidgets.QMainWindow()
        self.ui = Ui_cart()
        self.ui.setupUi(self.cart)
        Form.hide()
        self.cart.show()


    def retranslateUi(self, fruts):
        _translate = QtCore.QCoreApplication.translate
        fruts.setWindowTitle(_translate("fruts", "MainWindow"))
        self.label.setText(_translate("fruts", "میوه و سبزیجات"))
        self.label_3.setText(_translate("fruts", "هندوانه ممتاز فله"))
        self.label_4.setText(_translate("fruts", "قیمت:51700"))
        self.pushButton.setText(_translate("fruts", "+"))
        self.label_5.setText(_translate("fruts", "نظرات کاربران:"))
        self.label_6.setText(_translate("fruts", "هندوانه با کیفیت ، شیرین ، ترد و قرمزی بود"))
        self.label_7.setText(_translate("fruts", "همیشه ، کیفیت هندوانه عالی بود ولی این بار ، تمام هندوانه را بعد از بریدن ، انداختم دور "))
        self.label_8.setText(_translate("fruts", "خوب و شیرین بود انتظار نداشتم خوب باشه"))
        self.label_10.setText(_translate("fruts", "هلو "))
        self.label_11.setText(_translate("fruts", "قیمت:40250"))
        self.pushButton_2.setText(_translate("fruts", "+"))
        self.label_12.setText(_translate("fruts", "نظرات کاربران:"))
        self.label_13.setText(_translate("fruts", "از خریدم راضی هستم"))
        self.label_14.setText(_translate("fruts", "از نظر کیفیت عالی بود مرسی"))
        self.pushButton_3.setText(_translate("fruts", "ثبت دیدگاه و نظر شما کاربر عزیز"))
        self.pushButton_4.setText(_translate("fruts", "تایید"))







class Ui_cart(object):
    def setupUi(self, cart):
        cart.setObjectName("cart")
        cart.resize(800, 600)
        cart.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(cart)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 110, 721, 411))
        self.frame.setStyleSheet("background-color: rgb(0, 47, 71)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(10)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 661, 41))
        self.label_3.setStyleSheet("background-color: rgb(252, 255, 179);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 149, 661, 41))
        self.label_4.setStyleSheet("background-color: rgb(252, 255, 179);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 209, 661, 41))
        self.label_5.setStyleSheet("background-color: rgb(252, 255, 179);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 661, 41))
        self.label_6.setStyleSheet("background-color: rgb(252, 255, 179);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 661, 41))
        self.label_2.setStyleSheet("background-color: rgb(252, 255, 179);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(252, 255, 179);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 540, 111, 41))
        self.pushButton_2.setStyleSheet("background-color:rgb(5, 189, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.topay)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 540, 111, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tocategory)
        cart.setCentralWidget(self.centralwidget)

        self.retranslateUi(cart)
        QtCore.QMetaObject.connectSlotsByName(cart)
        
        
    def topay(self):
        self.pay = QtWidgets.QMainWindow()
        self.ui = Ui_pay()
        self.ui.setupUi(self.pay)
        Form.hide()
        self.pay.show()


    def tocategory(self):
        self.category = QtWidgets.QMainWindow()
        self.ui = Ui_category()
        self.ui.setupUi(self.category)
        Form.hide()
        self.category.show()




    def retranslateUi(self, cart):
        _translate = QtCore.QCoreApplication.translate
        cart.setWindowTitle(_translate("cart", "MainWindow"))
        self.label.setText(_translate("cart", "سبد خرید"))
        self.label_6.setText(_translate("cart", "..."))
        self.label_7.setText(_translate("cart", "مجموع ----------------------------------------------------------------------------------------  (           )"))
        self.pushButton_2.setText(_translate("cart", "تایید"))
        self.pushButton.setText(_translate("cart", "انصراف"))


class Ui_pay(object):
    def setupUi(self, pay):
        pay.setObjectName("pay")
        pay.resize(800, 600)
        pay.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(pay)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(310, 270, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton.setStyleSheet("background-color:rgb(217, 255, 255);\n"
    "")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(310, 340, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_2.setStyleSheet("background-color:rgb(217, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 410, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_3.setStyleSheet("background-color:rgb(217, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 140, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(217, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 480, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tofinal)
        pay.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pay)
        self.statusbar.setObjectName("statusbar")
        pay.setStatusBar(self.statusbar)

        self.retranslateUi(pay)
        QtCore.QMetaObject.connectSlotsByName(pay)
        
        
    def tofinal(self):
        self.FinalRegistration = QtWidgets.QMainWindow()
        self.ui = Ui_FinalRegistration()
        self.ui.setupUi(self.FinalRegistration)
        Form.hide()
        self.FinalRegistration.show()

    def retranslateUi(self, pay):
        _translate = QtCore.QCoreApplication.translate
        pay.setWindowTitle(_translate("pay", "MainWindow"))
        self.radioButton.setText(_translate("pay", "پرداخت آنلاین"))
        self.radioButton_2.setText(_translate("pay", "پرداخت در محل"))
        self.radioButton_3.setText(_translate("pay", "پرداخت با کارت هدیه"))
        self.label.setText(_translate("pay", "نحوه ی پرداخت را انتخاب کنید:"))
        self.pushButton.setText(_translate("pay", "تایید"))


class Ui_FinalRegistration(object):
    def setupUi(self, FinalRegistration):
        FinalRegistration.setObjectName("FinalRegistration")
        FinalRegistration.resize(800, 600)
        FinalRegistration.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(FinalRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 150, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 340, 91, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tocategory)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 340, 91, 41))
        self.pushButton_2.setStyleSheet("background-color:rgb(5, 187, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.tothank)
        FinalRegistration.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FinalRegistration)
        self.statusbar.setObjectName("statusbar")
        FinalRegistration.setStatusBar(self.statusbar)

        self.retranslateUi(FinalRegistration)
        QtCore.QMetaObject.connectSlotsByName(FinalRegistration)
        
        
        
    def tocategory(self):
        self.category = QtWidgets.QMainWindow()
        self.ui = Ui_category()
        self.ui.setupUi(self.category)
        Form.hide()
        self.category.show()
        
        
    def tothank(self):
        self.thank = QtWidgets.QMainWindow()
        self.ui = Ui_thank()
        self.ui.setupUi(self.thank)
        Form.hide()
        self.thank.show()

    def retranslateUi(self, FinalRegistration):
        _translate = QtCore.QCoreApplication.translate
        FinalRegistration.setWindowTitle(_translate("FinalRegistration", "MainWindow"))
        self.label.setText(_translate("FinalRegistration", "آیا میخواهید خرید خود را ثبت نهایی کنید؟"))
        self.pushButton.setText(_translate("FinalRegistration", "خیر"))
        self.pushButton_2.setText(_translate("FinalRegistration", "بله"))


class Ui_thank(object):
    def setupUi(self, thank):
        thank.setObjectName("thank")
        thank.resize(800, 600)
        thank.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(thank)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 180, 501, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        thank.setCentralWidget(self.centralwidget)

        self.retranslateUi(thank)
        QtCore.QMetaObject.connectSlotsByName(thank)

    def retranslateUi(self, thank):
        _translate = QtCore.QCoreApplication.translate
        thank.setWindowTitle(_translate("thank", "MainWindow"))
        self.label.setText(_translate("thank", "از خرید شما متشکریم "))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
