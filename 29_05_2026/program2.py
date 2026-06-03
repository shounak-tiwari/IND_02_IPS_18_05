# lambda function: it is anonymous , single line function, which is mainly use developing high order functions its is syntax is complete in a line and it return their output in a ref or ref object 


ips = (lambda x,y: x(y)+x(y**2))
print(ips(abs,-9))

# def result(x,y):
#     return x(y)+x(y**2)
# print(result(abs,-9))
