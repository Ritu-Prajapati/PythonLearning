import numpy as np 
m = np.array([[2,3,9,5], [7,8,9,2]])
print(m, m.shape)  #(2 rows, 3 col)

print(m.itemsize) # size of bytes 
print(m.size)  #number of elements 

# sorting 
print(np.sort(m)) 
# flattened in one line 
print(np.sort(m, axis = None)) 