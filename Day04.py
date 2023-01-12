with open('4/input.txt') as inputFile:
    lines = inputFile.readlines()

# part one:
containedPairs = 0
for line in lines:
    sections = line.split(',')  # ['1-2', '3-4']
    elf1 = sections[0].split('-')   # [1, 2]
    elf2 = sections[1].split('-')   # [3, 4]
    if (int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
        containedPairs += 1
print(containedPairs)

# part two:
overlappingPairs = 0
for line in lines:
    sections = line.split(',')  # ['1-2', '3-4']
    elf1 = sections[0].split('-')   # [1, 2]
    elf2 = sections[1].split('-')   # [3, 4]
    if (int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0])) or (int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0])):
        overlappingPairs += 1
print(overlappingPairs)