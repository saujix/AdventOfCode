totalArray = []
sampleArray=[]
abnormalArray=[]

with open('input.txt', "r") as file:
    for line in file:
        sampleArray = list(map(int, line.strip().split(" ")))  # better to process it this way and cast it directly to ints
        totalArray.append(sampleArray)


def isSafe(array):
    i = 0
    while i<len(array)-1:
        t = int(array[i+1]) - int(array[i])
        if t<-3 or t>3 or t==0:
            return False
        i+=1 

def order(array):
    if array != sorted(array) and array != sorted(array,reverse= True):
       return False
    return True

def newArray(index, array):
    i=0
    newArray=[]
    while(i<len(array)):
        if i == index:
            pass
        else:
            newArray.append(array[i])
        i+=1
    return newArray


def lenientIssafe(array):
    length = len(array)
    t = array
    i=0
    safe=0
    while(i<length):
        array=t
        array=newArray(i,array)
        if order(array):
            if isSafe(array)==None:
                return True
        i+=1 

safe=0
for x in totalArray:
    if lenientIssafe(x):
        safe+=1    

print(safe)




