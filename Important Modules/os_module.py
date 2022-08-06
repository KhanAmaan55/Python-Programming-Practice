import os
print(dir(os))
print(os.getcwd())  ## used to show the directory of program
os.chdir("C://")  ## used to change directory
print(os.getcwd())
print(os.listdir())  ## used to get all the folders/files that are present in the directory
os.mkdir("made by os module")  ##used to create a new folder in the directory
os.makedirs("main folder by os module/sub folder by os module")  ## used to create new folder and sub folders
os.rename("yello.txt", "hello.txt")   ## used to rename any file inside the directory
print(os.environ.get('Path'))  ## used to get environent variable
print(os.path.join("C:/", "/hello.txt"))  ## used to join two paths WITHOUT ANY ERROR
print(os.path.isfile("C:\\Program Files"))  ## checks whether the file exists or not
print(os.path.isdir("C:\\Program Files"))  ## checks whether the dir exists or not