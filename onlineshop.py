from PyQt5 import QtCore, QtGui, QtWidgets

class person():
    def __init__(self, FirstName, LastName, gender, address, phonnumber, email,password)
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Address = Address
        self.__Phonnumber = Phonnumber
        self.__Email = Email
        self.__password=password

    #setters and getters
    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self.__FirstName = fullname

    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, LastName):
        self.__LastName = LastName
    
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phonnumber(self):
        return self.__phonnumber

    @phonnumber.setter
    def phonnumber(self, phonnumber):
        self.__phonnumber = phonnumber

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def gender(self): 
    return self.__gender

    @gender.setter
    def gender(self,gender): 
    if gender not in ['male', 'female']: 
        raise Error('the value of gender should be [male or female] ')
    self.__gender = gender
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password
#import person
#class customer(person):
    #def __init__(self,Fullname,Password,confirmPassword,Phonenumber,email,Gender):
        #self.Fullname=Fullname
        #self.Password=Password
        #self.confirmPassword=confirmPassword
        #self.Phonnumber=Phonenumber
        #self.email=email
        #self.Gender=Gender

    #def fullname(self):
    #    return self.Fullname
    #def password(self):
    #    return self.Password
    #def confirm(self):
    #    return self.confirmPassword
    #def phonenumber(self):
    #    return self.Phonnumber
    #def email(self):
    #    return self.email
    #def gender(self):
    #    return self.Gender

class Item():
    def __init__(self, name, description, price, code):
        self.name = name
        self.description = description
        self.price = price
        self.code = code

    def name(self):
        return self.name

    def description(self):
        return self.description

    def price(self):
        return self.price

    def code(self):
        return self.code

import Item
class ShoppingBasket():
    def __init__(self):
        self.items = {} #A dictionary of all the items in the shopping basket: {item:quantity} 
        self.checkout = False
  
    # add an item to the shopping basket  
    def addItem(self,item,quantity=1):
        if quantity > 0: 
            #Check if the item is already in the shopping basket
            if item in self.items:
                self.items[item] += quantity
            else: 
                self.items[item] = quantity
        else:
            print("Invalid operation - Quantity must be a positive number!")

      
    # remove an item from the shopping basket (or reduce it's quantity)  
    def removeItem(self,item,quantity=0):
        if quantity<=0: 
            #Remove the item
            self.items.pop(item, None)
        else:
            if item in self.items:
                if quantity<self.items[item]:
                    #Reduce the required quantity for this item
                    self.items[item] -= quantity
                else:
                    #Remove the item
                    self.items.pop(item, None)
          
    # update the quantity of an item from the shopping basket  
    def updateItem(self,item,quantity):
        if quantity > 0: 
            self.items[item] = quantity
        else:
            self.removeItem(item)

  
    # view/list the content of the basket.
    def view(self):

  
    # calculate the total cost of the basket.
    def getTotalCost(self):
        totalCost = 0
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            totalCost += cost
        return totalCost

    
    # empty the content of the basket
    def reset(self):
        self.items = {}
    
    # return whether the basket is empty or not:
    def isEmpty(self):
        return len(self.items)==0