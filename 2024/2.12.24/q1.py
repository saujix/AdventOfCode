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

while(i < len(totalArray)):
#while(i < 1):
    
    #nth element of the array, this is the element we are working with
    currentArray = totalArray[i]
    j = 0
    

    #gets the difference of consecutive elements and appends them to the dif array
    while(j<len(currentArray)-1):
        dif.append(int(currentArray[j+1])-int(currentArray[j]))
        j+=1
    

    #this is to check the diff nature between different elements
    for t in dif:
        if t>0:
            pos+=1
        elif t<0:
            neg+=1
    
    status_unsafe=0

    #
    if (pos > 0) != (neg > 0): 
        for t in dif:
            if abs(t) not in range(1, 4):
                status_unsafe +=1
    
    if status_unsafe>0:
        unsafe+=1
    else:
        safe+=1

    #resetting
    pos=0
    neg=0
    dif=[]
    status_unsafe=0
    
    i+=1
print(safe)
print(unsafe)