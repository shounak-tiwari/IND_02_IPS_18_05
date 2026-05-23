lst = [100,101,102,103,104,105]
try:
    for x in lst[5]:
        print(x)
except IndexError as e:
    print(e)
except:
    print("Some errors in for loops program")