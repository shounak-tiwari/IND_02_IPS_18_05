set_1 = {"Rakshita","Sidharth","Nehul","Aditya","Pratham"}
set_2 = {"Ankit","Harsh","Aditya","Pratham"}

# remove element from set 1 who present in set 2 
set_1.difference_update(set_2)
print(set_1)