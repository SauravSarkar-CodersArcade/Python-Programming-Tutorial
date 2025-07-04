import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [50000, 45000, 55000, 48000, 60000]
})

# Average salary by department
avg_salary = df.groupby("Department")["Salary"].mean()

"""
.groupby() groups data by unique values in 'Department'
.mean() computes average salary per group
"""

print("Average Salary:\n", avg_salary)
