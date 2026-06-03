# inheritance : inheritance is major piller of oops , which refers access the public/protected properites of parent/base in child/derived classes ,  class which is not interit from any one thats known as base and class which is interited called child class mainly inheritance is divide into 5 types 
'''
a. Single level inheritance 
b. Multi level inheritance 
c. 
d.
e. 
'''
from program3 import * 
from program4 import * 

class Animal(AnimalsPersonal):
    def __init__(self):
        super().__init__()
    def output(self):
        return super().output()
    
obj = Animal()
obj.output()