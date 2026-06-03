'''
Encapsulation : is one of the major piller of oops , it wrape the data in a single unit.
'''
class Student:
    def setDetails(self,name):
        self.__name = name
    def getDetails(self):
        return self.__name
obj = Student()
obj.setDetails("IPS")
print(obj.getDetails())