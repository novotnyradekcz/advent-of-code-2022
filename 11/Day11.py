with open('11/input.txt') as inputFile:
    rawLines = inputFile.readlines()
    
splitLines = []
for line in rawLines:
    splitLines.append(line.split())

# original part one code, unoptimised, unusable for part two
# monkeyItems = [[80], [75, 83, 74], [86, 67, 61, 96, 52, 63, 73], [85, 83, 55, 85, 57, 70, 85, 52], [67, 75, 91, 72, 89], [66, 64, 68, 92, 68, 77], [97, 94, 79, 88], [77, 85]]
# monkeyInspections = [0, 0, 0, 0, 0, 0, 0, 0]
# i = 0
# while i < len(splitLines):
#     i += 1  # line: starting items
#     j = 0
#     k = i
#     i += 1  # line: operation
#     for j in range(2, len(splitLines[k])):
#         worryLevel = int(splitLines[k][j].strip(','))
#         if splitLines[i][4] == '*':
#             if splitLines[i][5] == 'old':
#                 worryLevel *= worryLevel
#             else:
#                 worryLevel *= int(splitLines[i][5])
#         if splitLines[i][4] == '+':
#             if splitLines[i][5] == 'old':
#                 worryLevel += worryLevel
#             else:
#                 worryLevel += int(splitLines[i][5])
#         worryLevel = worryLevel // 3
#         i += 1  # line: test
#         monkeyInspections[i // 7] += 1
#         if worryLevel % int(splitLines[i][3]) == 0:
#             i += 1  #line: true
#             monkeyItems[int(splitLines[i][5])].append(worryLevel)
#             i -= 2  # line: back to operation
#         else:
#             i += 2  # line: false
#             monkeyItems[int(splitLines[i][5])].append(worryLevel)
#             i -= 3  # line: back to operation
#         j += 1  # next item
#     i += 5
# print(monkeyItems)  # state after round 1
# print(monkeyInspections)

def keepAway(rounds):
    monkeyItems = [[80], [75, 83, 74], [86, 67, 61, 96, 52, 63, 73], [85, 83, 55, 85, 57, 70, 85, 52], [67, 75, 91, 72, 89], [66, 64, 68, 92, 68, 77], [97, 94, 79, 88], [77, 85]]
    monkeyInspections = [0, 0, 0, 0, 0, 0, 0, 0]
    numMonkeys = 8
    i = 7
    highestDivisor = 2 * 7 * 3 * 17 * 11 * 19 * 5 * 13
    for round in range(rounds):
        for monkey in range(numMonkeys):
            i *= monkey # line: current monkey
            i += 2  # line: operation
            while len(monkeyItems[monkey]) > 0:
                worryLevel = monkeyItems[monkey].pop(0)
                if splitLines[i][4] == '*':
                    if splitLines[i][5] == 'old':
                        worryLevel *= worryLevel
                    else:
                        worryLevel *= int(splitLines[i][5])
                if splitLines[i][4] == '+':
                    if splitLines[i][5] == 'old':
                        worryLevel += worryLevel
                    else:
                        worryLevel += int(splitLines[i][5])
                if rounds == 20:    # only in part one
                    worryLevel = worryLevel // 3
                i += 1  # line: test
                monkeyInspections[monkey] += 1
                if worryLevel % int(splitLines[i][3]) == 0:
                    i += 1  #line: true
                    monkeyItems[int(splitLines[i][5])].append(worryLevel % highestDivisor)
                    i -= 2  # line: back to operation
                else:
                    i += 2  # line: false
                    monkeyItems[int(splitLines[i][5])].append(worryLevel % highestDivisor)
                    i -= 3  # line: back to operation
            i = 7 # reset monkey index
    monkeyBusiness = max(monkeyInspections) # highest value
    monkeyInspections.remove(monkeyBusiness)
    monkeyBusiness *= max(monkeyInspections)    # second highest value
    return monkeyBusiness

rounds1 = 20
rounds2 = 10000
print(keepAway(rounds1))
print(keepAway(rounds2))