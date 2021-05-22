from PyQt5 import QtCore, QtGui, QtWidgets

class person():
    def __init__(self, FirstName, LastName, gender, address, phonnumber, email)
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Address = Address
        self.__Phonnumber = Phonnumber
        self.__Email = Email

        if gender not in ['male', 'female']: 
            raise Error('the value of gender should be [male or female] ')
        self.__gender = gender

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