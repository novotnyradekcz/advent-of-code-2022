with open('10/input.txt') as inputFile:
    rawLines = inputFile.readlines()

lines = []
for line in rawLines:
    lines.append(line.split())

# part one:
strength = 0
cycle = 0
x = 1
for line in lines:
    if line[0] == 'noop':
        cycle += 1
        if (cycle - 20) % 40 == 0 and cycle <= 220:
            strength += cycle * x
    if line[0] == 'addx':
        cycle += 1
        if (cycle - 20) % 40 == 0 and cycle <= 220:
            strength += cycle * x
        cycle += 1
        if (cycle - 20) % 40 == 0 and cycle <= 220:
            strength += cycle * x
        x += int(line[1])
print(strength)

# part two:
position = 1
cycle = 0
display = [[], [], [], [], [], [], []]

for line in lines:
    if line[0] == 'noop':
        if cycle % 40 >= position - 1 and cycle % 40 <= position + 1:
            display[cycle // 40].append('#')    # saving to list to print later
        else:
            display[cycle // 40].append('.')
        cycle += 1
    if line[0] == 'addx':
        if cycle % 40 >= position - 1 and cycle % 40 <= position + 1:
            display[cycle // 40].append('#')
        else:
            display[cycle // 40].append('.')
        cycle += 1
        if cycle % 40 >= position - 1 and cycle % 40 <= position + 1:
            display[cycle // 40].append('#')
        else:
            display[cycle // 40].append('.')
        cycle += 1
        position += int(line[1])    # update position of sprite

for row in display:
    print(''.join(row))