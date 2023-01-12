with open('6/input.txt') as inputFile:
    content = inputFile.read()

# part one:    
for i in range(3, len(content)):
    if content[i - 3] != content[i - 2] and content[i - 3] != content[i - 1] and content[i - 3] != content[i] and content[i - 2] != content[i - 1] and content[i - 2] != content[i] and content[i - 1] != content[i]:
        print(i + 1)
        break

# part two:
for i in range(len(content)):
    for j in range(i, i + 14):
        if content[j] in content[j + 1:i + 14]:
            break
    if j == i + 13:
        print(i + 14)
        break