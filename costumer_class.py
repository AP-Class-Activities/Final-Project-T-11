import datetime
import random
products = dict()
sellers = dict()
costumers = dict()
store_cash_desk = dict()
gift_cards = dict()


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

    def __init__(self, name, last_name, address, phone_number, email=None,sex,password):
        self.__name = name  # assigning costumer's name
        self.__last_name = last_name  # assigning costumer's last_name
        self.__address = address # assigning customer's address
        self.__phone_number = phone_number  # assigning costumer's phone number
        self.__email = email  # assigning costumer's email
        self.__sex = sex
        self.__password = password
        if sex not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = sex
        # setter and getter
        @property
        def name(self): 
            return self.__name

        @name.setter
        def name(self,value): 
            self.__name = value
        @property
        def last_name(self): 
            return self.__last_name

        @last_name.setter
        def last_name(self,value): 
            self.__last_name = value
        @property
        def address(self): 
            return self.__address

        @adress.setter
        def address(self,value): 
            self.__address = value
        @property
        def phone_number(self): 
            return self.__phone

        @phone.setter
        def phone_number(self,value): 
            self.__phone_number = value
        @property
        def email(self): 
            return self.__email

        @email.setter
        def email(self,value): 
            self.__email = value
        @property
        def sex(self): 
            return self.__sex
        @sex.setter
        def sex(self,value): 
            if value not in ['male', 'female']: 
               raise ValueError('the value of sex should be [male or female] ')
            self.__sex = value
        @property
        def password(self): 
            self.__password

        @password.setter
        def password(self,value): 
            self.__password = value
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
        costumers[self.costumer_id] = [name, last_name, address, phone_number, email,sex,password, self.credit, self.cart,
                                       self.favorites, self.last_shopping]

    # static method to list all products in the store for the costumer
    @staticmethod
    def list_stocks():
        for goods in products.keys():  # iterating and showing all of the products
            yield str(goods) + " : " + str(products[goods])

    # method to charge balance of the costumer
    def charge_credit(self, amount):
        self.credit = self.credit + amount  # increasing costumer credit by the amount which he/she deposited.

    def add_to_cart(self, item, seller_id, price):
        self.cart[item] = seller_id, price

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
        # according to the Seller class _init_ method is stored in it's 7th position so the index is 7.
        sellers[seller_id][7][self.costumer_id] = costumer_rate  # adding costumer rate to the seller's rating records.

    # method to write a comment for a product
    def comment(self, product_name):
        costumer_comment = input("Please write your comment about the " + product_name)
        # according to the Product class _init_ method is stored in it's 3th position so the index is 3.
        # adding costumer comment to the product's comments records.
<<<<<<< Updated upstream
        products[product_name][3][self.costumer_id] = costumer_comment
=======
        products[product_name][3][self.costumer_id] = costumer_comment
        def __str__(self): 
        return 'name: {}   last_name: {} {}    address: {}   phone_number: {}   email: {}   sex: {}    password: {}'\
            .format(self.name,self.last_name, self.address, self.phone_number, self.email, self.sex, self.password)
>>>>>>> Stashed changes
