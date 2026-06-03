# creating a class
# 
def add():
    x = int(input("Enter the value of x "))
    return x
class Animals:
    # attributes & methods
    Name = add()

# create object of class
obj = Animals

obj.Name

print(obj.Name)