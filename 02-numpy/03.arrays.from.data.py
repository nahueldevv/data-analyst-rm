import numpy as np

# =============================
# Arrays from existing data
# =============================

# You can also stack two existing arrays, both vertically and horizontally. Let’s say you have two arrays, a1 and a2:
a1 = np.array([[1, 1], [2, 2],])
a2 = np.array([[3, 3], [4, 4]])

# You can stack them vertically with vstack:
print(np.vstack((a1, a2)))

# Or stack them horizontally with hstack:
print(np.hstack((a1, a2)))


# You can split an array into several smaller arrays using *hsplit*. You can specify either the number of equally shaped arrays to return

x = np.arange(1, 25).reshape(2, 12)

print(x)

# If you wanted to split this array into three equally shaped arrays
print(np.hsplit(x, 3)) # three 2x4 arrays


# Copy
print("=" * 20)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :] 

print(a)
print(b1) # [1, 2, 3, 4]

b1[0] = 99

print("after of change")

print(b1) # [99, 2, 3, 4]
print(a) # you can show like was modified

# Using the copy method will make a complete copy of the array and its data
b2 = a.copy()
print(b2)