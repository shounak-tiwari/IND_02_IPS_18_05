# class : it is blue print 
class Stud:
    def inputStud(self):
        self.name = input("Enter the name of students ")
    def outputStud(self):
        print("The name of student : ",self.name)


#object : real entity / instance of the class 
Obj_1 = Stud()
Obj_2 = Stud()


Obj_1.inputStud()
Obj_2.inputStud()

Obj_1 = Obj_2

Obj_1.outputStud()
Obj_2.outputStud()