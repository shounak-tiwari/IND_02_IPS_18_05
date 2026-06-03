class Student:
    def __init__(self,a,b):
        self.x,self.y=a,b
    def GetValues(self):
        print(self.x)
        print(self.y)
stud1 = Student(10,20)
stud1.GetValues()
