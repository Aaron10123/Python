import os

print(os.listdir())

with open("new_file.text", "w") as f:
    f.write("Hello, MicroPython!")


print(os.listdir())

os.remove("new_file.text")

print(os.listdir())
