#calculate the sum of even no. a given no 
# while 
n = 0
s = 0 
while n <= 10 :
    if n % 2 ==0:
        s = n + s
    n +=1
print(s)

# for 
d= 0
for i in range(0, 11):
    if i % 2==0:
        d= i + d
print(d)