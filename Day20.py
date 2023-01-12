with open('20/input.txt') as inputFile:
    rawLines = inputFile.readlines()

inputNumbers = []
for i in range(len(rawLines)):
    inputNumbers.append([])
    inputNumbers[i].append(int(rawLines[i]))
    inputNumbers[i].append(0)

# part one:
for i in range(len(inputNumbers)):
    while inputNumbers[i][1] == 0:
        inputNumbers[i][1] = 1
        num = inputNumbers.pop(i)
        if (i + num[0]) % len(inputNumbers) == 0:  # to add it to the end of the list instead of the beginning
            inputNumbers.insert(len(inputNumbers), num)
        else:
            inputNumbers.insert(((i + num[0]) % len(inputNumbers)), num)

print(inputNumbers[(inputNumbers.index([0, 1]) + 1000) % len (inputNumbers)][0] + inputNumbers[(inputNumbers.index([0, 1]) + 2000) % len (inputNumbers)][0] + inputNumbers[(inputNumbers.index([0, 1]) + 3000) % len (inputNumbers)][0])

# part two:
decryptionKey = 811589153
decrypted = []
for i in range(len(rawLines)):
    decrypted.append([])
    decrypted[i].append(i)  # to keep track of numbers' original order
    decrypted[i].append(int(rawLines[i]) * decryptionKey)
    decrypted[i].append(0)  # just to keep track of mixing rounds, not necessary

for n in range(10):
    for j in range(len(decrypted)):
        for i in range(len(decrypted)):
            if decrypted[i][0] == j:
                decrypted[i][2] += 1
                num = decrypted.pop(i)
                if (i + num[1]) % len(decrypted) == 0:  # to add it to the end of the list instead of the beginning
                    decrypted.insert(len(decrypted), num)
                else:
                    decrypted.insert((i + num[1]) % len(decrypted), num)
                break

for num in decrypted:
    if num[1] == 0:
        zero = num
print(decrypted[(decrypted.index(zero) + 1000) % len (decrypted)][1] + decrypted[(decrypted.index(zero) + 2000) % len (decrypted)][1] + decrypted[(decrypted.index(zero) + 3000) % len (decrypted)][1])