# Access Modifiers in python 
# AM  are used to control the visibility and accessibility of attributes and methods with in a class
'''
1. public : by defailt , all attributes and methods in  a class are considered public 
2. Protected :  Attributes and methods for internal use within the class and ites subclasses
3. Private: attributes and methods that should not be accessed from outside the class  
'''
class Student:
    # public Attribute 
    name = "Akash"
    # protected attribute 
    _age = 20
    # private attributes 
    __marks = 90
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self._age)
        print("Marks : ",self.__marks)

stud1 = Student()
print(stud1.name)
print(stud1._age)
print(stud1._Student__marks)