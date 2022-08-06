f1= open("20.txt")
try: 
    f2= open("25.txt")

except Exception as e:
    print(e)

# except EOFError as e:
#     print("EOFError",e)
# except IOError as e2:
#     print("IOError",e2)

else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway")
    f1.close()
    # f2.close()

print("Important stuff")