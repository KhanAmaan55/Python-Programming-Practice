a=input("Enter first number : ")
b=input("Enter second number : ")
try:
    print(int(a)+int(b))
except Exception as ex:
    print(ex)
print("Thanks for joining")