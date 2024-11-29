# Write code below 💖

g=0
r=0
h=0
s=0
Q1 = int(input("Do you like Dawn or Dusk? 1)Dawn 2)Dusk - "))
Q2 = int(input("When I’m dead, I want people to remember me as: 1)The Good 2)The Great 3)The Wise 4)The Bold- "))
Q3 = int(input("Which kind of instrument most pleases your ear? 1)The violin 2)The trumpet 3)The piano 4)The drum- "))

if Q1==1:
  g = g+1
  r= r+1
elif Q1 ==2:
  h= h + 1
  s= s +1

if Q2 == 1:
  h = h+2
elif Q2 ==2 :
  s= s + 2
elif Q2 ==3 :
  r= r+ 2
elif Q2 ==4 :
  g= g + 2
else:
  print('wrong')

if Q3 == 1:
  s= s + 4
elif Q3 ==2 :
  h = h+4
elif Q3 ==3 :
  r= r+ 4
elif Q3 ==4 :
  g= g + 4
else:
  print('wrong')

# print(f'Scores are')
# print(f'Gryffindor - {g}')
# print(f'Ravenclaw - {r}')
# print(f'Hufflepuff - {h}')
# print(f'Slytherin - {s}')
# print(max(s,g,r,h))
if s==7:
  print('Your house is 🐍 Slytherin')
elif g==7:
  print('Your house is 🦁 Gryffindor')
elif r==7:
  print('Your house is 🦅 Ravenclaw')
elif h==7:
  print('Your house is 🦡 Hufflepuff')
  