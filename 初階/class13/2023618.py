# import os

# file_path = "class4\syicjkhvjb,bjv"

# if os.path.isfile(file_path):
# file = open(file_path, 'r')
# print(file.read())
# file.close()
#     with open(file_path, "r") as file:
#         print(file.read())

# else:
#     print("File not found")

fileName = 'text.txt'
Mode = "w"
myFile = open(fileName, Mode)
myFile.write("Hi\n")
myFile.write('aaaaaaaaaa')
myFile.close()

file_name = "example.txt"
mode = "a"
with open(file_name, mode) as file:
    file.write("World\n")
    file.write(" is our new text file\n")