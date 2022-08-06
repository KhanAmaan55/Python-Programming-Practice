l = 10 # Global

def function1():
    # l = 5 #Local
    m = 8 #Local
    global l
    l = l + 45
    print(l, m)

function1()
# print(l)
# print(m)





# x = 89
# def function1():
#     x = 20
#     def function2():
#         global x
#         x = 88
#     print("before calling function2()", x)
#     function2()
#     print("after calling function2()", x)

# print(x)
# function1()
# print(x)





  
