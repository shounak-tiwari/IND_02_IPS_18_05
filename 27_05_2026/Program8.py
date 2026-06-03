# dict : dictionary is an ordered, changeable and does not allow duplicates keys , it store the items inside the curly brackets its items is present in form of {key:value}  and seprated by commas
# creating  a dictionary 
dic = {
    "Name":"Akash",
    "Address":"Satna",
    "email":"akashtiwari1014@gmail.com",
}

dic.setdefault("k","x")
print(dic)
# print(dic.get("Address"))
# print(dic.pop("Address"))
# print(dic.popitem())

# dic = dict.fromkeys(['Name','Address','Email'],"Not Defined")
# print(dic)