import pandas as pd

# Create a DataFrame using a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

"""
This creates a table (DataFrame) like:

      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
"""

print(df)
