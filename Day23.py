# very slow but works (several seconds for part one, over half an hour for part two)

with open('23/input.txt') as inputFile:
    rawLines = inputFile.readlines()

def checkN(elves, proposed):
    for elf in elves:
        if [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves:
            proposed.append(elf)
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] - 1, elf[1]])
        elif [elf[0] + 1, elf[1] - 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] + 1, elf[1]])
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves and [elf[0] + 1, elf[1] - 1] not in elves:
            proposed.append([elf[0], elf[1] - 1])
        elif [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0], elf[1] + 1])
        else:
            proposed.append(elf)
def checkS(elves, proposed):
    for elf in elves:
        if [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves:
            proposed.append(elf)
        elif [elf[0] + 1, elf[1] - 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] + 1, elf[1]])
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves and [elf[0] + 1, elf[1] - 1] not in elves:
            proposed.append([elf[0], elf[1] - 1])
        elif [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0], elf[1] + 1])
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] - 1, elf[1]])
        else:
            proposed.append(elf)
def checkW(elves, proposed):
    for elf in elves:
        if [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves:
            proposed.append(elf)
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves and [elf[0] + 1, elf[1] - 1] not in elves:
            proposed.append([elf[0], elf[1] - 1])
        elif [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0], elf[1] + 1])
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] - 1, elf[1]])
        elif [elf[0] + 1, elf[1] - 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] + 1, elf[1]])
        else:
            proposed.append(elf)
def checkE(elves, proposed):
    for elf in elves:
        if [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves:
            proposed.append(elf)
        elif [elf[0] - 1, elf[1] + 1] not in elves and [elf[0], elf[1] + 1] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0], elf[1] + 1])
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0] - 1, elf[1]] not in elves and [elf[0] - 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] - 1, elf[1]])
        elif [elf[0] + 1, elf[1] - 1] not in elves and [elf[0] + 1, elf[1]] not in elves and [elf[0] + 1, elf[1] + 1] not in elves:
            proposed.append([elf[0] + 1, elf[1]])
        elif [elf[0] - 1, elf[1] - 1] not in elves and [elf[0], elf[1] - 1] not in elves and [elf[0] + 1, elf[1] - 1] not in elves:
            proposed.append([elf[0], elf[1] - 1])
        else:
            proposed.append(elf)

# part one:
elves = []
for i in range(len(rawLines)):
    for j in range(len(rawLines[i])):
        if rawLines[i][j] == '#':
            elves.append([i, j])

round = 0
while round < 10: # 10 rounds for part one
    proposed = []
    if round % 4 == 0:
        checkN(elves, proposed)
    if round % 4 == 1:
        checkS(elves, proposed)
    if round % 4 == 2:
        checkW(elves, proposed)
    if round % 4 == 3:
        checkE(elves, proposed)
    moved = []
    for i in range(len(elves)):
        if proposed.count(proposed[i]) == 1:
            moved.append(proposed[i])
        else:
            moved.append(elves[i])
    elves = moved
    # print(round)  # for checking progress
    round += 1

minI = elves[0][0]
maxI = elves[0][0]
minJ = elves[0][1]
maxJ = elves[0][1]
for elf in elves:   # find smallest and largest coordinates
    if elf[0] < minI:
        minI = elf[0]
    if elf[0] > maxI:
        maxI = elf[0]
    if elf[1] < minJ:
        minJ = elf[1]
    if elf[1] > maxJ:
        maxJ = elf[1]
# print(minI, maxI, minJ, maxJ)

emptyTiles = 0  # counting empty tiles
for i in range(minI, maxI + 1):
    for j in range(minJ, maxJ + 1):
        if [i, j] not in elves:
            emptyTiles += 1
print(emptyTiles)

# part two:
elves = []
for i in range(len(rawLines)):
    for j in range(len(rawLines[i])):
        if rawLines[i][j] == '#':
            elves.append([i, j])

round = 0
while round < 1000: # 1000 is enough for my input
    proposed = []
    if round % 4 == 0:
        checkN(elves, proposed)
    if round % 4 == 1:
        checkS(elves, proposed)
    if round % 4 == 2:
        checkW(elves, proposed)
    if round % 4 == 3:
        checkE(elves, proposed)
    moved = []
    for i in range(len(elves)):
        if proposed.count(proposed[i]) == 1:
            moved.append(proposed[i])
        else:
            moved.append(elves[i])
    if elves == moved:  # only for part two
        print(round)
        break
    elves = moved
    # print(round)  # for checking progress
    round += 1