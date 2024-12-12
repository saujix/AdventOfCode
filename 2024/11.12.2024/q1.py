# so apparently caching a function means it just gets called once and next time just gives the return value as being saved
from functools import cache

with open('input.txt', 'r') as file:
    file = file.read()

stones = [int(x) for x in file.split()]

@cache
def count(stone, steps) :

    if steps == 0:
        return 1 # see here it didn't call count again, it just stopped
    
    if stone == 0:
        return count(1, steps - 1)
    
    string = str(stone)
    length = len(string)

    if length % 2 == 0:
        return count( int(string[ :length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
    
    return count (stone * 2024, steps - 1)

sum = 0
for stone in stones:
    sum += count (stone , 25)
print(sum)