import datetime
import random 
products = dict()
coustumer = dict()
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

class coustumer:

    def __init__(self, name, last_name, address ,phone_number, email:
        self.name = name  # assigning costumer's name
        self.last_name = last_name # assigning costumer's last_name
        self.address = address # assigning costumer's address
        self.phone_number = phone_number  # assigning costumer's phone number
        self.email = email  # assigning costumer's email
        random_id = random.randint(100000,1000000)# generating random 6 digit id number
         '''hence the generated id is random, it is possible that they may coincide, so to avoid such situations we use
         this while loop to check for existing duplicates'''
        flag = True# a flag to keep while loop going until we have a unique costumer id
        while flag is True:# assigning a unique costumer id to the new seller
          if random_id not in Costumer.costumers.keys(): # checking existing costumers to find duplicate costumer id
             self.costumer_id = "CU" + str(random_id) # no duplicates were found, so we assign costumer id
             flag = False# now that the id is successfully assigned, we change the flag to stop while loop
            else: # duplicate id were found
                random_id = random.randint(100000, 1000000)# generating a new random costumer id
        self.credit = 0# initial costumer's balance
        self.cart = dict()# costumer's cart(shopping basket)
        self.favorites = list() # costumer's favorites lists
        self.last_shopping = list()  # costumer's historical shopping details
         # adding the new costumer to the dictionary so that we can add them to database later
        costumers[self.costumer_id] = [name, last_name, address, phone_number, email, self.credit, self.cart,
                                       self.favorites, self.last_shopping]

        # static method to list all products in the store for the costumer
         @staticmethod
    def list_stocks():
        for goods in products.keys(): #iterating and showing all of the products
            yield str(goods) + " : " + str(products[goods])

        # method to charge balance of the costumer
    def charge_credit(self, amount):
        self.credit = self.credit + amount #increasing costumer credit by the amount which he/she deposited

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

   


        
