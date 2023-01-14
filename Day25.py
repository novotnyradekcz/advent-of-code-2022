with open('25/input.txt') as inputFile:
    rawLines = inputFile.readlines()

total = 0
for line in rawLines:
    for i in range(len(line) - 1):
        if line[i] == '=':
            total += -2 * (5 ** (len(line) - i - 2))
        if line[i] == '-':
            total += -1 * (5 ** (len(line) - i - 2))
        if line[i] == '0':
            total += 0 * (5 ** (len(line) - i - 2))
        if line[i] == '1':
            total += 1 * (5 ** (len(line) - i - 2))
        if line[i] == '2':
            total += 2 * (5 ** (len(line) - i - 2))

snafu = ''
while total > 0:
    if total % 5 == 3:
        snafu += '='
        total = total // 5 + 1
    if total % 5 == 4:
        snafu += '-'
        total = total // 5 + 1
    if total % 5 == 0:
        snafu += '0'
        total //= 5
    if total % 5 == 1:
        snafu += '1'
        total //= 5
    if total % 5 == 2:
        snafu += '2'
        total //= 5

for i in range(len(snafu)): # needs to be reversed
    print(snafu[len(snafu) - i - 1], end='')