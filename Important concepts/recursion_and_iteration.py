def factorial_iterative(n):
    """
    calculating factorial using iteration
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    """
    calculating factorial using recursion
    """
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


number = int(input("Enter then number : "))
print("Factorial of",number, "Using Iterative Method", factorial_iterative(number))
print("Factorial of",number, "Using Recursive Method", factorial_recursive(number))
print("The fibonacci series",number,"position element is",fibonacci(number))
  
