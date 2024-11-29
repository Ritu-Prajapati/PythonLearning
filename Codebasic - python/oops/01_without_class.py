import datetime

def get_avg_score(player):
    return sum(player['score'])/len(player['score'])

def get_age(player):
    current_year= datetime.datetime.now().year       # datetime = module and .datetime = is class datetime module
    return current_year - player['birth_year']

virat = {
    "f_name" : "Virat",
    'l_name' :"kohli",
    'score': [],
    'birth_year' : 1988

}

rohit = {
    "f_name" : "Rohit",
    'l_name' :"Sharma",
    'score': [],
    'birth_year' : 1982
}

virat['score'].append(80)
virat['score'].append(100)
virat['score'].append(0)

rohit['score'].append(200)
rohit['score'].append(130)
rohit['score'].append(80)


print(get_avg_score(virat))
print(get_age(virat))

# likewise adding another dictionary for different person 
# to much of task lets use class 
