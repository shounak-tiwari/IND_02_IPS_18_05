'''
bitwise operators : 
a. AND :
b. OR :
c. XOR : 
d. Rshift 
e. Lshift 
f. Compliment 

'''
#  Smallest of three integers without comparison operators 

a =1
b =2

print(bin(((a^b)&((a-b)>>31))))

# print((b^((a^b)&((a-b)>>31))))