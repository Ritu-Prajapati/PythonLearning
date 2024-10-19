# repeating funtions 
a = 10 
b = 2 
sum = a + b 
print(sum)

a = 23
b = 25
sum = a + b 
print(sum)

# lets create function rather than repeating the sum problem 
# function definition 
def  cal_sum(a , b): # parameters 
    sum = a+ b 
    print(sum)
    return sum

cal_sum(6,7)  # function call; arguments 

# thus now we dont have to repeat and it reduces redundancy

cal_sum(10, 2)
cal_sum(25, 23)