'''How would you concatenate two string variables, say str1 = "Hello" and str2 = "World" in Python?

Write a Python code snippet to take user input for their name and greet them, using the input() function.

If you have a list my_list = [1, 2, 3, 4, 5], how would you access the third element of this list?

What is the main difference between a list and a tuple in Python?

How would you convert a tuple my_tuple = (1, 2, 3) into a list?'''

str1 = "Hello" 
str2 = " World"
str = str1 + str2 
print(str)

name = input("Enter your name ")
print(f"Hello {name},how are you doing?")

my_list = [1, 2, 3, 4, 5]
print(my_list[2])

my_tuple = (1, 2, 3)
print(list(my_tuple))
