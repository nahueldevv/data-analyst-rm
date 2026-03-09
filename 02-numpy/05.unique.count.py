import numpy as np

# =============================
# Unique and Count
# =============================

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)

print(a)
print(unique_values)

# To get the indices of unique values in a NumPy array (an array of first index positions of unique values in the array), just pass the return_index argument
_, indices_list = np.unique(a, return_index=True)
print(indices_list)

# You can pass the return_counts argument in np.unique() along with your array to get the frequency count of unique values in a NumPy array.
_, counts = np.unique(a, return_counts=True)
print(counts) # 11 -> 3 times, 12 -> 2 times, ...

print("2d arrays")

a_2d = np.array([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [1, 2, 3, 4]
])
print(np.unique(a_2d)) # ret an array with all unique elements

# If you want to get the unique rows or columns, make sure to pass the axis argument. To find the unique rows, specify axis=0 and for columns, specify axis=1.
print("a_2d\n", a_2d)

unique_rows = np.unique(a_2d, axis=0)
print("unique_rows\n", unique_rows)


unique_rows, indices, occurrence_count = np.unique(
  a_2d, axis=0, return_counts=True, return_index=True)

print(unique_rows)
print(indices)
print(occurrence_count)