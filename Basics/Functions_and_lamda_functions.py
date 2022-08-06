# print(sum((2,3))) #Builtin Functions
def average1(a, b):
    """
This function is used to find average of two numbers
    """
    average = (a+b)/2
    return average


print(average1.__doc__)
a = 10
b = 20
average = average1(a, b)
print(average)

# a=int(input("Enter a number : "))
# half=lambda x:x/2       # # mini functions 
# print(half(a))