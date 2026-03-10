import pandas as pd
import numpy as np

# =============================
# Series (1D)
# =============================
# is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).

# Here, the data can be many different things: python dictionary, a ndarray, or a scalar value
data = np.random.randn(5)

# data = {"a":0, "b":1, "c": 2} # here, the keys will be labels
# data = 5 # here, the value is copied for labels

s = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(s)

print(s.index)
print(s.ndim)

# Series acts very similarly to a np.ndarray and is a valid argument to most NumPy functions. However, operations such as slicing will also slice the index.
print(s.iloc[0])
print(s.iloc[:2])

print("Getting C value: ", s.get("c"))
# print("Getting C value: ", s.get("f")) # None

print("====== Operating ======")

print(s + 2)
print(s * 2)


print("================= Dataframes =================")

# =============================
# Dataframes (2D)
# =============================
# is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects.

# From dict of Series
d = {
  "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
  "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(d)
print(df)
print(df.shape)
print(df.columns)
print(df.index)

print() # divider

print(pd.DataFrame(d, index=["d", "b", "a"]))
print(pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"]))

# From a list of dicts
d = [
  {"a":1, "b":2, "c":3},  # row1
  {"a":-1, "b":-2, "c":-3, "d": -4} # row2 ...
]

print() # divider

df = pd.DataFrame(d)
print(df)

print("Getting column b")
print(df.get("b"))

print("=" * 50)

# ========================================
# Column selection, addition and removing 
# ========================================

data = {
  "one": np.random.randint(20, size=(10,)),
  "two": np.random.randint(20, size=(10,))
}

df = pd.DataFrame(data)
print(df)

print()

df["three"] = df["one"] + df["two"]
df["twenty_up"] = df["three"] > 20
# df["one"] = 2 # change all one column values

print(df)

# Columns can be deleted or popped like with a dict:
three = df.pop("three")

print()
print(df)

df.insert(2, "new_two", np.random.randn(10)) # (column_index, column_name, value)

print()
print(df)

print()
print(df.loc[4])  # select row
print(df.iloc[4:8]) # slice rows