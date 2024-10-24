#print all element in list 

def inda(list,index=0):
    if index == len(list):
        return
    print(list[index])
    inda(list, index+1)
    
dict = ["aap", "mai", "tum"]
inda(dict)