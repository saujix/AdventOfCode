totalArray = []
sampleArray=[]

with open('input.txt', "r") as file:
    for line in file:
        sampleArray = line.split(" ")
        sampleArray[-1] = sampleArray[-1].replace("\n","")
        totalArray.append(sampleArray)

totalLength = len(totalArray)
i = 0

unsafe = 0
safe = 0
dif=[]
findif=[]
pos=0
neg=0

#gets the difference of consecutive elements and appends them to the dif array
def diffArray(array):
    j = 0
    while(j<len(array)-1):
        dif.append(int(array[j+1])-int(array[j]))
        j+=1
    return dif

def checkArray(array):
    pos=0
    neg=0
    for t in array:
        if t>0:
            pos+=1
        elif t<0:
            neg+=1
    return pos, neg

def checkunSafe(pos, neg):
    status_unsafe=0
    if (pos > 0) != (neg > 0): 
        for t in dif:
            if abs(t) not in range(1, 4):
                status_unsafe +=1
    return status_unsafe




while(i < len(totalArray)):

    currentArray = totalArray[i]
    
    dif = diffArray(currentArray)

    pos=checkArray(dif)[0]
    neg=checkArray(dif)[1]   

    if checkunSafe(pos,neg)==0:
        safe+=1
        
  
    i+=1
print(safe)
print(unsafe)