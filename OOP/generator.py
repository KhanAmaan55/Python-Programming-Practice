"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - method 

"""
def gen(n):
    for i in range(n):
        yield i

# g= gen(4)
# print(g)

# generator for fibonacci series
def fib(n):
    n1=0
    n2=1
    nth=0
    for i in range(n):
        yield nth
        n1=n2
        n2=nth
        nth=n1+n2

f=fib(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())