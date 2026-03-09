import numpy as np

# =============================
# Indexing
# =============================

# You can index and slice NumPy arrays in the same ways you can slice Python lists.
a = np.array([-1, 2, 10, 93, 0])
print(a[3]) # 93
print(a[2:-1]) # [10, 93]

# If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.
a = np.array([
  [1, 2, 3, 4], 
  [5, 6, 7, 8], 
  [9, 10, 11, 12]
])
print(a[a < 5])

five_up = (a > 5) | (a == 5)
print(five_up)

# You can use np.nonzero() to print the indices (coordinates) of elements that are, for example, less than 5:
b = np.nonzero(a > 5)
print(b)


print("=" * 20)

# =============================
# Slicing
# =============================
a = np.random.randint(0, 10, size=(3, 4))
print(a)

# NOTE The : means all, and for access the matrix element remenber -> m[rows, cols]

# print all second column
print("second row:\n", a[:,1])

# print a submatrix
print("submatrix:\n", a[1:,2:])

random_3d = np.random.randint(0, 20, size=(2, 2, 3))

print("3d Matrix")
print(random_3d)
print(random_3d.shape)

print("submatrix")
print(random_3d[:,:,1])