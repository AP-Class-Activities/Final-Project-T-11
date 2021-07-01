from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import random
sellers = dict()
suspended_sellers = list()
products = dict()
costumers = dict()
store_cash_desk = dict()
gift_cards = dict()

#To choose you are seller or customer
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


# Question about whether you have an account or you need to register first
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 50, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 361, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("photo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 290, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 370, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 370, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.checkBox_2.setObjectName("checkBox_2")
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
        self.label_3.setText(_translate("MainWindow", "آیا قبلا عضو شدید؟"))
        self.checkBox.setText(_translate("MainWindow", "بله"))
        self.checkBox_2.setText(_translate("MainWindow", "خیر"))


def is_gift_card_valid(code, costumer_id, product):
    date_check = False
    if datetime.date.today() < gift_cards[code][0]:
        date_check = True
    costumer_check = False
    product_check = False
    for detail in gift_cards.values():
        if costumer_id in detail[1].keys():
            costumer_check = True
        if product in detail[2]:
            product_check = True
    return date_check and costumer_check and product_check


class Costumer:

    def __init__(self, name, last_name, address, phone_number, email=None):
        self.name = name  # assigning costumer's name
        self.last_name = last_name  # assigning costumer's last_name
        self.address = address #assigning coustumer's address
        self.phone_number = phone_number  #assigning costumer's phone number
        self.email = email  # assigning costumer's email
        random_id = random.randint(100000, 1000000)  # generating random 6 digit id number
        '''hence the generated id is random, it is possible that they may coincide, so to avoid such situations we use
         this while loop to check for existing duplicates'''
        flag = True  # a flag to keep while loop going until we have a unique costumer id
        while flag is True:  # assigning a unique costumer id to the new seller
            if random_id not in costumers.keys():  # checking existing costumers to find duplicate costumer id
                self.costumer_id = "CU" + str(random_id)  # no duplicates were found, so we assign costumer id
                flag = False  # now that the id is successfully assigned, we change the flag to stop while loop
            else:  # duplicate id were found
                random_id = random.randint(100000, 1000000)  # generating a new random costumer id
        self.credit = 0  # initial costumer's balance
        self.cart = dict()  # costumer's cart(shopping basket)
        self.favorites = list()  # costumer's favorites lists
        self.last_shopping = list()  # costumer's historical shopping details
        # adding the new costumer to the dictionary so that we can add them to database later
        costumers[self.costumer_id] = [name, last_name, address, phone_number, email, self.credit, self.cart,
                                       self.favorites, self.last_shopping]

    # static method to list all products in the store for the costumer
    @staticmethod
    def list_stocks():
        for goods in products.keys():  # iterating and showing all of the products
            yield str(goods) + " : " + str(products[goods])

    # method to charge balance of the costumer
    def charge_credit(self, amount):
        self.credit = self.credit + amount  # increasing costumer credit by the amount which he/she deposited.

    # method to add item to the costumer's cart(shopping basket) from an specific seller
    def add_to_cart(self, item, seller_id, price, quantity):
        try:  # check if store approves this order or not
            if Store.approve_order(item, seller_id, self.costumer_id, price, quantity) is True:
                self.cart[item] = seller_id, price, quantity  # order was approved so we add it to cart(shopping basket)
        except PermissionError:  # order was not approved.
            print("order was declined by the system administrator!")

    # method to add an item to costumer's favorites list
    def add_to_favorites(self, item):
        self.favorites.append(item)

    # method to remove an item from costumer's favorites list
    def remove_favorites(self, item):
        self.favorites.remove(item)

    # method to pay for the items that costumer is willing to buy
    def pay(self, gift_code=None):
        total_fee = 0  # a variable to store the amount of money that costumer should pay for it's shopping
        # adding products prices to the invoice
        for order in self.cart.values():  # iterating over costumer's cart(shopping basket)
            total_fee += order[1]  # adding prices
        if gift_code is not None:  # check if a gift code is entered or not
            for product in self.cart.keys():  # iterating over purchased items
                gift_card_validity = is_gift_card_valid(gift_code, self.costumer_id, product)  # validity of gift card
                if gift_card_validity is True:  # gift card is valid
                    # decrease the costumer fee relative to the gift card off percentage and product price
                    total_fee -= self.cart[product][1] * gift_cards[gift_code][3]
        if total_fee > self.credit:  # checking if costumer have enough money to pay for his card(shopping basket)
            return "sorry, you have to increase your balance by: " + str(total_fee - self.credit) + "$"
        else:  # it has enough money so:
            self.credit = self.credit - total_fee  # reducing the costumer's shopping fees from it's credit
            self.last_shopping.append(self.cart)  # adding user cart(shopping basket) to it's historical shopping data
            for product, details in self.cart:  # adding each seller sales to the history of store transactions
                if details[0] not in store_cash_desk.keys():  # check if a seller is present in the dictionary or not
                    '''according to add_to_cart method the first item in value is seller id the second is price and the 
                    third is it's quantity. so in order to construct the ledger in form of {seller: credit_to_pay}
                    we have to set the seller id as the key and the price of the product multiplied by it's quantity 
                    that the costumer wants to buy as the value.'''
                    store_cash_desk[details[0]] = details[1] * details[2]
                else:  # seller does exist in the transactions history
                    # so we only have to increase it's credit by the amount that the costumer is buying
                    store_cash_desk[details[0]] += details[1] * details[2]
            # reducing the quantity of the product by the amount which costumer have bought
            for product in self.cart.keys():  # iterating over items that costumers have bought
                products[product][-1] -= self.cart[product][-1]  # reducing the quantity of product in inventory
            self.cart = dict()  # resetting costumer cart to be empty for next shopping
            return "thank you for your shopping."

    # method to rate a seller
    def rate(self, seller_id):
        costumer_rate = int(input("Please rate the seller from -5 to 5:"))  # taking the seller's rate from costumer
        # according to the Seller class __init__ method is stored in it's 7th position so the index is 7.
        sellers[seller_id][7][self.costumer_id] = costumer_rate  # adding costumer rate to the seller's rating records.

    # method to write a comment for a product
    def comment(self, product_name):
        costumer_comment = input("Please write your comment about the " + product_name)
        # according to the Product class __init__ method is stored in it's 3th position so the index is 3.
        # adding costumer comment to the product's comments records.
        products[product_name][3][self.costumer_id] = costumer_comment

# If you have already been a member, enter this page and enter your username and password
f = open('database.txt', 'r+')
username = input()
password = input()
s = f.readlines()
s = [j for i in s for j in i.split()]
emkanSabtnam = True
for k in range(0, len(s), 2):
    if username == s[k]:
        emkanSabtnam = False
        print('in name karbari tekrari ast!')
        break
f.close()
if emkanSabtnam:
    f = open('database.txt', 'a+')
    f.write(f'{username} {password}\n')
    print('sabtname ba mofaghiat anjam shod!')
    f.close()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 351, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images.jpg"))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 440, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(506, 300, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.label_4.setText(_translate("MainWindow", " رمز ورود مشتری"))
        self.pushButton.setText(_translate("MainWindow", "تایید"))
        self.pushButton_2.setText(_translate("MainWindow", "انصراف"))
        self.label_2.setText(_translate("MainWindow", "نام کاربری"))


# If the customer is not a member before, first enter this page and become a member
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 255, 127);\n"
"background-color: rgb(170, 170, 255);")
        MainWindow = QtWidgets.QMainWindow(mainwindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.lineEdit.setGeometry(QtCore.QRect(60, 150, 421, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 110, 421, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 190, 421, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 230, 421, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 270, 431, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 310, 431, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 470, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 470, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 350, 431, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "صفحه مشتری"))
        self.label_2.setText(_translate("MainWindow", "نام"))
        self.label_3.setText(_translate("MainWindow", "نام خانوادگی"))
        self.label_4.setText(_translate("MainWindow", "آدرس"))
        self.label_5.setText(_translate("MainWindow", "شماره تلفن"))
        self.label_6.setText(_translate("MainWindow", "ایمیل"))
        self.label_7.setText(_translate("MainWindow", "جنسیت"))
        self.label_8.setText(_translate("MainWindow", "رمز ورود"))
        self.pushButton.setText(_translate("MainWindow", "تایید"))
        self.pushButton_2.setText(_translate("MainWindow", "انصراف"))


class Seller:

    def __init__(self, name, last_name, distance_to_inventory, address, phone_number, email):

        # check if store approves this new seller or not
        try:
            # calling the store system admin to accept or reject this seller request
            if Store.approve_seller([name, last_name, distance_to_inventory, address, phone_number, email]) is True:
                self.name = name  # assigning it's first name
                self.last_name = last_name   # assigning it's last name
                self.phone_number = phone_number  # assigning it's phone number
                self.email = email  # assigning it's email address
                self.rates = dict()  # assigning empty dictionary of rates to be filled by costumers opinions
                random_id = random.randint(100000, 1000000)  # generating random 6 digit id number
                '''hence the generated id is random, it is possible that they may coincide, so to avoid such situations
                we use this while loop to check for existing duplicates'''
                flag = True  # a flag to keep while loop going until we have a unique seller id
                while flag is True:  # assigning a unique seller id to the new seller
                    if random_id not in sellers.keys():  # checking existing sellers to find duplicate seller id
                        self.seller_id = "SL" + str(random_id)  # no duplicates were found, so we assign seller id
                        flag = False  # now that the id is successfully assigned, we change the flag to stop while loop
                    else:  # duplicate id were found
                        random_id = random.randint(100000, 1000000)  # generating a new random seller id
                self.balance = 0  # seller initial account balance
                self.distance_to_inventory = distance_to_inventory  # time distance to store  from seller location
                self.sales = dict()  # all seller sales by date, the format of the dictionary is = {date: sale details}
                self.suspension = False  # the suspension status
                self.list_of_orders = []  # assigning empty list of orders to the newly added seller
                self.products = []  # empty product list to be filled by costumers, entries are tuples: (quantity, type)
                self.address = address  # assigning it's address
                self.profit = 0
                self.cost = 0
                self.income = 0
                self.total_sales_counts = 0
                # adding the new seller to the dictionary so that we can add them to database later
                sellers[self.seller_id] = [self.name, self.last_name, self.address, self.list_of_orders, self.balance,
                                           self.phone_number, self.email, self.rates, self.sales, self.suspension,
                                           self.distance_to_inventory, self.products, self.profit, self.income,
                                           self.cost]
        # if gets rejected
        except PermissionError:
            print("This seller was not approved by the system admin.")

    # method to generate sales records by time
    def historical_sales(self, item, quantity, date, costumer_id, buying_price, selling_price, cost):
        profits = (selling_price - buying_price) * quantity
        incomes = selling_price * quantity
        self.profit = profits  # updating profits amount
        self.income = incomes  # updating incomes amount
        self.cost += cost  # accumulating costs
        # records will be saved in a dictionary by below format:
        self.sales[date] = [item, quantity, costumer_id, buying_price, selling_price, profits, self.cost, incomes]

    # method to generate historical sale data in an arbitrary timeframe
    def statistics(self, time_frame):  # have in mind that time_frame should either be an integer or "all"
        results = []
        for date in self.sales.keys():
            if time_frame.isdigit() is True:  # check if time_frame is a number or the whole time is wanted
                # now we filter the sales which happened between today and time_frame days ago
                if date >= datetime.date.today() - datetime.timedelta(int(time_frame)):
                    results.append(self.sales[date])  # appending filtered sales
            else:  # time_frame was "all" so we enter every sale record
                results.append(self.sales[date])  # appending every sale record
        time_frame_profits = 0
        time_frame_costs = 0
        time_frame_incomes = 0
        time_frame_sales_count = len(results)
        for i in results:
            time_frame_profits += i[5]  # updating profits amount
            time_frame_costs += i[6]  # updating costs amount
            time_frame_incomes += i[7]  # updating incomes amount
        return [time_frame_profits, time_frame_incomes, time_frame_costs, time_frame_sales_count]

    # method to suspend a seller if it's negative feedbacks exceeds a certain amount, limit can be changed arbitrarily
    def suspend(self, limit):
        # filtering negative feedbacks from the seller's rating list
        count_of_negative_feedbacks = len(list(filter(lambda i: i < 0, sellers[self.seller_id][7])))
        if count_of_negative_feedbacks > limit:  # if negative feedbacks pass over a certain amount we suspend seller
            self.suspension = True  # seller suspended
            suspended_sellers.append(self.seller_id)

    # method to list the ongoing costumers orders for the seller
    def list_of_orders(self, costumer_order):
        self.list_of_orders.append(costumer_order)

    # method to allow seller to withdraw an arbitrary amount of money from it's credit from the store
    def withdraw(self, amount, net_withdrawal_rate):
        assert 0 < net_withdrawal_rate < 1
        if store_cash_desk[self.seller_id] > amount:  # check if seller have enough credit in store cash desk.
            '''net withdrawal rate is the net deposited percentage of sales which seller can withdraw and the extra
            money is paid to the store as commission. it should be a floating number between 0 and 1. for example a 0.7
            net withdrawal rates means that the seller takes 70 percent of the whole sale and pay 30 percent of it to 
            store as commission.'''
            self.balance = self.balance + amount * net_withdrawal_rate  # withdrawing credit & adding it to it's balance
            Store.net_profit += (1 - net_withdrawal_rate) * amount  # paying the commission to the store
            store_cash_desk[self.seller_id] -= amount  # decreasing the seller's credit by the withdrawing amount
        else:  # seller does not have enough credit in store cash desk
            print("you don't have enough credit!")

    # method to add a product which is an object of Product class
    def seller_products(self, product_name, product_quantity, product_price):

        # check if it gets approved by admin or not
        try:
            # generate a product object from the Product class
            product_id = random.randint(100000, 1000000)  # generating random 6 digit product id
            '''hence the generated id is random, it is possible that they may coincide, so to avoid such situations we
             use this while loop to check for existing duplicates'''
            flag = True  # a flag to keep while loop going until we have a unique product id
            while flag is True:
                for item, details in products.items():  # iterating over all products to find duplicate product id
                    if details[0] == product_id:  # check if product id is not unique
                        product_id = random.randint(100000, 1000000)  # generating a new random product id
                # we have successfully iterated whole products and we have make sure that the product id is unique
                # now that the product id is unique we generate the new product object from Products class
                new_product = Product(product_name, product_quantity, product_id, self.seller_id, product_price)
                self.products.append(new_product)  # append new product to seller products list
                flag = False  # now that the product is added successfully we change the flag to stop while loop

        # if gets rejected:
        except PermissionError:
            print("This product was denied by admin")


# If you have already been a member, enter this page and enter your username and password
f = open('database.txt', 'r+')
username = input()
password = input()
s = f.readlines()
s = [j for i in s for j in i.split()]
emkanSabtnam = True
for k in range(0, len(s), 2):
    if username == s[k]:
        emkanSabtnam = False
        print('in name karbari tekrari ast!')
        break
f.close()
if emkanSabtnam:
    f = open('database.txt', 'a+')
    f.write(f'{username} {password}\n')
    print('sabtname ba mofaghiat anjam shod!')
    f.close()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 351, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images.jpg"))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 440, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(506, 300, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.label_4.setText(_translate("MainWindow", "رمز ورود فروشنده"))
        self.pushButton.setText(_translate("MainWindow", "تایید"))
        self.pushButton_2.setText(_translate("MainWindow", "انصراف"))
        self.label_2.setText(_translate("MainWindow", "نام کاربری"))


# If the seller doesn't have an account, log in to this page and become a member
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


class Store:
    net_profit = 0  # variable to store the net profit of the store until this moment

    def __init__(self, address, website_url, telephone_number):
        self.address = address
        self.website_url = website_url
        self.telephone_number = telephone_number

    # method to approve a seller registration request
    @staticmethod
    def approve_seller(name, last_name, distance_to_inventory, address, phone_number, email):
        approval = input("Do you approve a seller with following details: type yes or no \n"
                         "name: {}, last name: {}, distance to inventory: {}, address: {}, phone number: {},"
                         " email: {}".format(name, last_name, distance_to_inventory, address, phone_number, email))
        if approval.lower() == "yes":
            return True
        else:
            raise PermissionError

    # method to approve a product listing request
    @staticmethod
    def approve_product(product, quantity, product_id, sellers_id, price):
        approval = input("Do you approve a product with following details: type yes or no \n"
                         "product name: {}, quantity: {}, product id: {}, seller id: {},"
                         " product price: {}".format(product, quantity, product_id, sellers_id, price))
        if approval.lower() == "yes":
            return True
        else:
            raise PermissionError

    # method to approve a costumer order request
    @staticmethod
    def approve_order(item, seller_id, costumer_id, price, quantity):
        approval = input("Do you approve an order with following details: type yes or no \n"
                         "item name: {}, quantity: {}, seller id: {}, costumer id: {}," 
                         "unit price: {}".format(item, quantity, seller_id, costumer_id, price))
        if approval.lower() == "yes":
            return True
        else:
            raise PermissionError

    # method to remove a specific costumer
    @staticmethod
    def remove_costumer(costumer_id):
        del costumers[costumer_id]

    # method to remove a specific seller
    @staticmethod
    def remove_seller(seller_id):
        del sellers[seller_id]

    # method to see specific seller details
    @staticmethod
    def seller_details(seller_id):
        # below results is a list of form [name, last name, address, list of orders, balance, phone number,
        # email, rates, sales, suspension, distance to inventory, products] and the indices are
        # corresponding to each of these item
        seller_details = sellers[seller_id]
        print("current status and details of the seller is: \n",
              "name: {}\n".format(seller_details[0]),
              "last name: {}\n".format([seller_details[1]]),
              "address: {}\n".format(seller_details[2]),
              "phone: {}\n".format(seller_details[5]),
              "email: {}\n".format(seller_details[6]),
              "suspension status: {}\n".format(seller_details[9]),
              "balance: {}\n".format(seller_details[4]),
              "with-held credit: {}\n".format(store_cash_desk[seller_id]),
              "average rate: {} and detailed ratings is: {}\n".format(sum(seller_details[7])/len(seller_details[7]),
                                                                      seller_details[7]),
              "sales: {}\n".format(str(seller_details[8])),
              "list of orders: {}\n".format(seller_details[3]),
              "profit: {}\n".format(seller_details[12]),
              "incomes: {}\n".format(seller_details[13]),
              "costs: {}\n".format(seller_details[14]),
              "products: {}\n".format(seller_details[11]),
              "distance: {}\n".format(seller_details[10]))

    # method to list specific costumer details
    @staticmethod
    def costumer_details(costumer_id):
        # below results is a list of form [name, last name, address, phone_number, email, credit, cart, favorites,
        # last_shopping] and the indices are corresponding to each of these item.
        costumer_details = costumers[costumer_id]
        print("current status and details of the costumer is: \n",
              "name: {}\n".format(costumer_details[0]),
              "last name: {}\n".format([costumer_details[1]]),
              "address: {}\n".format(costumer_details[2]),
              "phone: {}\n".format(costumer_details[3]),
              "email: {}\n".format(costumer_details[4]),
              "balance: {}\n".format(costumer_details[5]),
              "current cart(shopping basket): {}\n".format(costumer_details[6]),
              "favorites: {}\n".format(costumer_details[7]),
              "shopping history: {}\n".format(costumer_details[8]))

    # method to calculate approximate shipping time
    def shipping_time_calculator(self, costumer_id, seller_id):
        print("your address is: {}".format(self.address))
        print("the costumer address is: {}".format(costumers[costumer_id][2]))
        distance_to_costumer = int(input("estimate the approximate time from inventory to costumer in minutes: "))
        distance_to_seller = sellers[seller_id][10]
        return "approximate shipping time is: " + str(distance_to_seller) + str(distance_to_costumer)

    # method to generate gift cards
    @staticmethod
    def gift_card_generator(code, year, month, day, specified_costumers_list, usage_count, specified_products, percent):
        expire_date = datetime.date(int(year), int(month), int(day))  # determining expiration date via date object
        specified_costumers = dict.fromkeys(specified_costumers_list, usage_count)  # determining allowed costumers
        # adding generated gift card to gift cards dictionary by below code:
        gift_cards[code] = [expire_date, specified_costumers, specified_products, percent]


#category: To choose in which product category you offer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(120, 130, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 130, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 310, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 310, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "میوه و سبزیجات"))
        self.pushButton_2.setText(_translate("MainWindow", "مواد غذایی"))
        self.pushButton_3.setText(_translate("MainWindow", "پوشاک"))
        self.pushButton_4.setText(_translate("MainWindow", "آرایشی و بهداشتی"))


#Food to be provided by the seller
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 689)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(700, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
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
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
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
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " مواد غذایی :"))
        self.label_2.setText(_translate("MainWindow", "قیمت "))
        self.label_3.setText(_translate("MainWindow", "نام محصول "))
        self.pushButton_6.setText(_translate("MainWindow", "بازگشت"))


