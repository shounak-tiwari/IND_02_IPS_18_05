'''
Polymorphisms : polymorphisms is laten greek word where as poly means many and morphisms means forms  
it is divide into two types 
a. compile time  : 
    i. function overloading  : multiple function in class with same name.. 
    with different parameters function overloading ... 
    ii. operators overloading 

b. run time : methods orderriding 
'''
class A:
    def intro(self):
        print("Hello A")

class B(A):
    def intro(self):
        print("Hello B")

objB = B()

objB.intro()
