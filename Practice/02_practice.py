'''String Methods: Given sentence = "Python is Awesome!", how would you:
Convert the entire string to lowercase?
Count the number of times the letter 'o' appears in the sentence?''' 
string=  "Python is Awesome!"
lower = string.lower()
count = string.count("o")
print(lower)
print(count)


'''List Slicing: If numbers = [10, 20, 30, 40, 50, 60, 70, 80], how would you:
Extract the first four elements from the list?
Reverse the list using slicing?'''

list= [10, 20, 30, 40, 50, 60, 70, 80]
print(list[0:4])
list.sort()  # i tried using sort and reverse 
list.reverse()
print(list)
reversed_list = list[::-1]  # Slicing to reverse the list
print(reversed_list)  # Output: [80, 70, 60, 50, 40, 30, 20, 10]


'''Tuple Unpacking: Given the tuple my_tuple = (1, 2, 3), how would you unpack the values into variables a, b, and c?'''
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)

'''List Comprehension: Write a one-line Python list comprehension to create a list of squares for all numbers from 1 to 10.''' 
sq= [x**2 for x in range(1, 11)]
print(sq)

'''Dictionary: Create a dictionary student with the following key-value pairs: Name = "John", Age = 21, Grade = "A". Then, update the age to 22 and print the updated dictionary.'''
dict = { "Name": "John" , "Age": 21, "Grade": "A"}  # learned about dictinary 
dict["Age"]= 22
print(dict)   #A dictionary in Python is a collection of key-value pairs. It's similar to a real-world dictionary

'''Handling Errors: Write a code that tries to convert a string s = "abc" to an integer using int(), and handle the error if it occurs by printing "Invalid input!".'''

s = "abc"    # learned about try and except case
try:
    print(int(s))
except ValueError:
    print("Invalid input!")