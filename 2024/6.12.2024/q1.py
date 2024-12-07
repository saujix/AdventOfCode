grid= []
with open("input.txt", "r") as file:
    for x in file.readlines():
        grid.append(x.replace("\n",""))

inGrid = True

def getPosition(grid, word):
    r = 0
    c = 0

    for x in grid:
        for y in x:
            if y == word:
                return r, c
            r+=1
        c+=1
        r=0

x = 0
y = 0
while inGrid:
    r, c = getPosition(grid, "^")
    while grid[c - x][r - y]:
        print(grid[c - x][r - y])
        x-=1
    inGrid = False

# grid[column][row]



