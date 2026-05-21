'''
control statement : statement controls the flow of execution of program based on some conditions
1. if
2. if else
3. if elif else
4. nested if 
5. nested if else 
6. match (3.9+ )version
7. loops 
'''
# Enter a name and check name is valid or not, it is valid when len <=8 and gre from 2 , make sure the name's first latter is capital 
import re

# dob email full name last name first name passwords 
namere = "^[A-Z][a-z]+\s+[A-Z][a-z]{2,8}$"
name = input("Enter the name of candidate  : ")

if re.match(namere,name):
    print("it is valid")
else:
    print("it is invalid")