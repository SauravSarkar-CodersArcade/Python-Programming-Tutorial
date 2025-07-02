with open("hello.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Total words:", len(words))
