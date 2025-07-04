import numpy as np
import matplotlib.pyplot as plt

# Generate X values from 0 to 10
x = np.linspace(0, 10, 100)

# Y values = sin(x)
y = np.sin(x)

# Plot the graph
plt.plot(x, y, label='sin(x)', color='blue')

# Add title and labels
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Show the plot
plt.show()
