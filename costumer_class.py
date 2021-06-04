import random 
from Seller_Class import Seller


class coustumer:
    coustumer = dict()
    store_inventory = dict()

    def __init__(self, name, last_name, address ,phone_number=None, email=None):
        self.name = name  # assigning costumer's name
        self.last_name = last_name # assigning costumer's last_name
        self.address = address # assigning costumer's address
        self.phone_number = phone_number  # assigning costumer's phone number
        self.email = email  # assigning costumer's email
        random_id = random.randint(100000,1000000)# generating random 6 digit id number
        flag = True
        while flag is True:
          if random_id not in Costumer.costumers.keys():
             self.costumer_id = "CU" + str(random_id)
             flag = False
            else:
                random_id = random.randint(100000, 1000000)
                flag = True
        self.credit = 0
        self.cart = dict()
        self.favorites = list()
        self.last_shopping = list()
        Costumer.costumers[self.costumer_id] = [name, last_name, address,phone_number, email]
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

          

        
