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

# we have conditions array and cases array now

def splittingList(array, condition):
    splitted = []
    constList = []
    for i in array:
        if i == condition:
            splitted.append(constList)
            constList = []
        else:
            constList.append(i)
    # for last constList as it was never appended
    if constList:
        splitted.append(constList)

    return splitted

sample_array = [12, 5, 3, 19, 3, 8, 25, 14, 9, 21]

print(splittingList(sample_array, 12))

def merge_except_last(array):
    merged = []
    for x in array[:-1]:
        merged.extend(x)

    merged.append(array[-1])

    return merged

def conditionTest(case, condition):
    count = 0
    
    blocks = splittingList(case, condition[0])
    mergedExceptLast = merge_except_last(blocks)

    if len(mergedExceptLast) > 1:
        # Ensure that mergedExceptLast[1] is an iterable (like a list)
        if (condition[1] not in [mergedExceptLast[1]] and
            condition[1] in mergedExceptLast[0]):
            count += 1
    
    if count > 0:
        return 0
    else:
        return 1

valid = 0
actualValid = 0

# for case in cases:
#     valid = 0  # Reset valid for each case
#     for condition in conditions:
        

# print(actualValid)