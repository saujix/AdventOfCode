import re

multiply = 0
with open('input.txt', 'r') as file:
    content = file.read()
    match = re.findall(r"mul\((\d+),(\d+)\)", content)
    for x in match:
        multiply += int(x[0]) * int(x[1])

print(multiply)