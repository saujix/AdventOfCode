totalArray = []
sampleArray=[]

with open('input.txt', "r") as file:
    for line in file:
        sampleArray = line.split(" ")
        sampleArray[-1] = sampleArray[-1].replace("\n","")
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

        
totalLength=len(totalArray)
l=0
safe=0
inorder = 0

while(l<totalLength):
    if order(totalArray[l]):
        inorder+=1
        if isSafe(totalArray[l])==None:
            safe+=1
    l+=1
    
print(safe)




