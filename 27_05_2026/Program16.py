#decorators : it is change the functionality of function without change in its code 

def greet(x):
    def cube():
        print("Good Evening ")
        x()
    return cube

@greet
def intro():
    print("my name is ips")


intro()


