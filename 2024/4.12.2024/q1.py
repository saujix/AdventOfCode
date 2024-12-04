import re

dataArray=[]
with open("input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        dataArray.append(line.strip())

count = 0

def lookUp(data, x, y):
    try:
        if data[x][y] =="X" and data[x][y-1] =="M" and data[x][y-2]=="A" and data[x][y-3]=="S":
            return 1
    except:
        pass
    return 0

def lookDown(data, x, y):
    try:
        if data[x][y] =="X" and data[x][y+1] =="M" and data[x][y+2]=="A" and data[x][y+3]=="S":
            return 1
    except:
        pass
    return 0

def lookRight(data, x, y):
    try:
        if data[x][y] =="X" and data[x+1][y] =="M" and data[x+2][y]=="A" and data[x+3][y]=="S":
            return 1
    except:
        pass
    return 0

def lookLeft(data, x, y):
    try:
        if data[x][y] =="X" and data[x-1][y] =="M" and data[x-2][y]=="A" and data[x-3][y]=="S":
            return 1
    except:
        pass
    return 0

def looktopLeft(data, x, y):
    try:
        if data[x][y] =="X" and data[x-1][y-1] =="M" and data[x-2][y-2]=="A" and data[x-3][y-3]=="S":
            return 1
    except:
        pass
    return 0

def looktopRight(data, x, y):
    try:
        if data[x][y] =="X" and data[x+1][y-1] =="M" and data[x+2][y-2]=="A" and data[x+3][y-3]=="S":
            return 1
    except:
        pass
    return 0

def lookbottomLeft(data, x, y):
    try:
        if data[x][y] =="X" and data[x-1][y+1] =="M" and data[x-2][y+2]=="A" and data[x-3][y+3]=="S":
            return 1
    except:
        pass
    return 0

def lookbottomRight(data, x, y):
    try:
        if data[x][y] =="X" and data[x+1][y+1] =="M" and data[x+2][y+2]=="A" and data[x+3][y+3]=="S":
            return 1
    except:
        pass
    return 0

x = 0
y = 0

for y in range(140):
    for x in range(140):
        count += lookUp(dataArray,x,y)
        count+= lookDown(dataArray,x,y)
        count+= lookRight(dataArray,x,y)
        count+= lookLeft(dataArray,x,y)
        count+=looktopLeft(dataArray, x, y)
        count+=looktopRight(dataArray, x, y)
        count+=lookbottomLeft(dataArray, x, y)
        count+=lookbottomRight(dataArray, x, y)
print(count)


    


