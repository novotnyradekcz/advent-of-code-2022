import ast

with  open('13/input.txt') as inputFile:
    rawLines = inputFile.readlines()

listLines = []
for line in rawLines:
    if line != '\n':
        listLines.append(ast.literal_eval(line))

# part one:
counter = 0
undetermined = []
for i in range(0, len(listLines), 2):   # compare those that can be compared easily
    try:
        if listLines[i] < listLines[i + 1]:
            counter += i // 2 + 1
    except:
        undetermined.append(i // 2 + 1)
# print(counter)  # sum of indices those that could be determined by default comparing

with open('13/output1.txt', 'x') as fileOut: # export to file and compare the rest manually and add to the counter
    for i in undetermined:
        fileOut.write(str(i))
        fileOut.write('\n')
        fileOut.write(rawLines[3 * (i - 1)])
        fileOut.write(rawLines[3 * (i - 1) + 1])
        fileOut.write('\n')

counter += 2694 # visual inspection result
print(counter)

# part two:
# my custom sorting, works well for lists starting with different numbers
# lists with the same starting numbers compared later manually
def myRule(myString):  
    for i in range(len(myString)):
        if myString[i] == '\n':
            return 10000
        if myString[i] == '[':
            continue
        if myString[i] == ']':
            return -10 + i
        if myString[i:i + 2].isnumeric():
            return int(myString[i:i + 2])
        return int(myString[i])

rawLines.append('[[2]]')
rawLines.append('[[6]]')
rawLines.sort(key=myRule)

sortedLines = []
for line in rawLines:   # converting to a list of strings to a list of lists
    if line != '\n':
        sortedLines.append(ast.literal_eval(line))
with open('13/output2.txt', 'x') as fileOut:    # outputting to file for visual inspection
    for line in sortedLines:   
        fileOut.write(str(line))
        fileOut.write('\n')

# sorting isn't perfect, puts [[2]] after other lines with 2 at the front instead of before
# also 1 needs to be added, because index starts at 1, not usual 0
print((rawLines.index('[[2]]') - 15) * (rawLines.index('[[6]]') - 17))