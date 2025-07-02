import os

try:
    if os.path.exists("hello.txt"):
        with open("hell.txt", "r") as file:
            print(file.read())
except FileNotFoundError:
    print("File does not exist!")
