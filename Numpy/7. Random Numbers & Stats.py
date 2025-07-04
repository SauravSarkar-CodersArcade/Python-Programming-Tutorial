import numpy as np

# Random float values between 0 and 1
rand_floats = np.random.rand(3)
print(rand_floats)

# Random integers between 1 and 100 (size 5)
rand_ints = np.random.randint(1, 100, size=5)
print(rand_ints)
# Statistics on array
data = np.array([5, 10, 15, 20, 25])
print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))
print("Maximum:", np.max(data))
