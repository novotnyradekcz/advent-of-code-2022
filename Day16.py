import random

with  open('16/input.txt') as inputFile:
    rawLines = inputFile.readlines()

splitLines = []
for line in rawLines:
    splitLines.append(line.split())

dictLines = {}
for line in splitLines:
    dictLines[line[1]] = []
    dictLines[line[1]].append(int(line[4].strip('rate=;')))
    for j in range(9, len(line)):
        dictLines[line[1]].append(line[j].strip(','))

# generate paths
paths = []
for i in range(10000): # 10000 is enough to solve part one
    paths.append(['AA'])
    for j in range(30):
        paths[i].append(dictLines[paths[i][-1]][random.randint(1, len(dictLines[paths[i][-1]]) - 1)])
        while len(paths[i]) > 2 and len(dictLines[paths[i][-2]]) > 2 and paths[i][-1] == paths[i][-3]:
            paths[i].pop()
            paths[i].append(dictLines[paths[i][-1]][random.randint(1, len(dictLines[paths[i][-1]]) - 1)])

# for part two
# pathsE = []
# for i in range(10000000): # 10000000 was not enough to solve part two
#     pathsE.append(['AA'])
#     for j in range(30):
#         pathsE[i].append(dictLines[pathsE[i][-1]][random.randint(1, len(dictLines[pathsE[i][-1]]) - 1)])
#         while len(pathsE[i]) > 2 and len(dictLines[pathsE[i][-2]]) > 2 and pathsE[i][-1] == pathsE[i][-3]:
#             pathsE[i].pop()
#             pathsE[i].append(dictLines[pathsE[i][-1]][random.randint(1, len(dictLines[pathsE[i][-1]]) - 1)])
# random.shuffle(pathsE)

highest = 0
for n in range(len(paths)):
    time = 30
    # part two:
    # time = 26
    pressure = 0
    room = 'AA'
    roomE = 'AA'
    opened = []
    i = 0
    while time > 1:
        i += 1
        roomCheck = 0
        if dictLines[room][0] >= 9 and room not in opened:  # 8 works for part one
            roomCheck = 1
            opened.append(room)
            time -= 1
            pressure += time * dictLines[room][0]
        # part two - elephant
        # if dictLines[roomE][0] >= 4 and roomE not in opened:
        #     opened.append(roomE)
        #     if roomCheck == 0:
        #         time -= 1
        #     pressure += time * dictLines[roomE][0]
        # room = dictLines[room][random.randint(1, len(dictLines[room]) - 1)]
        if time == 1:
            break
        room = paths[n][i]
        # part two - elephant
        # roomE = pathsE[n][i]
        time -= 1
    if pressure > highest:
        highest = pressure
        highestOpened = opened
print(highest, highestOpened)

# part two never quite worked, solved in excel