with open('input.txt','r') as file:
    file= file.read()

array = []
index = 0
for i in range(len(file)):
    if i % 2 != 0:
        for d in range(int(file[i])):  
            array.append(".")
    else:
        for x in range(int(file[i])):
            array.append(index)
        index+=1

for i in range(len(array)-1 , -1, -1):
    if array[i] != ".":
        array[array.index(".")] = array[i]
        array[i] ="."


sum = 0
for i, num in enumerate(array):
    if num != ".":
        sum1 = int(num) * (i - 1)
        sum+= sum1

print(sum)
