class MyClass:
    def __init__(self):
        self.__myAge = 0 
    
    # setter method 
    def setMyAge(self,value):
        self.__myAge = value
    
    # Getter method 
    def getMyAge(self):
        return self.__myAge


obj = MyClass()
obj.setMyAge(100)
print(obj.getMyAge())