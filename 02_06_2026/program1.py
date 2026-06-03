'''
1. Compile time Polymorphisms  : deciding the operations to run during the compilation of program 
a. method overloading : multiple methods with same name and different parameters in a class , and it is call by object based on parameters 


same methods name with different signature 
'''
# dispatch : to send someone  or something to a specific destination 
from multipledispatch import dispatch
class Calculator:
    @dispatch(int)
    def calc(self,a):
        return a
    @dispatch(int,int)
    def calc(self,a,b):
        return a+b
    @dispatch(int,float)
    def calc(self,a,b):
        return a-b
obj = Calculator()
print(obj.calc(10,25.25))
# python keeps only the last defination of calc()
# to call that methods when one interger are passed 