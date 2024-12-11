zeros = 0
localWord = []
array = []
zpositions = []

# Read input file and prepare the grid and zpositions
with open('input.txt', 'r') as file:
    for row, line in enumerate(file):
        for col, word in enumerate(line):
            if word == "\n":
                pass
            else:
                localWord.append(int(word))
            if word == "0":
                zpositions.append((row, col))
        array.append(localWord)
        localWord = []

unique_paths = set()

def lookingEverywhere(index, array, visited, path):
    row, col = index

    if index in visited:
        return

    visited.add(index)

    path.append(index)

    if array[row][col] == 9:
        print(path)
        unique_paths.add(tuple(path))
        path.pop()
        visited.remove(index)
        return

    if row - 1 >= 0 and array[row - 1][col] - array[row][col] == 1:
        lookingEverywhere((row - 1, col), array, visited, path)

    if col - 1 >= 0 and array[row][col - 1] - array[row][col] == 1:
        lookingEverywhere((row, col - 1), array, visited, path)

    if row + 1 < len(array) and array[row + 1][col] - array[row][col] == 1:
        lookingEverywhere((row + 1, col), array, visited, path)

    if col + 1 < len(array[0]) and array[row][col + 1] - array[row][col] == 1:
        lookingEverywhere((row, col + 1), array, visited, path)

    path.pop()
    visited.remove(index)

for x in zpositions:
    visited = set()  # Reset visited for each new path
    lookingEverywhere(x, array, visited, [])

print(len(unique_paths))