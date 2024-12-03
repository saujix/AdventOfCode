import re

text = ''
i =0
okArray=[]


with open('input.txt','r') as file:
    data=file.read().split("mul")

def findBrackets(string):
    l = len(string)
    if string[0] == "(":
        text = re.search(r'\((.*?)\)', string)
        if text:
            return text.group(1)


array = []
for x in data:
    try:
        array.append(findBrackets(x).split(","))
    except:
        pass


multiply = 0
for x in array:
    try:
        multiply += int(x[0])*int(x[1])
        print(x)
    except:
        pass



    

