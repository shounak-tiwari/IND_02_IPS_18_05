def decorator(x):
    def cubeX():
        print("Hello ips")
        x()
    return cubeX

@decorator
def greet():
    print("Hello Good afternoon")

greet()