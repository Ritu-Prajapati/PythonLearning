class Person:
    name = "Ritu"
    occupation = "Analyst"
    age = 22
    networth = 10
    def info(self):
        print(self.name )
a = Person()
a.name = "Usha"
# a.occupation= "Business Woman"
# print(a.name, a.occupation)
print(a.info())
