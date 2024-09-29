#print(letter template ) 
#chaining of .replace()
letter= '''Dear <|Name|>
You are selected!
<|date|>'''
name = input("enter your name ")
date = input("Enter in format DD-MM_YYYY ")
print(letter.replace("<|Name|>", name).replace("<|date|>", date))
