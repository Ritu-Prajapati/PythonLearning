# sum of first n natural no. 

def cal(n):
    if n== 0 :
        return 0
    
    return cal(n-1) + n 
    

print(cal(10))