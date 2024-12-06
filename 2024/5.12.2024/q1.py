# function to input stuff , gives conditions array, cases array
with open('input.txt', 'r') as file:
    lines = file.readlines()
    cases = []
    conditions = []

    for line in lines:
        if "|" in line:
            condition = line.split("|")
            condition[0] = int(condition[0])
            condition[1] = int(condition[1])
            conditions.append(condition)
        elif "," in line:
            caseArray = []
            icases = line.split(",")
            for case in icases:
                caseArray.append(int(case))
            cases.append(caseArray)

array = [10, 20, 30, 40, 50]

# this function finds the last occurence, returns index of last occurence
def lastOccurence(array, num):
    for i in range(len(array) - 1, -1, -1):
        if array[i] == num:
            return i
    return None


actualValid = []
sum1 = 0
length = 0
notNoneIndex = 0
invalidCounter = 0
invalidArray = []

caseCounter = 0
for case in cases:
    caseCounter +=1
    for index, condition in enumerate(conditions):

        last_index = lastOccurence(case, condition[0])

        if last_index is not None:
            leftPart = case[:last_index]
            rightPart = case[last_index+1:]

            if (
                condition[1] in leftPart
            ):
                invalid = 1

        if index == len(conditions) - 1:
            if invalid == 0:
                sum1 += case[len(case)//2]
                invalid = 0
            elif invalid == 1:
                invalidArray.append(case)


for x in invalidArray:
    print(x)
