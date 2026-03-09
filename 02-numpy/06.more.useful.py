import numpy as np

# =============================
# Transposing and reshaping
# =============================

x = np.arange(1, 25).reshape(6, 4)
print(x)

print(x.transpose())
print(x.T)


# =============================
# Reverse an array
# =============================
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr)

print(arr)
print('Reversed Array: ', reversed_arr)

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d)
print(reversed_arr)

print("\n2d Array:\n", arr_2d)

reversed_arr_rows = np.flip(arr_2d, axis=0)
print("rev_rows:\n", reversed_arr_rows)

reversed_arr_columns = np.flip(arr_2d, axis=1)
print("rev_cols:\n",reversed_arr_columns)

# You can also reverse the contents of only one column or row.
arr_2d[1,:] = np.flip(arr_2d[1,:])
print("Reversed row 2:\n", arr_2d)