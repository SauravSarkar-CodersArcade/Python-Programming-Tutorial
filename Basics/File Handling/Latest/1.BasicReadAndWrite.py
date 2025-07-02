# Write to a file
with open("hello.txt", "w") as file:
    file.write("Hello, Python File Handling!\n")
    file.write("This is line 2.\n")

# Read from the same file
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
