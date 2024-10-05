# find any particular word 
a = input("Enter your comment ")

if("harry" in a.lower()): #using a.lower() so if user write either Harry or harry it will detect both 
    print("Harry is present")
else:
    print("harry is not present")