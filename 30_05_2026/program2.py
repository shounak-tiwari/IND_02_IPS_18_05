# creating a class 
class Student:
    def inputDetails(self):
        self.studName = input("Enter the name of student : ")
        self.studAge = int(input("Enter the age of student  : "))
        self.studEmail = str(input("Enter the email of student : "))
    def outputDetails(self):
        print("Name of student : ",self.studName)
        print("Age of student : ",self.studAge)
        print("Contact of student : ",self.studEmail)
        
Stud1 = Student()
Stud1.inputDetails()
Stud1.outputDetails()