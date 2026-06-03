
class AnimalProf:
    def __init__(self):
        self._grade = input("Enter the grade  : ")
        self._cgpa = input("Enter the cgpa")
        self._sgpa = input("Enter the sgpa")
    def output(self):
        print("the grade of animal : ",self._grade)
        print("the cgpa of animal : ",self._cgpa)
        print("the sgpa of animal : ",self._sgpa)
