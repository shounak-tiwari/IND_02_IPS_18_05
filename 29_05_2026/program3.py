# # create user define / take list element in runtime input 
# x = []
# while True:
#     element = int(input("Enter the element  : "))
#     if element == -1:
#         break
#     else:
#         x.append(element)
# print(x)


def createList():
    lst = []
    while (n:= (lambda:int(input("Enter the value of x ")))()) !=-1:
        lst.append(n)
    return lst 

# even list 
def EvList(x):
    lst =  x()
    result = [] 
    for i in lst:
        if i%2==0:
            result.append(i)
    return result

print(EvList(createList))