with open('9/input.txt') as inputFile:
    rawLines = inputFile.readlines()

lines = []
for line in rawLines:
    lines.append(line.split())

def move(position):
    tailPositions = [[0, 0]]
    for line in lines:
        for i in range(int(line[1])):
            # move head
            if line[0] == 'U':
                position[0][0] += 1
            if line[0] == 'D':
                position[0][0] -= 1
            if line[0] == 'R':
                position[0][1] += 1
            if line[0] == 'L':
                position[0][1] -= 1
            # adjust tails
            for x in range(len(position) - 1):
                if position[x + 1][0] == position[x][0]:
                    if position[x + 1][1] < position[x][1] - 1:
                        position[x + 1] [1] += 1
                    if position[x + 1][1] > position[x][1] + 1:
                        position[x + 1] [1] -= 1
                if position[x + 1][1] == position[x][1]:
                    if position[x + 1][0] < position[x][0] - 1:
                        position[x + 1] [0] += 1
                    if position[x + 1][0] > position[x][0] + 1:
                        position[x + 1] [0] -= 1
                if position[x + 1][0] != position[x][0] and position[x + 1][0] != position[x][0] and (position[x + 1][0] - position[x][0])**2 + (position[x + 1][1] - position[x][1])**2 > 2:
                    if position[x + 1][0] > position[x][0]:
                        position[x + 1][0] -= 1
                    else:
                        position[x + 1][0] += 1
                    if position[x + 1][1] > position[x][1]:
                        position[x + 1][1] -= 1
                    else:
                        position[x + 1][1] += 1
            # ad tail position to list
            if [position[-1][0], position[-1][1]] not in tailPositions:
                tailPositions.append([position[-1][0], position[-1][1]])
    return tailPositions

# part one:
position1 = [[0, 0], [0, 0]]
print(len(move(position1)))

# part two:
position2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
print(len(move(position2)))