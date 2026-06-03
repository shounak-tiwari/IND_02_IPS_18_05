def nSum(*x):
    add = 0
    print(type(x))
    for i in x:
        add = add + i
    return add


print(nSum(10,20,30,40,50))