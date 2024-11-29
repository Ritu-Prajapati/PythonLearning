import pandas as pd

l= [10, 20, 30, 40]
x= pd.Series(l)
# print(x)
y= pd.Series(l, index=['i', 'ii','iii', 'iv'])
print(y)