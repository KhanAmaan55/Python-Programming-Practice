class A:
    classvar1="This is class A var"
    def __init__(self):
        self.var1="This is variable of class A"
        self.special="Class A special Variable"
        self.classvar1="This is class A var"

class B(A):
    classvar2= "This is class B var"
    def __init__(self):
        super().__init__()
        self.var1="This is variable of class B"
    

a=A()
b=B()

print(a.classvar1)
print(b.var1)
print(b.special)