# adding value in list using append 
code = ["fr", "brb", "ngl"]
code.append("idk")
print(code)

# sorting 
l = [1, 4,68, 34, 45,22]
l.sort()
print(l)

#reverse 
a = [ 4, 23, 56, 32]
a.reverse()
print(a)

#insert value in between 
b = [4, 74, 56, 45]
b.insert(3,888)
print(b)

# .pop()
abc= [34, 45, 56, 23 , 46]
print(abc.pop(1))
print(abc)

#remove
x= [34, 45, 27, 7 ]
x.remove(34)  # removes the exact match 
print(x)

#new 
tt = [ 23, 45, 12, 28, 75, 93, 56, 67]

'''I have to get descending value'''
# a.sort()
# a.reverse()
'''replace index 3 value 28 to 42'''
tt.pop(3)
tt.insert(3,42)
print(tt)