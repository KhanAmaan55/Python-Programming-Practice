"""
Operators In Pythons
1.Arithmetic Operators
2.Assignment Operators
3.Comparison Operators
4.Logical Operators
5.Identity Operators
6.Membership Operators
7.Bitwise Operators
"""

# # Arithmetic Operators
print("## Arithemetic Operators ##")
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 ** 3 is ", 5**3) ##exponential
print("5 % 5 is ", 5%5)   ##reminder
print("15 // 6 is ", 15//6)  ##integer value after division

# # Assignment Operators
print("## Assignment Operators ##")
x = 5
print(x)
x %=7     ##x = x%7
print(x)

# #Comparison Operators
print("## Comparison Operators ##")
i = 5
print(i>10)
print(i<10)


# #Logical Operators
print("## Logical Operators ##")
a = True
b = False
print(a and b)

# #Identity Operators
print("## Identity Operators ##")
print(5 is 5)

# #Membership Operators
print("## Membership Operators ##")
list = [3, 3,2, 2,39, 33, 35,32]
print(324 not in list)

# #Bitwise Operators
# 0 - 00
#1 - 01
#2 - 10
#3 - 11
print("## Bitwise Operators ##")
print(0 & 2)
print(0 | 3)