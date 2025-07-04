import pandas as pd

df = pd.DataFrame({
    "Name": ["Tom", "Jerry"],
    "Score": [95, 89]
})

# Save to file
df.to_csv("output.csv", index=False)

"""
Saves the DataFrame to 'output.csv' without row numbers (index=False).
"""
