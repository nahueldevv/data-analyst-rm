import numpy as np

# =====================
# Create a basic array
# =====================
print(np.zeros(5))
print(np.ones(5, dtype=np.int64))
print(np.empty(4))

#NOTE: The reason to use empty over zeros (or something similar) is speed - just make sure to fill every element afterwards!

print("=" * 50) # separator

print(np.arange(2, 10, 3)) # (start, stop, step)
print(np.linspace(0, 100, 5)) # (start, stop, nums to show) -> the step is calculated automatly)

data, step = np.linspace(0, 10, num=5, retstep=True)
print(data)
print("step:", step)

my_numpy_arr = np.array(
  [[1, 3, 4, -1, 10],
  [3, 4, 7, 1, 0]]
) # create a ndarray from simple array

print(my_numpy_arr)
print(my_numpy_arr.shape)


print("=" * 50) # separator

# =============================
# Adding, removing, sorting 
# =============================
a = np.arange(1, 6)
b = np.arange(-5, 0)

print(a, b) # [1 2 3 4 5] [-5 -4 -3 -2 -1]

concatenated = np.concatenate((a, b))
print(concatenated) # [1 2 3 4 5 -5 -4 -3 -2 -1]

print(np.sort(concatenated))

# Example with 2D arrays

c = np.array([
  [1, 2, 3], 
  [4, 5, 6]]
)
d = np.array([[-3, -2, -1]])

print(np.concatenate((c, d), axis=0)) # axis=0 -> default


print("=" * 50) # separator

# =============================
# Reshape 
# =============================
a = np.arange(6)

print("a:", a)
print("reshaped\n", a.reshape(2, 3))
print("reshaped\n", np.reshape(a, shape=(3, 2)))


print("=" * 50) # separator

# =============================
# Convertions 
# =============================
a = np.arange(6)
print(a)
print("a:", a.shape)  # (6,)

row_vector = a[np.newaxis, :]
print(row_vector.shape) # (1,6)

col_vector = a[:, np.newaxis]
print(col_vector.shape) # (6,1)

# All is equal with expand_dims method

print("expand_dims:")
print(np.expand_dims(a, axis=0)) # (1,6)
print(np.expand_dims(a, axis=1)) # (6,1)