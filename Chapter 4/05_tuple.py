a = (1,) #tuple
b = (1) # integer

print(type(a))
print(type(b))

ac= (1, 45, "Rohan", False, 34.67, 45)
# ac[0] = 56 - this wont change the tuple value coz its immutable
print(ac)
 

print(ac.count(45))
print(ac.index(45))