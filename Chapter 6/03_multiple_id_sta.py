a = int(input("enter your age "))

# If statement no. 1 
if(a%2==0):
    print("a is even")
# end of If statement no. 1 

#if statment no. 2
if(a>=18):
    print("You are above the age of consent")

elif(a<0):    
    print("Negative no. is invalid")

elif(a==0):
    print("0 is invalid")

else:    
    print("You are below the age of consent")
# end of If statement no. 2

print("--Check your age again--")    