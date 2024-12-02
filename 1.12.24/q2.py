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

i = 0
sum =0

t=0
for x in leftarray:
    t=0
    for y in rightarray:
        if int(y) == int(x):
            t+=1
            sum+=int(x)
    print(f"{x} x {t}")
        
print(sum)   