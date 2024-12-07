import time

localLine = []
dataArray = []

with open('input.txt', 'r') as file:
    file = file.read()
    data = file.split("\n")
    for line in data:
        localLine = []
        for word in line:
            localLine.append(word)
        dataArray.append(localLine)
    data = dataArray


def getLocation(pointer, data):
    for col, line in enumerate(data):
        for row, word in enumerate(line):
            if word == pointer:
                return col, row

inGrid = True

directions = {
    "^": [-1, 0],  # moving up
    ">": [0, 1],   # moving right
    "v": [1, 0],   # moving down
    "<": [0, -1]   # moving left
}

def pointerChange(pointer):
    if pointer == "^":
        return ">"
    elif pointer == ">":
        return "v"
    elif pointer == "v":
        return "<"
    elif pointer == "<":
        return "^"


count = 0
step = 1
pointer = "^"

first, last = getLocation(pointer, data)

while inGrid:
    
    nextX = first + directions[pointer][0]
    nextY = last + directions[pointer][1]

    
    if nextX < 0 or nextY < 0 or nextX >= len(data) or nextY >= len(data[0]):
        break

    
    if data[nextX][nextY] == "#":

        pointer = pointerChange(pointer)  



    elif data[nextX][nextY] == ".":

        count += 1
        data[nextX][nextY] = "O"  
        first, last = nextX, nextY
    
    elif data[nextX][nextY] == "O":

        first, last = nextX, nextY  

    
    if (
        (first == len(data) - 1 and pointer == "v") or
        (last == len(data[0]) - 1 and pointer == ">") or
        (first == 0 and pointer == "^") or
        (last == 0 and pointer == "<")
    ):
        count += 1 # because one step will be the one in which we jump out the grid
        inGrid = False
        
    time.sleep(0.005)
    print("\033[H\033[J")
    for x in data:
        print(''.join(x))
    

print(f"currentSteps : {count}, currentDirection : {pointer}")

