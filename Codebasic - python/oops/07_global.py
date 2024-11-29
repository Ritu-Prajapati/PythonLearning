# defining global 

def hello():
    global w 
    w = 56
    print("hello world!")

hello()
print(w)
# without defining global
def hello(): 
    w = 56
    print("hello world!")

hello()
print(w) # it throws error that w doesnot exist coz its local 