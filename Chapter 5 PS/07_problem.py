# even though the name of 2 person is name there will be cahnge the updated version willbe written
# for eg if Ritu fav lang is python but again Ritu fav language is french then 'Ritu' : 'French' prints
#key will update ; here key is name 
dict = {}
lang1 = input("enter your fav language ")
name1 = input("enter your name ")
dict.update({name1: lang1})
lang2 = input("enter your fav language ")
name2 = input("enter your name ")
dict.update({name2: lang2})
lang3 = input("enter your fav language ")
name3 = input("enter your name ")
dict.update({name3: lang3})
lang4 = input("enter your fav language ")
name4 = input("enter your name ")
dict.update({name4: lang4} )

# dict.update([(lang1, name1), (lang2, name2), (lang3, name3), (lang4, name4)] ) or we can use this 
print(dict)