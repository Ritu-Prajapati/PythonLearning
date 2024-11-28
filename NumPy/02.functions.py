import numpy as np 
m = np.array([[2,3,9,5], [7,8,9,2]])
print(m, m.shape)  #(2 rows, 3 col)

print(m.itemsize) # size of bytes each elemts taking

# YOU CAN WRITE THIS m.size or np.size(m)
print(m.size)  #count of elements 
print(np.size(m))

# sorting 
print(np.sort(m)) 
# flattened in one line 
print(np.sort(m, axis = None)) 

#linspace (evenly distribute)
x= np.linspace(0, 10, 5)
print(x)

#-------
# flatten the array:
# return the view of the original data not copy 
print(m.ravel())
#rreturn the copy flatten
print(m.flatten())

#we can have reshape 
y = np.array([[2,3,9], [7,8,9]])
print(y.shape)
print(y.reshape(3,2))

#min / max both ways 
print(np.min(y)) 
print(y.min()) 

#sum 
rev= np.array([[4, 5,6 ], [9, 10, 12]])
print(rev.sum(axis = 1)) # row wise sum 
print(rev.sum(axis = 0)) # column wise sum 
for row in rev:
    print('row >', row)

s= np.array([1, 4, 16])
print(np.sqrt(s))   # it wont take s.sqrt()
print(np.square(s))  
print(np.std(s))  