import copy

class Student:
    def __init__(self,a,b):
        self.x,self.y=a,b
    
    def __copy__(self):
        return Student(self.x,self.y)
                
stud1 = Student(10,20)

stud2 = copy.copy(stud1)

print(stud1.x,stud1.y)
print(stud2.x,stud2.y)