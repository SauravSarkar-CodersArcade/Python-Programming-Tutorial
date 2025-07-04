import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Ana", "Ben", "Chris"],
    "Marks": [88, 76, 93]
})

# Get column
print("Names:\n", df["Name"])

# Add new column
df["Passed"] = df["Marks"] > 80

# Filter rows where Passed is True
passed_students = df[df["Passed"]]

"""
Filters students who have marks > 80:

   Name  Marks  Passed
0  Ana     88    True
2  Chris   93    True
"""

print(passed_students)
