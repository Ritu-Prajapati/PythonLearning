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
    
    def get_age(player):
        current_year= datetime.datetime.now().year       # datetime = module and .datetime = is class datetime module
        return current_year - player['birth_year']

    def __lt__(self,other):  #  Operator Overloading-1 ///
        self_avg_score  = self.avg_scores()
        other_avg_score = other.avg_scores()
        return self_avg_score < other_avg_score
    
    def __et__(self, other):   #  Operator Overloading-2 ///
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age == other_age

   
virat = cricketplayers("Virat" , "Kohli", 1988, 'India')
virat.add_score(80)
virat.add_score(67)
virat.add_score(50)


david = cricketplayers("David" , "Warner", 1985 ,"Australia")

david.add_score(40)
david.add_score(27)
david.add_score(0)


print(virat < david)  #  Operator Overloading-1 ///
print(virat == david)  #  Operator Overloading-2 ///