import pandas as pd

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D"],
    "Score": [87, 45, 92, 68]
})

# Sort by score (descending)
sorted_df = df.sort_values(by="Score", ascending=False)

# Summary statistics
stats = df["Score"].describe()

"""
.sort_values() sorts rows by a column.
.describe() gives count, mean, std, min, max, quartiles.
"""

print("Sorted:\n", sorted_df)
print("\nStats:\n", stats)
