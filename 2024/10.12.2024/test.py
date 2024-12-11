zeros = 0
localWord = []
array = []
zpositions = []

# Read input file and populate array and zpositions
with open('input.txt', 'r') as file:
    for row, line in enumerate(file):
        localWord = [int(word) for word in line.strip()]  # Strip newlines
        for col, word in enumerate(localWord):
            if word == 0:
                zpositions.append((row, col))  # Store zero positions
        array.append(localWord)

trail = 0  # Initialize trail count globally

# Recursive function to look in all directions
def lookingEverywhere(index, array, visited):
    global trail
    row, col = index

    # If already visited, return
    if index in visited:
        return

    # Mark as visited
    visited.add(index)

    # Check for trail end
    if array[row][col] == 9:
        trail += 1
        return

    # Look up
    if row - 1 >= 0 and array[row - 1][col] - array[row][col] == 1:
        lookingEverywhere((row - 1, col), array, visited)

    # Look left
    if col - 1 >= 0 and array[row][col - 1] - array[row][col] == 1:
        lookingEverywhere((row, col - 1), array, visited)

    # Look down
    if row + 1 < len(array) and array[row + 1][col] - array[row][col] == 1:
        lookingEverywhere((row + 1, col), array, visited)

    # Look right
    if col + 1 < len(array[0]) and array[row][col + 1] - array[row][col] == 1:
        lookingEverywhere((row, col + 1), array, visited)

# Iterate over all zero positions and process
for x in zpositions:
    visited = set()  # Reset visited set for each trail
    lookingEverywhere(x, array, visited)

print("Trail count:", trail)