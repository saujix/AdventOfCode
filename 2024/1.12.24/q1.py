leftarray=[]
rightarray=[]

with open("input.txt","r") as file:
    i = 0
    for line in file:
        leftarray.append(line.split("   ")[0])
        rightarray.append(line.split("   ")[1])
        i += 1


len = len(leftarray)
i = 0
k = 0

leftarray.sort()
rightarray.sort()

dist= 0
i =0

while i<len:
    dist += abs(int(leftarray[i])-int(rightarray[i]))
    i+=1
        
print(dist)   