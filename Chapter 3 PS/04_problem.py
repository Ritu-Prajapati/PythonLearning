# replace double space with single space 
a = "he is good  boy."
print(a.replace("  ", " ")) # returns -1 if it doesnot find the value
print(a) 

''' strings are immutable which means that you cannot change them
by running functions on them a still holds the
str as he is good  boy '''