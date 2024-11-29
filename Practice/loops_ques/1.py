# sum even numbrs 
# while 
list = [8, 56, -5 , -9]
n = 0
sum = 0
while n < len(list):
    if list[n] % 2 == 0:
        # print(list[n])
        sum =list[n] +sum
    sum
    n +=1
print(sum)

# for
sumy =0
for l in list:
    if l % 2 == 0 :
        sumy = sumy + l
print(sumy)