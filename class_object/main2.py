class Person:
    name :"Ritu"
    occupation :"Model"
    networth = "10M$"
    def info(self):
        return self.name 

a = Person()
print(self.name)

class Person:
    # Class variables
    name = "Ritu"
    occupation = "Model"
    networth = "10M$"

    def __init__(self, name):
        # Instance variable
        self.name = name

# Class attribute usage
a = Person("Alice")
print(a.name)  # Output: Alice (instance variable)
print(Person.name)  # Output: Ritu (class variable)
