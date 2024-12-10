import itertools

with open('input.txt','r') as file:
    lines = file.readlines()

characters = {}

for row, line in enumerate(lines):
    for col, word in enumerate(line):
        if word == ".":
            pass
        elif word != "\n":
            if word in characters:
                characters[word]+= [(col , row)]
            else:
                characters[word] = [(col, row)]

# input current, point1, point2
# so we got the distance thing setup

def isEqualDistant(current, point1, point2):
    distance1 = ((point1[0]-current[0])**2 + (point1[1]-current[1])**2)
    distance2 = ((point2[0]-current[0])**2 + (point2[1]-current[1])**2)
    if distance1 == distance2:
        return True

# for key, value in characters.items():
#     for x in value:
#         print(f"row = {x[0]}, col = {x[1]}")

#itterating thrught the rows and columns

array1 = [1,2,3,4,5,3]
array2 = [2,3,5,7,8,9]
combinations = itertools.combinations(array1,array2)

for combo in combinations:
    print(combo)
for row, line in enumerate(lines):
    for col, word in enumerate(line):

        point1 = 13, 0
        point2 = 14,2

        current = row,col

        if word == ".":
            if isEqualDistant(current, point1, point2):
                print(current)
            
            
            

# so i am working on a strategy in which we take the co-ordinates
# so we have to just find point which have twice the distance from one point than the other
# we do this by iterating thought the loop with row and col in hand, we put it in a formula 
# if it satisifes the condition we add it into a list of antinodes
# we then 

