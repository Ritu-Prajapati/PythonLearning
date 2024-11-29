import datetime

class cricketplayers:
    def __init__(self, fname, lname, birth_year, team):
        self.firstname = fname
        self.lastname = lname
        self.birthyear = birth_year
        self.team = team
        self.scores= []
        
    def add_score(self, score):
        self.scores.append(score)

    def avg_scores(self):
        return sum(self.scores)/len(self.scores)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}, the cricket player from {self.team}"

      
virat = cricketplayers("Virat" , "Kohli", 1988, 'India')
virat.add_score(80)
virat.add_score(67)
virat.add_score(50)

print(virat)
print(virat.firstname)
print(virat.lastname)
print(virat.birthyear)
print(virat.scores)
print(virat.avg_scores())

david = cricketplayers("David" , "Warner", 1985 ,"Australia")

david.add_score(40)
david.add_score(27)
david.add_score(0)

print(david.firstname)
print(david.lastname)
print(david.birthyear)
print(david.scores)


