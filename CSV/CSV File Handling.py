import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Name", "Score"])
    writer.writerow([101, "Alice", 87])
    writer.writerow([102, "Bob", 91])

# Reading the CSV file
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
