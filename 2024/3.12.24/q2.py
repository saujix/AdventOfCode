import re

multiply = 0
final=[]

def chunksOp(string):
    sum = 0
    match = re.findall(r"mul\((\d+),(\d+)\)", string)
    for x in match:
        sum += int(x[0]) * int(x[1])
    return sum


with open('input.txt', 'r') as file:
    t = file.read().split("do()")
    for x in t:
        index = x.find("don't()")
        if index != -1:
            x=x[:index]
        multiply+=chunksOp(x)


        

