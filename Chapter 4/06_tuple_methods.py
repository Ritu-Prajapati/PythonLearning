ac= (1, 45, "Rohan", False, 34.67, 45)

c = ac.count(45)
print(c) # count the no. of time its present in tuple 
i  = ac.index(45)
print(i) # find the index no. in whch that value is present 
print(len(ac))   #len of the value

bb= (2, 4, 6,8)
print(sum(bb)) #sum of the tuple

# concatenation using + , repeat using * 
y= (9, 10)
z= (2,3)
concate = y + z 
repeat = y * 3
print(concate, repeat)

# zip(): Combines two or more iterables (such as tuples) element-wise into tuples.
alpha = ("a", 'b', 'c')
words = ("apple", "ball", "cat")
zip = zip(alpha , words)
print(list(zip))
print("apple" in words)
print("a" in alpha)
