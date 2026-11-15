import numpy as np
a= np.array([1, 2, 3])
print(a)
print(type(a))
b= np.array([4, 5, 6])
print(a + b)
print(a * b)
print(a ** 2)
c= np.array([1, 4, 9, 16, 25])
print(np.sqrt(c))
print(np.mean(c))
print(np.sum(c))
print(np.max(c))
#index and slicing
m =   np.array([[1, 2, 3],
                [4, 5, 6]])

print(m[0, 1])   # row 0, col 1

mm= np.array([10, 20, 30, 40, 50])
print(mm[0])
print(mm[3])
print(mm[:4])
#2d index
print(m[0, 0]) # row, column
print(m[1, 0])
print(m[0, 1])
print(m[1, 1])
print(m[0, 2])
print(m[1, 2])
d= np.array([10, 25, 30, 5])
f= np.array([10,])
print(d[d > 20])
a = np.arange(6)
e = d.reshape(2, 2)
print(e)