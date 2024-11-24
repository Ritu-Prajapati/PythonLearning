#first non repeated character 
x = "teeth"
y = 0
while y <= len(x):
    y +=1 
    if x.count(x[y]) ==1:
        print(x[y])
        break

# for 

for char in x:
    if x.count(char)== 1:
        print(char)
        break