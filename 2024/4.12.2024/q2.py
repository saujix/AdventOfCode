dataArray=[]
with open("input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        dataArray.append(line.strip())

width = len(dataArray[0])
height = len(dataArray)


count = 0
for y in range(height):
    for x in range(width):
        if (
            (x + 1 < width and
            y + 1 < height and
            0 <= x - 1 and
            0 <= y - 1 and
            dataArray[y][x] == "A")     
        ):
            uL = dataArray[y-1][x-1]
            uR = dataArray[y-1][x+1]
            dL = dataArray[y+1][x-1]
            dR = dataArray[y+1][x+1]

            t=0

            if (
                uL == dL =="M" and
                uR == dR == "S"
            ):
                count +=1
                t=1

            if (
                uR == uL == "M" and
                dL == dR == "S"
            ):
                count+=1
                t=1

            if (
                uR == dR == "M" and
                dL == uL =="S"
            ):
                count +=1
                t=1
            
            if (
                dL == dR =="M" and
                uR == uL == "S"
            ):
                count +=1
                t = 1
            
print(count)


            

            