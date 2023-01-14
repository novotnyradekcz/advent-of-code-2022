with open('21/input.txt') as inputFile:
    rawLines = inputFile.readlines()

newLines = []
for line in rawLines:
    newLines.append(line.split())
for line in newLines:
    line[0] = line[0].strip(':')

# part one
orderedLines = []
operationsLines = []
for line in newLines:
    if any(i.isdigit() for i in line):
        orderedLines.append(line)   # picking out lines with number assignment
    else:
        operationsLines.append(line)    # the rest of the lines = operations with variables

for n in range(41): # 41 iterations are needed to reorder all lines
    for operationsLine in operationsLines:
        if operationsLine not in orderedLines and operationsLine[1] in list(next(zip(*orderedLines))) and operationsLine[3] in list(next(zip(*orderedLines))):
            orderedLines.append(operationsLine)

with open('21/output.py', 'w') as outputFile:  # printing out the file to be executed in python to print the result
    for line in orderedLines:
        outputFile.write(line[0])
        outputFile.write(' = ')
        outputFile.write(line[1])
        if len(line) > 2:
            outputFile.write(line[2])
            outputFile.write(line[3])
        outputFile.write('\n')
    outputFile.write('print(root)')
exec(open("21/output.py").read())

# part two
# output2.py manually edited, == instead of + at root's line
for x in range(3093175982000, 3093175983000):   # range adjusted manually
    exec(open("21/output2.py").read())
    # if x % 100 == 0:
        # print(lttc, pfjc)   # numbers to compare to find the right range
    if root:
        print(x)