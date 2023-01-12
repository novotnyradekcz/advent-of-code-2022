with open('5/input.txt') as inputFile:
    lines = inputFile.readlines()

# part one:
columns = [['R', 'P', 'C', 'D', 'B', 'G'],
            ['H', 'V', 'G'],
            ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
            ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
            ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
            ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
            ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
            ['C', 'M', 'D', 'B', 'F'],
            ['F', 'C', 'Q', 'G']]

for line in lines:
    # move: 5(-6), from 12(/13), to 17(18)
    if line[6] != ' ':
        move = int(line[5:7])
        fromC = int(line[13])
        toC = int(line[18])
    else:
        move = int(line[5])
        fromC = int(line[12])
        toC = int(line[17])
    for i in range(move):   # moving boxes one by one
        columns[toC - 1].append(columns[fromC - 1].pop())

result = ''
for column in columns:
    result += column.pop()
print(result)

# part two:
columns = [['R', 'P', 'C', 'D', 'B', 'G'],
            ['H', 'V', 'G'],
            ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
            ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
            ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
            ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
            ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
            ['C', 'M', 'D', 'B', 'F'],
            ['F', 'C', 'Q', 'G']]

for line in lines:
    # move: 5(-6), from 12(/13), to 17(18)
    if line[6] != ' ':
        move = int(line[5:7])
        fromC = int(line[13])
        toC = int(line[18])
    else:
        move = int(line[5])
        fromC = int(line[12])
        toC = int(line[17])
    columns[toC - 1].extend(columns[fromC - 1][-move:]) # moving (copying) all boxes at once
    for i in range(move):   # removing them fromm the original column
        columns[fromC - 1].pop()

result = ''
for column in columns:
    result += column.pop()
print(result)