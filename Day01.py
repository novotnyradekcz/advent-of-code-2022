with open('1/input.txt') as inputFile:
    lines = inputFile.readlines()

calories = 0
maxima = []
for line in lines:
    if line == '\n':
        maxima.append(calories)
        calories = 0
    else:
        calories += int(line.strip('\n'))

# part one:
print(max(maxima))
# part two:
topThree = max(maxima)
maxima.remove(max(maxima))
topThree += max(maxima)
maxima.remove(max(maxima))
topThree += max(maxima)
print(topThree)