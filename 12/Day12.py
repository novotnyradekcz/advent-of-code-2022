import random

with open('12/input.txt') as inputFile:
    rawLines = inputFile.readlines()

letterLines = []
for line in rawLines:
    letterLines.append(line.strip())

myStart = []
myEnd = []
numberLines = []
for i in range(len(letterLines)):
    numberLines.append([])
    for j in range(len(letterLines[i])):
        if letterLines[i][j] == 'S':
            myStart.append(i)
            myStart.append(j)
            numberLines[i].append(1)
        elif letterLines[i][j] == 'E':
            myEnd.append(i)
            myEnd.append(j)
            numberLines[i].append(26)
        else:
            numberLines[i].append(ord(letterLines[i][j]) - 96)
# print(numberLines)

print(myStart)
print(myEnd)
pathLength = 0
y, x = myStart
while [y, x] != myEnd:
    direction = random.randint(0, 3)
    oldX = x
    oldY = y
    if direction == 0 and x < len(numberLines[y]) - 1:
        if numberLines[y][x] > numberLines[y][x + 1] - 2:
            x += 1
    if direction == 1 and y < len(numberLines) - 1:
        if numberLines[y][x] > numberLines[y + 1][x] - 2:
            y += 1
    if direction == 2 and x > 0:
        if numberLines[y][x] > numberLines[y][x - 1] - 2:
            x -= 1
    if direction == 3 and y > 0:
        if numberLines[y][x] > numberLines[y - 1][x] - 2:
            y -= 1
    if [x, y] != [oldX, oldY]:
        pathLength += 1
print(pathLength)

# doesn't work, solved in excel by manually tracing path