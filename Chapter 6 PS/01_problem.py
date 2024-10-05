# enter the greatest of four no. 
a1= int(input("Enter no.1: "))
a2= int(input("Enter no.2: "))
a3= int(input("Enter no.3: "))
a4= int(input("Enter no.4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest no. is a1", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest no. is a2", a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("Greatest no. is a3", a3)
else:
    print("Greatest no. is a4", a4)