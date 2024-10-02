s1= {1 , 3 , 4 , 45}
s2 = {6, 7, 1, 76}

# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.intersection_update(s2) # this means that s1 is updated with only the intersection 
# print(s1)
z = s1-s2
y = s2-s1
x= s1 + s2
print(z , y, x)