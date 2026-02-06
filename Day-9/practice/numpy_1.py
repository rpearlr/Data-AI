import numpy as np

a = np.array([1,2,3])
print(a)

a = np.array([[1,2,3],[4,5,6]])
print(a)

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a)

print(a[1])
print(a[0 ,1:2])
print(a[1,1,1])

print(a.shape)

b = np.array([1,2,3,4,5,6,7,8,9,0])
c = b.reshape(5,2)
print("2D : " ,c)
d = b.reshape(2,1,5)
print(d)
d = a.reshape(-1)
print(d)

image = np.random.randint(0,255,(64,64,3))
r= image[:,:,0]
print(r)

print(a*4)
