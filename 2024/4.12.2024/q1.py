import re

dataArray=[]
with open("input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        dataArray.append(line.strip())

count = 0
operations = [[1,0],
              [0,1],
              [1,1],
              [-1,0],
              [0,-1],
              [-1,-1],
              [-1,1],
              [1,-1]
              ]
x = 0
y = 0

for x in range(140):
    for y in range(140):
        for i in operations:
            try:
                if dataArray[x][y] =="X" and dataArray[x+i[0]][y+i[1]] =="M" and dataArray[x+2*(i[0])][y+2*(i[1])]=="A" and dataArray[x+3*(i[0])][y+3*(i[1])]=="S":
                    count+=1
            except:
                pass
        
print(count)