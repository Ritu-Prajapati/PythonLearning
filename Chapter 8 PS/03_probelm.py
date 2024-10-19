# WAF to  find  the factorial of n!
# write caode to print the factorial and then add the function 


def fac(n):
    x = 1
    for i in range (1, n+1):
        x = x * i 
    print(x)  
    return x 

fac(3)
