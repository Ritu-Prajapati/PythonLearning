import numpy as np
# zip 
x = [5,6,9]
y = [8,6,3]
print(tuple(zip(x, y)))

for x,y in zip(x,y):
    print(x+y)

z= np.array([5,4,4])
a= np.array([7,5,6])
print(z + a)