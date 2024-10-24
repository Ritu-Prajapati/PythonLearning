# factorial 1 or 0 = 1
# def factorial(n):
#     if (n==0 or n ==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# # print(factorial(3))

# fibonacci
# f(0) = 0 
# f(1) = 1 
# f(2)= f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibbo(f):
    if (f==0):
        return 0
    elif (f==1):
        return 1
    else:
        
        return fibbo(f-1) + fibbo(f-2)
    
def fib_series(g):
    for i in range(g):
        print(fibbo(i), end = " ") 
    
fib_series(5)

