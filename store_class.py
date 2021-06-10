import random
sellers_id = dict()
sellers = dict()
products = dict()
costumers = dict()

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

class Product:

    def __init__(self, product, quantity, product_id, sellers_id, price,color):

        # to check if store approves this product to be listed on it's catalogue or not
        if Store.approve_product([product, quantity, product_id, sellers_id, price,color]) is True:

            # to check if a product is not available in the store by another seller
            if product not in products.keys():
                assert len(str(product_id)) == 6  # check if the length of the product id is exactly 6 or not
                self.product = product  # assigning product name
                self.product_id = "PR" + str(product_id)  # assigning product id
                self.sellers_id = [sellers_id]  # assigning seller id
                self.price = price  # assigning it's price
                self.color = color # assigning color
                self.comments = dict()  # empty dictionary of comments to be filled by costumers opinions
                self.quantity = quantity  # assigning product quantity
                # adding new product to the dictionary of all products to be inserted to database later in below format:
                products[self.product] = [self.product_id, self.sellers_id, self.price, self.comments, quantity,color]

            # if it is available then:
            else:
                products[product][1].append(sellers_id)  # append the new seller to the existing list of sellers
                products[product][-1] += quantity  # increase the quantity by the amount which new seller wish to add

        # if store does not permit the new product:
        else:
            raise PermissionError

        if color not in ['blue', 'black', 'red', 'yellow', 'white']:
            raise Error('the value of color should be [blue, black, red, yellow and white] ')
        self.color = color # Available colors for a product###
        
        #def get_price(self, number_to_be_bought):
           # if number_to_be_bought > quantity:
                #return Error("Your purchase is more than the number available!")
           # else:
               # return price * number_to_be_bought###
        

