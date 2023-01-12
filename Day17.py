with  open('17/input.txt') as inputFile:
    arrows = inputFile.read()

def createRock(shape, maxHeight):
    rock_shapes = {
        0: [[maxHeight + 4, 2], [maxHeight + 4, 3], [maxHeight + 4, 4], [maxHeight + 4, 5]],
        1: [[maxHeight + 4, 3], [maxHeight + 5, 2], [maxHeight + 5, 3], [maxHeight + 5, 4], [maxHeight + 6, 3]],
        2: [[maxHeight + 4, 2], [maxHeight + 4, 3], [maxHeight + 4, 4], [maxHeight + 5, 4], [maxHeight + 6, 4]],
        3: [[maxHeight + 4, 2], [maxHeight + 5, 2], [maxHeight + 6, 2], [maxHeight + 7, 2]],
        4: [[maxHeight + 4, 2], [maxHeight + 4, 3], [maxHeight + 5, 2], [maxHeight + 5, 3]]
    }
    return rock_shapes.get(shape, [])

def moveRock(arrow, rock, fallen):
    move = True
    if arrow == '>':
        i = 0
        while i < len(rock) and move:
            if rock[i][1] > 5 or tuple([rock[i][0], rock[i][1] + 1]) in fallen:
                move = False
            i += 1
        if move:
            for block in rock:
                block[1] += 1
    if arrow == '<':
        i = 0
        while i < len(rock) and move:
            if rock[i][1] < 1 or tuple([rock[i][0], rock[i][1] - 1]) in fallen:
                move = False
            i += 1
        if move:
            for block in rock:
                block[1] -= 1

def fall(rock, fallen):
    fall = True
    i = 0
    while i < len(rock) and fall:
        if tuple([rock[i][0] - 1, rock[i][1]]) in fallen:
            fall = False
        i += 1
    if fall:
        for block in rock:
            block[0] -= 1
    else:
        for block in rock:
            fallen.add(tuple(block))
    return fall

fallen = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)}   # starting with the floor

maxHeight = 0
counter = 0
jet = 0

while counter < 2022:  # 2022 for part one
    currentRock = createRock(counter % 5, maxHeight)
    falling = True
    while falling:
        moveRock(arrows[jet % len(arrows)], currentRock, fallen)
        jet += 1
        falling = fall(currentRock, fallen)
        maxHeight = max(fallen)[0]
    counter += 1

print(maxHeight)