# abstraction: abstraction is also major piller of oops , it refers to hide the implemenration and show neccessary details only 
# create a class with area method take args l and b return the area of ra
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def area(self,l,b):
        return l*b

class IPS(Area):
    def area(self, l, b):
        return super().area(l, b)

A= IPS()
print(A.area(10,20))
# A.intro()