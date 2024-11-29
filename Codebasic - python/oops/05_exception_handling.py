x = 10 #int(input("Enter no. "))
y = 0 #int(input("Enter no. "))

# exception handling 
# specifically using division by zero 
a=0
try:
    d = x/y
    a = 'baby yoda' + 56

# # division by zero
except ZeroDivisionError as ze:
    print("Exception occured: ", ze)
    d = -1 

# # type error
except TypeError as te:
    print("Exception occured: ", te)
    d = -1 

# generic exception - include all exception case 
except Exception as e:
    print("Generic Exception occured: ", e)
    d = -1 

print("Division is ",d)