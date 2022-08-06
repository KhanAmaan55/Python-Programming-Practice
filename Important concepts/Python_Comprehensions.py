print("\n")
print("-- LIST COMPREHENSIONS --")
print("Without Comprehensions")
ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)

print(ls)
print("\nWith Comprehensions")

l1=[j for j in range(100) if j%3==0]
print(l1)
print("\n")
print("-- DICTIONARY COMPREHENSIONS --")
dict = {i:f"item{i}" for i in range(10)}
print(dict)
dict2={value:key for key,value in dict.items()}
print(dict2)
print("\n")
print("-- GENERATOR COMPREHENSIONS --")
even=(i for i in range (50) if i%2==0)
print(even)
print(even.__next__())
print(even.__next__())