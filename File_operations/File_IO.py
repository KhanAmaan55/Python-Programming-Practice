f = open("20.txt")
# # for iterating every line(dont take content in any variable)
# for line in f:
#     print(line)

# content = f.read(3)
# print("1 .",content)
# content = f.read(2)
# print("2 .",content)
# content = f.read()
# print("3 .",content)

# # for iterating every charactor
# content = f.read()
# for line in content:
#     print(line)

# # for reading everyline
# print(f.readline())
# print(f.readline())
# print(f.readline())

# # for reading file in the form of list
# print(f.readlines())

# # seek() and tell()
# print(f.tell())
# print(f.readline())
# f.seek(10)
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
f.close()
