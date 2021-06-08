import random

class products:
    def __init__(self, name, color, price, quantity):
        self.name = name #name of products
        self.price = price
        self.quantity = quantity

        random_id = random.randint(100000, 1000000)  # generating random 6 digit id number
        '''hence the generated id is random, it is possible that they may coincide, so to avoid such si
        this while loop to check for existing duplicates'''
        flag = True  # a flag to keep while loop going until we have a unique product id
        while flag is True:  # assigning a unique product id to the new product
            if random_id not in products.keys():  # checking existing products to find duplicate products id
                self.products_id = "PR" + str(random_id)  # no duplicates were found, so we assign cost
                flag = False  # now that the id is successfully assigned, we change the flag to stop while loop
            else:  # duplicate id were found
                random_id = random.randint(100000, 1000000)  # generating a new random costumer id
        
        if color not in ['blue', 'black', 'red', 'yellow', 'white']:
            raise Error('the value of color should be [blue, black, red, yellow and white] ')
        self.color = color # Available colors for a product
        
        def get_price(self, number_to_be_bought):
            if number_to_be_bought > quantity:
                return Error("Your purchase is more than the number available!")
            else:
                return price * number_to_be_bought
        


class Store:
    net_profit = 0  # variable to store the net profit of the store until this moment

    def __init__(self, address, website_url, telephone_number):
        self.address = address
        self.website_url = website_url
        self.telephone_number = telephone_number