#Fruits and vegetables to be provided by the seller
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 689)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(MainWindow)
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
        self.label_2 = QtWidgets.QLabel(MainWindow)
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
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
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
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " میوه و سبزیجات :"))
        self.label_2.setText(_translate("MainWindow", "قیمت "))
        self.label_3.setText(_translate("MainWindow", "نام محصول "))
        self.pushButton_6.setText(_translate("MainWindow", "بازگشت"))


#Cosmetics provided by the seller
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 689)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(MainWindow)
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
        self.label_2 = QtWidgets.QLabel(MainWindow)
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
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
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
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " آرایشی و بهداشتی :"))
        self.label_2.setText(_translate("MainWindow", "قیمت "))
        self.label_3.setText(_translate("MainWindow", "نام محصول "))
        self.pushButton_6.setText(_translate("MainWindow", "بازگشت"))


#Clothing provided by the seller
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 689)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 85, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(MainWindow)
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
        self.label_2 = QtWidgets.QLabel(MainWindow)
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
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(280, 120, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(280, 200, 591, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 290, 591, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 591, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 591, 71))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 560, 591, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
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
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 111, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(80, 300, 111, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 111, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(80, 480, 111, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(80, 570, 111, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " پوشاک :"))
        self.label_2.setText(_translate("MainWindow", "قیمت "))
        self.label_3.setText(_translate("MainWindow", "نام محصول "))
        self.pushButton_6.setText(_translate("MainWindow", "بازگشت"))


class Product:

    def __init__(self, product, quantity, product_id, sellers_id,color, price):

        # to check if store approves this product to be listed on it's catalogue or not
        if Store.approve_product([product, quantity, product_id, sellers_id, price]) is True:

            # to check if a product is not available in the store by another seller
            if product not in products.keys():
                assert len(str(product_id)) == 6  # check if the length of the product id is exactly 6 or not
                self.product = product  # assigning product name
                self.product_id = "PR" + str(product_id)  # assigning product id
                self.sellers_id = [sellers_id]  # assigning seller id
                self.price = price  # assigning it's price
                self.color = color # assigning it's color
                self.comments = dict()  # empty dictionary of comments to be filled by costumers opinions
                self.quantity = quantity  # assigning product quantity
                # adding new product to the dictionary of all products to be inserted to database later in below format:
                products[self.product] = [self.product_id, self.sellers_id, self.price, self.comments, quantity]

            # if it is available then:
            else:
                products[product][1].append(sellers_id)  # append the new seller to the existing list of sellers
                products[product][-1] += quantity  # increase the quantity by the amount which new seller wish to add

        # if store does not permit the new product:
        else:
            raise PermissionError

        if color not in ['blue', 'black', 'red', 'yellow', 'white']:
            raise ('the value of color should be [blue, black, red, yellow and white] ')
        self.color = color # Available colors for a product
        
        def get_price(self, number_to_be_bought):
           if number_to_be_bought > quantity:
                return ("Your purchase is more than the number available!")
           else:
                return price * number_to_be_bought

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
