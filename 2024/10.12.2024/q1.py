zeros = 0
localWord = []
array = []
zpositions = []
with open('input.txt','r') as file:
    for row,line in enumerate(file):
        for col,word in enumerate(line):
            if word == "\n":
                pass
            else:
                localWord.append(int(word))
            if word == "0":
                zpositions.append((row,col))
        array.append(localWord)
        localWord = []


# index [1] should be row
# index [0] should be col


trail = 0
def lookingEverywhere(index, array,visited):

    global trail  #this is to ensure that everytime it's called we dont create a new variant
    row,col = index

    if index in visited:
        return

    visited.add(index) # so we dont end up on same node again


    if array[row][col] == 9:
        trail += 1
        return
    

    if (row - 1 >= 0 and array[row - 1][col] - array[row][col] == 1):
        lookingEverywhere((row-1,col), array, visited)

    if (col - 1 >= 0 and array[row][col - 1] - array[row][col] == 1): 
        lookingEverywhere((row ,col - 1),array, visited)

    if (row + 1 < len(array) and array[row + 1][col] - array[row][col] == 1):
        lookingEverywhere((row + 1,col),array, visited)

    if (col + 1 < len(array[0]) and array[row][col + 1] - array[row][col] == 1):
        lookingEverywhere((row ,col + 1),array, visited)

    
for x in zpositions:
    visited = set()
    lookingEverywhere(x, array, visited)

print(trail)
