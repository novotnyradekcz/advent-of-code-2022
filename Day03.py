with open('3/input.txt') as inputFile:
    lines = inputFile.readlines()

priorities = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0

# part one:
def checkLine(line):
    priority = 0
    for i in range(len(line) // 2): # for each item in first half
        for j in range(len(line) // 2, len(line)):  # find matching item in second half
            if line[i] == line[j]:
                priority = priorities.index(line[i])
                return priority

for line in lines:
    total += checkLine(line)
print(total)

# part two:
total = 0
for i in range(0, len(lines), 3):
    for item in priorities:
        if item in lines[i] and item in lines[i + 1] and item in lines[i + 2]:  # check if item in all three lines
            total += priorities.index(item)
            break
print(total)
