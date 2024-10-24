# recursive function 
def show(n):
    if (n ==0):   # condition to nullfy the infinite loop 
        return
    print(n)
    show(n-1)

# show(4)  #5, 4 = n -1 , 3= n-2, 2= n-3, 1 


# or using loop
def w_l(i):
    while (i>= 0):
        print(i)
        i = i - 1

w_l(5)
