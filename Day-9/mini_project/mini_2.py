import numpy as np
a = np.arange(0,24)
b = a.reshape(2,3,4)
print(b)
print("First layer")
print(b[0])
print("Last Layer")
print(b[-1])
print("Element at 0 , 1 ,2")
print(b[0,1,2])

print("first line in each layer")
for i in range(2) :
    print(b[i,0])

print("last line in each layer")
for i in range(2) :
    print(b[i,-1])