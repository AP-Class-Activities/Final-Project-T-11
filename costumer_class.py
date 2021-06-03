import random 

class coustumer:
    coustumer = dict()
    store_inventory = dict()

    def __init__(self, name, last_name, address ,phone_number=None, email=None):
        self.name = name 
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number 
        self.email = email 
        random_id = random.randint(100000,1000000)
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
        Costumer.costumers[self.costumer_id] = [name, last_name, phone_number, email]
          

        
