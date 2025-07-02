# Read from one file and write to another
with open("hello.txt", "r") as source:
    with open("copy.txt", "w") as dest:
        for line in source:
            dest.write(line)
