# reverse string usng Loop 
x = "stringy"
y = len(x) - 1
reve = ""
while y >= 0:
    reve += x[y]
    y -=1
print(reve)
# for 
v = "again"
rev = ''
for char in v:
    rev = char + rev
print(rev)