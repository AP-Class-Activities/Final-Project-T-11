import random 
from Seller_Class import Seller


class coustumer:
    coustumer = dict()
    store_inventory = dict()

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
        Costumer.costumers[self.costumer_id] = [name, last_name,address , phone_number, email]

         @staticmethod
    def list_stocks():
        for goods in Costumer.store_inventory.keys():
            yield str(goods) + " : " + str(Costumer.store_inventory[goods])

    def charge_credit(self, amount):
        self.credit = self.credit + amount

    def add_to_cart(self, item, seller_id, price):
        self.cart[item] = seller_id, price

    def add_to_favorites(self, item):
        self.favorites.append(item)

    def pay(self):
        total_fee = 0
        for order in self.cart.values():
            total_fee += order[1]
        if total_fee > self.credit:
            return "sorry, you have to increase your balance by: " + str(total_fee - self.credit) + "$"
        else:
            self.credit = self.credit - total_fee
            self.last_shopping.append(self.cart)
            self.cart = dict()
            return "thank you for your shopping."

    @staticmethod
    def rate(seller_id, rating):
        int(input("Please rate the seller from 1 to 5:"))
        Seller.sellers_rates[seller_id].append(rating)

          

        
