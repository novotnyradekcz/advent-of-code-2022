with open('8/input.txt') as inputFile:
    rawLines = inputFile.readlines()

lines = []
for line in rawLines:
    lines.append(line.strip('\n'))

# part one:
counterList = []
    
for i in range(len(lines)):
    max = -1

    j = 0
    while j < len(lines[i]):
        if int(lines[i][j]) > max:
            if [i, j] not in counterList:
                counterList.append([i, j])
            max = int(lines[i][j])
        j += 1
    max = -1
    while j > 0:
        j -= 1
        if int(lines[i][j]) > max:
            if [i, j] not in counterList:
                counterList.append([i, j])
            max = int(lines[i][j])
for j in range(len(lines[i])):
    max = -1
    i = 0
    while i < len(lines):
        if int(lines[i][j]) > max:
            if [i, j] not in counterList:
                counterList.append([i, j])
            max = int(lines[i][j])
        i += 1
    max = -1
    while i > 0:
        i -= 1
        if int(lines[i][j]) > max:
            if [i, j] not in counterList:
                counterList.append([i, j])
            max = int(lines[i][j])
print(len(counterList))

# part two:
finalScore = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        score = 1
        for k in range(i + 1, len(lines)):
            if int(lines[i][j]) <= int(lines[k][j]) or k == len(lines) - 1:
                score *= (k - i)
                break
        for k in range(i - 1, -1, -1):
            if int(lines[i][j]) <= int(lines[k][j]) or k == 0:
                score *= (i - k)
                break
        for l in range(j + 1, len(lines[i])):
            if int(lines[i][j]) <= int(lines[i][l]) or l == len(lines[i]) - 1:
                score *= (j - l)
                break
        for l in range(j - 1, -1, -1):
            if int(lines[i][j]) <= int(lines[i][l]) or l == 0:
                score *= (l - j)
                break
        if score > finalScore:
            finalScore = score
    
print(finalScore)