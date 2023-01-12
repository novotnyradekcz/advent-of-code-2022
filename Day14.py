with  open('14/input.txt') as inputFile:
    rawLines = inputFile.readlines()

splitLines = []
for line in rawLines:
    splitLines.append(line.strip().split(' -> '))

cave = [['.' for i in range(400)] for j in range(200)]  # creating empty cave

for line in splitLines: # adding rock formations
    x = 0
    y = 0
    i = 0
    while i < len(line) - 1:
        if i == 0:
            start = line[i].split(',')
            x = int(start[0])
            y = int(start[1])
        next = line[i + 1].split(',')
        if x == int(next[0]):
            if y < int(next[1]):
                while y < int(next[1]):
                    cave[y][x - 300] = '#'
                    y += 1
            else:
                while y > int(next[1]):
                    cave[y][x - 300] = '#'
                    y -= 1
        elif y == int(next[1]):
            if x < int(next[0]):
                while x < int(next[0]):
                    cave[y][x - 300] = '#'
                    x += 1
            else:
                while x > int(next[0]):
                    cave[y][x - 300] = '#'
                    x -= 1
        i += 1
        if i == len(line) - 1:
            cave[y][x - 300] = '#'

# adding sand origin point
cave[0][200] = '+'

# adding falling sand
sandYX = [0, 200]
sandUnits = 0

# part one:
while sandYX[0] != 199:
    if cave[sandYX[0] + 1][sandYX[1]] == '.':
        sandYX[0] += 1
    elif cave[sandYX[0] + 1][sandYX[1] - 1] == '.':
        sandYX[0] += 1
        sandYX[1] -= 1
    elif cave[sandYX[0] + 1][sandYX[1] + 1] == '.':
        sandYX[0] += 1
        sandYX[1] += 1
    else:
        cave[sandYX[0]][sandYX[1]] = 'o'
        sandUnits += 1
        sandYX[0] = 0
        sandYX[1] = 200
print(sandUnits)    # print out the result - number of sand units before sand starts falling into abyss

# part two:
sandYX = [0, 200]   # resetting sand
for i in range(400): # adding floor
    cave[174][i] = '#'

while cave[0][200] != 'o':
    if cave[sandYX[0] + 1][sandYX[1]] == '.':
        sandYX[0] += 1
    elif cave[sandYX[0] + 1][sandYX[1] - 1] == '.':
        sandYX[0] += 1
        sandYX[1] -= 1
    elif cave[sandYX[0] + 1][sandYX[1] + 1] == '.':
        sandYX[0] += 1
        sandYX[1] += 1
    else:
        cave[sandYX[0]][sandYX[1]] = 'o'
        sandUnits += 1
        sandYX[0] = 0
        sandYX[1] = 200
print(sandUnits)    # print out the result - number of sand units that come to rest before the source is blocked