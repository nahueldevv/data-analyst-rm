import numpy as np

# =============================
# Basic Arrays Operations
# =============================

# Basic operations are simple with NumPy

my_nums = np.array([1, 2, 3, 4, 5])
print(my_nums)

ones = np.ones(5, dtype=np.int16)

print(my_nums + ones)
print(my_nums - ones)

# If you want to find the sum of the elements in an array, you’d use sum()
print(my_nums.sum()) # 15

# You can sum over the axis of rows or cols:
b = np.array([[2, 4], [6, 8]])
print(b)

print("row sum:", b.sum(axis=0))
print("col sum:", b.sum(axis=1))


print("=" * 40)

# =============================
# Broadcasting
# =============================
a = np.array([1.0, 2.0])

print(a * 1.6)
print(a / 2)

b = np.array([
  [1, 2, 3],
  [4, 5, 6]
])
print(b * 2)


# Useful array operations
print("b:\n", b)

print(
  "min:", b.min(), 
  "max:", b.max(), 
  "sum:", b.sum(), 
  "prod:", b.prod(), 
  "avg:", b.mean()
)