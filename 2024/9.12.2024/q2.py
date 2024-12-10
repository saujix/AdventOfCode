array = []
index = 0
currentCount = 0
spaceData = {}

import time


with open('input.txt','r') as file:
    file= file.read()

for i in range(len(file)):
    if i % 2 != 0:
        for d in range(int(file[i])):  
            array.append(".")
    else:
        for x in range(int(file[i])):
            array.append(index)
            currentCount +=1
        index+=1



def find_dots(data):
    result = []
    start = None
    for i, val in enumerate(data):
        if val == '.':
            if start is None:
                start = i
        else:
            if start is not None:
                result.append((start, i - start))
                start = None
    if start is not None:
        result.append((start, len(data) - start))
    return result




def count_numbers(data):
    counts = {}
    for val in data:
        if val != '.':
            counts[val] = counts.get(val, 0) + 1
    return counts

# empty spaces
dots = find_dots(array)
print(dots)

reversedArray = array[::-1]
number_counts = count_numbers(reversedArray)



cNum = []
for key,value in number_counts.items():
    cNum.append((key,value))

print(f"cNum: {cNum}")
print(f"dots: {dots}")


# c Num is the length of number array [0][0] gives the actual number [0][1] gives the length of that number
# dots [0][0] is the position of the  [0][1] is the space

# cNum_a is equivalent of cNum[0]
# dots_a is equivalent of dots[0]

# we iterate throught the cNum and find the space
# then we iterate throught the spaces to find the correct one


print(array)

# for cnum_a in cNum:
#     for i in range(len(array)):
#         if array[i] == cnum_a[0]:
#             array[i] = "."
            

print(array)
for cNum_a in cNum:
    for dots_a in dots:
        if cNum_a[1] <= dots_a[1]:

            for i in range(cNum_a[1]):  
                array[dots_a[0]+i] = cNum_a[0] 
            
            print(array)
            time.sleep(10)
            dots = find_dots(array)
            #important to delete the index once it is filled other will overwrite
            break
        else:
            pass

# # if word length is less than or equal to space
# if cNum[0][1] <= dots[0][1]:
#     # replace the original position with .
#     array = ["." if x == cNum[0][0] else x for x in array]
#     # this is will start from the space starting index and add the rest word after that
#     for i in range(cNum[0][1]):  
#         array[dots[0][0]+i] = cNum[0][0]

# print(dots[0])
# print(cNum[0])
print(array)



# y[1] is length y[0] is the index (free space)
# v is length x is the numbers (data)

# we will get the index and length of free space i.e. "."