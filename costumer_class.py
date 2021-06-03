import random 
from seller_class import seller 

class coustumer:
    coustumer = dict()
    store_inventory = dict()

    def __init__(self, name, last_name, address ,phone_number=None, email=None):
        self.name = name 
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number 
        self.email = email 
        
