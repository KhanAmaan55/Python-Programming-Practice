with open("20.txt") as f:
    print(f.readlines())        ##no need to close file while using with block

f=open("20.txt")                ##you can open file again after with block as it was closed after with statement
print(f.readline())
f.close()