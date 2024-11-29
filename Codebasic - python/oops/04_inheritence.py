## for eg lets make the class for players in which tennis and cricket both players are included
import datetime

class Player:
    def __init__(self,fname , lname, birth_yr):
        self.firstname = fname
        self.lastname = lname
        self.birthyear = birth_yr
    
    def cal_age(self):
        currentyear = datetime.datetime.now().year
        return currentyear -self.birthyear
    
class TennisPlayer(Player):
        def __init__(self, fname , lname, birth_yr):
            super().__init__(fname, lname, birth_yr)
            self.aces = []
            
class CricketPlayer(Player):
        def __init__(self, fname , lname, birth_yr):
            super().__init__(fname, lname, birth_yr)
            
roger = TennisPlayer("Roger", "Garner", 1788)
print(roger.birthyear)

rohit = CricketPlayer("Rohit", "Sharma", 1985)
print(rohit.firstname, rohit.lastname)
