d = {} # empty dict
marks = {
    "harry" : 100,
    "rohan" : 46,
    "shubh" : 53,
    56.89: "DDLJ",
    False: "ipknd"
}
print(marks.items())
print(marks.values())
print(marks.keys())

marks.update({"harry": 99, "renuka" : 56})
print(marks)

# difference between .get() and indexing in dict:
print(marks.get("jyoti")) # print None
#print(marks["jyoti"])   # shows error

marks.pop("harry") # droped the key and values 
print(marks)

