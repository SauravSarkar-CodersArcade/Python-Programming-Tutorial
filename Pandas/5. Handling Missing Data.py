import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Eve", "Frank", "Grace"],
    "Marks": [np.nan, 78, 90]
})

# Fill missing values with 0
df_filled = df.fillna(0)

# Drop rows with missing data
df_dropped = df.dropna()

"""
.fillna() replaces NaN values.
.dropna() removes rows with any NaN values.
"""

print("Original:\n", df)
print("\nFilled:\n", df_filled)
print("\nDropped:\n", df_dropped)
