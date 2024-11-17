import numpy as np

rev_q1  = np.array([6, 12, 14]) # quadrant 1 revenue in millions
rev_q1_q2 = np.array([[4, 5,6 ], [9, 10, 12]]) # quadrant 1 & 2 revenue in millions

print(rev_q1.ndim ,rev_q1_q2.ndim)  # array dimensions

print(rev_q1_q2[1][0]) 
print(rev_q1_q2[1,0]) #can be access in both ways 

# values can be changed
rev_q1_q2[1,0]= 11
print(rev_q1_q2)

