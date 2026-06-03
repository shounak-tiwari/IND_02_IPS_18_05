'''
It is buiilt in methods returns a proxy object that allows a child class to call methods and access the attributes from its parents class 
'''

class Base:
    def show(self):
        print("Hello im base class ")

class Child(Base):
    def show(self):
        print("Hello Im child class ")

chdobj = Child()

chdobj.show()