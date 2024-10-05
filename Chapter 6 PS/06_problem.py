a = int(input("enter your marks "))


if(a>=90 and a<=100 ):
    grade = "Excellent"

elif(a>=80 and a<90):    
    grade = "A"

elif(a>=70 and a<80):
    grade = "B"

elif(a>=60 and a<70):
    grade = "C"

elif(a>=50 and a<60):
    grade = "D"

elif(a<50):
    grade = "E"

print("Your grade is", grade)

   