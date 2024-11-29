# '''Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)'''
# #loop 
# acc = 5
# buc = 0

# for i in range(1, acc+1):
    
#     buc = buc + i
# print(buc)
# # Built in function 
# x= sum(range(1, acc+1))
# print(x)

# '''no. must be divisible by 5'''

# a= [45, 56, 67, 70, 98, 30]
# for i in a:
#     if i% 5 == 0:
#         print(i)

# # reverse

# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in range(0,list,-1):
#     print(item)

# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i])

# print from -10 to -1
for j in range(-10,0):
    if j==0:
        break
    print(j)

list = []
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.remove(1)
list.sort()
list.pop(1)
print(list)
