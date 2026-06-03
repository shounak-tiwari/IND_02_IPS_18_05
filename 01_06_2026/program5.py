# multiple 
class A:
    def __init__(self):
        print("a")
class B:
    def __init__(self):
        print("b")
class C (A,B):
    def __init__(self):
        print("c")
        A.__init__(self)
        B.__init__(self)
obj = C()