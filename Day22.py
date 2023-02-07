with open('22/input.txt') as inputFile:
    rawLines = inputFile.readlines()

myPath = rawLines.pop().strip()
rawLines.pop()

mapLines = []
for line in rawLines:
    newLine = line.strip('\n') + ' ' * (len(rawLines[0]) - len(line))
    mapLines.append(newLine)

currentPosition = [0, 0]
while mapLines[0][currentPosition[1]] == ' ':
    currentPosition[1] += 1

# part one
facing = 0  # facing right
i = 0
while i < len(myPath):
    steps = ''
    if myPath[i] == 'R':
        facing = (facing + 1) % 4
        i += 1
    elif myPath[i] == 'L':
        facing = (facing - 1) % 4
        i += 1
    else:
        while i < len(myPath) and myPath[i].isnumeric():
            steps += myPath[i]
            i += 1
        for j in range(int(steps)):
            k = 1
            if facing == 0:
                if mapLines[currentPosition[0]][(currentPosition[1] + 1) % len(mapLines[currentPosition[0]])] == ' ':
                    while mapLines[currentPosition[0]][(currentPosition[1] + k) % len(mapLines[currentPosition[0]])] == ' ':
                        k += 1
                    if mapLines[currentPosition[0]][(currentPosition[1] + k) % len(mapLines[currentPosition[0]])] == '.':
                        currentPosition[1] = (currentPosition[1] + k) % len(mapLines[currentPosition[0]])
                        continue
                if mapLines[currentPosition[0]][(currentPosition[1] + 1) % len(mapLines[currentPosition[0]])] == '.':
                    currentPosition[1] = (currentPosition[1] + 1) % len(mapLines[currentPosition[0]])
            if facing == 1:
                if mapLines[(currentPosition[0] + 1) % len(mapLines)][currentPosition[1]] == ' ':
                    while mapLines[(currentPosition[0] + k) % len(mapLines)][currentPosition[1]] == ' ':
                        k += 1
                    if mapLines[(currentPosition[0] + k) % len(mapLines)][currentPosition[1]] == '.':
                        currentPosition[0] = (currentPosition[0] + k) % len(mapLines)
                        continue
                if mapLines[(currentPosition[0] + 1) % len(mapLines)][currentPosition[1]] == '.':
                    currentPosition[0] = (currentPosition[0] + 1) % len(mapLines)
            if facing == 2:
                if mapLines[currentPosition[0]][(currentPosition[1] - 1) % len(mapLines[currentPosition[0]])] == ' ':
                    while mapLines[currentPosition[0]][(currentPosition[1] - k) % len(mapLines[currentPosition[0]])] == ' ':
                        k += 1
                    if mapLines[currentPosition[0]][(currentPosition[1] - k) % len(mapLines[currentPosition[0]])] == '.':
                        currentPosition[1] = (currentPosition[1] - k) % len(mapLines[currentPosition[0]])
                        continue
                if mapLines[currentPosition[0]][(currentPosition[1] - 1) % len(mapLines[currentPosition[0]])] == '.':
                    currentPosition[1] = (currentPosition[1] - 1) % len(mapLines[currentPosition[0]])
            if facing == 3:
                if mapLines[(currentPosition[0] - 1) % len(mapLines)][currentPosition[1]] == ' ':
                    while mapLines[(currentPosition[0] - k) % len(mapLines)][currentPosition[1]] == ' ':
                        k += 1
                    if mapLines[(currentPosition[0] - k) % len(mapLines)][currentPosition[1]] == '.':
                        currentPosition[0] = (currentPosition[0] - k) % len(mapLines)
                        continue
                if mapLines[(currentPosition[0] - 1) % len(mapLines)][currentPosition[1]] == '.':
                    currentPosition[0] = (currentPosition[0] - 1) % len(mapLines)

print(1000 * (currentPosition[0] + 1) + 4 * (currentPosition[1] + 1) + facing)

# part two
facing = 0  # facing right
i = 0
while i < len(myPath):
    steps = ''
    if myPath[i] == 'R':
        facing = (facing + 1) % 4
        i += 1
    elif myPath[i] == 'L':
        facing = (facing - 1) % 4
        i += 1
    else:
        while i < len(myPath) and myPath[i].isnumeric():
            steps += myPath[i]
            i += 1