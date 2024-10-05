#print pass or  fail , requires total of 40% and each subject altleast 33%. Print 3 subject marks 
m1 = int(input("enter subject1 marks "))
m2 = int(input("enter subject2 marks "))
m3 = int(input("enter subject3 marks "))

tot_percentage = ((m1+m2+m3)/300)*(100)
# first if for each sub 33% 
if(tot_percentage >=40 and m1>=33 and m2>=33 and m3 >= 33):
    print("Passed!!")

else:
    print("Sorry you are fail, try again next year", tot_percentage)

