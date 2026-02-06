import numpy as np
a = np.arange(0,24)
b = a.reshape(2,3,4)
print(b)
filter_arr = b > 10
newarr = b[filter_arr]
print("Elements greater than 10")
print(newarr)
print("Count of even elements")
even = b[b % 2 == 0]
print( len(even) )
print("All elements less than 10 replaced with 0")
mask = b < 10

b[mask] = 0
print(b)
