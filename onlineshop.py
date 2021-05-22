from PyQt5 import QtCore, QtGui, QtWidgets



#class loginpage(object):



class customer():

    def __init__(self,Fullname,Password,confirmPassword,Phonenumber,email,Gender):
        self.Fullname=Fullname
        self.Password=Password
        self.confirmPassword=confirmPassword
        self.Phonnumber=Phonenumber
        self.email=email
        self.Gender=Gender

    def fullname(self):
        return self.Fullname
    def password(self):
        return self.Password
    def confirm(self):
        return self.confirmPassword
    def phonenumber(self):
        return self.Phonnumber
    def email(self):
        return self.email
    def gender(self):
        return self.Gender





#class mainpage(object):



#class CustomerRegistration(object):