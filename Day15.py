import numpy as np

with  open('15/input.txt') as inputFile:
    rawLines = inputFile.readlines()

splitLines = []
for line in rawLines:
    splitLines.append(line.split())
numberLines = []
for line in splitLines: # extract only coordinates
    numberLines.append([int(line[2].strip('x=,')), int(line[3].strip('y=:')), int(line[8].strip('x=,')), int(line[9].strip('y='))])

minX = 0
minY = 0
maxX = 0
maxY = 0
for line in numberLines:    # find minimum and maximum coordinates
    if line[0] < minX:
        minX = line[0]
    if line[2] < minX:
        minX = line[2]
    if line[0] > maxX:
        maxX = line[0]
    if line[2] > maxX:
        maxX = line[2]
    if line[1] < minY:
        minY = line[1]
    if line[3] < minY:
        minY = line[3]
    if line[1] > maxY:
        maxY = line[1]
    if line[3] > maxY:
        maxY = line[3]

# part one:
y = 2000000
counter = 0
closeLines = [] 
for line in numberLines:    # just selecting the sensors and beacons that affect the y = 2000000 row
    distance = abs(line[0] - line[2]) + abs(line[1] - line[3])
    if (line[1] <= y and line[1] + distance >= y) or (line[1] >= y and line[1] - distance <= y):
        closeLines.append(line)

isItThere = np.full((1, 8000000), False)

x = np.array(range(-2000000, 6000000))
for line in numberLines:
    distance = abs(line[0] - line[2]) + abs(line[1] - line[3])
    isItThere = np.logical_or(isItThere, (abs(line[0] - x) + abs(line[1] - y) <= distance))
print(np.count_nonzero(isItThere == True) - 1)
# need to subtraact 1 from the result as one spot in the y = 2000000 row is occupied by a beacon

# part two:
# output for drawing a graph and manually inspecting in excel
with  open('15/output.txt', 'w') as outputFile:
    for line in numberLines:
        distance = abs(line[0] - line[2]) + abs(line[1] - line[3])
        outputFile.write(f'{line[0]}, {line[1] - distance}\n')
        outputFile.write(f'{line[0] - distance}, {line[1]}\n')
        outputFile.write(f'{line[0] + distance}, {line[1]}\n')
        outputFile.write(f'{line[0]}, {line[1] + distance}\n')

# checking small sections based on excel check
x = np.array(range(3100000, 3110000))
for y in range(3385000, 3395000):
    isItThere = np.full((1, 10000), False)
    for line in numberLines:
        distance = abs(line[0] - line[2]) + abs(line[1] - line[3])
        isItThere = np.logical_or(isItThere, (abs(line[0] - x) + abs(line[1] - y) <= distance))
    if np.count_nonzero(isItThere == False) != 0:
        for i in range(10000):
            if (isItThere[0, i] == False):  # saving the coordinates of possible beacon location
                resX = 3100000 + i
                resY = y
print(4000000 * resX + resY)