# Multiplication upto 10 but skip 5th iteration 
m = int(input('Enter any no.: '))
n = 1
while n <=10:
    n +=1
    if n ==5:
        continue
    print(f'{m}*{n}={m*n}')

#for 
for i in range (1, 11):
    if i == 5:
        continue
    print(f'{m}*{i}={m*i}')
    
    

