# inputs array, returns total combination as an array
def totalCombinations(array):
    bigArray = []

    bigArray.append(array[0]*array[1])
    bigArray.append(array[0]+array[1])

    for i in range(2, len(array) ):
        temp = bigArray
        bigArray = []

        for x in temp:
            bigArray.append(x*array[i])
            bigArray.append(x+array[i])
    return bigArray
sum = 0
count = 0
test = []
with open('input.txt','r') as file:
    bigTests = []
    for line in file.readlines():

        result = int(line.split(":")[0])
        tests = line.split(":")[1]
        
        result = int(result)

        tests = tests.split(" ")
        tests = tests[1:]

        for idx, x in enumerate(tests):

            tests[idx] = int(x)

            if "\n" in x:
                tests[idx] = x.replace("\n","")
                tests[idx] = int(x)

        if result in totalCombinations(tests):
            sum+=result

print(sum)





        


        
        

