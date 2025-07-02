lines = ["First line\n", "Second line\n", "Third line\n"]
with open("list_output.txt", "w") as file:
    file.writelines(lines)
