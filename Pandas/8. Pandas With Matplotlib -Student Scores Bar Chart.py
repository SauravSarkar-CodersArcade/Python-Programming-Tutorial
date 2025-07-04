import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create sample data using Pandas
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Marks": [88, 76, 93, 65, 85]
}

df = pd.DataFrame(data)

"""
Creates a DataFrame like:

   Student  Marks
0   Alice     88
1     Bob     76
2 Charlie     93
3   David     65
4     Eve     85
"""

# Step 2: Plot a bar chart using Matplotlib
plt.bar(df["Student"], df["Marks"], color='skyblue')

# Step 3: Add labels, title
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Marks Scored by Students")
plt.ylim(0, 100)  # Optional: y-axis limit

# Step 4: Display the plot
plt.show()
