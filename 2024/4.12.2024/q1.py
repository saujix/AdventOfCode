
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

height = len(dataArray[0])
width=len(dataArray)

for x in range(width):
    for y in range(height):
        for dx,dy in operations:
            if (0 <= x + 3 * dx < width and
                0 <= y + 3 * dy < height and
                dataArray[x][y] =="X" and 
                dataArray[x+dx][y+dy] =="M" and 
                dataArray[x+2*dx][y+2*dy]=="A" and 
                dataArray[x+3*dx][y+3*dy]=="S"):
                    count+=1
            
            
print(count)