import pandas as pd

# Read a CSV file (make sure 'data.csv' exists)
df = pd.read_csv("Iris.csv")

"""
Reads the file 'data.csv' into a DataFrame.
Each row in the CSV becomes a row in the DataFrame.
"""

print(df.head())  # Show first 5 rows
print(df.tail())  # Show last 5 rows
print(df.info())
