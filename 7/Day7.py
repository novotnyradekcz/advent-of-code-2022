with open('7/input.txt') as inputFile:
    lines = inputFile.readlines()

files = []
myList = []

for line in lines:  # split linees into words
    myList.append(line.strip("$").strip().split())

mySizes = {}
currentPath = []

for i in range(len(myList)):
    if myList[i][0] == "cd":    # if changing directory, update it
        if myList[i][1] == "..":
            currentPath.pop()
        else:
            currentPath.append(myList[i][1])
    if myList[i][0].isnumeric():
        myPath = ['.'.join(currentPath[:x+1]) for x in range(len(currentPath))] # save full path to folder
        for file in myPath: # add file's size to all its parent directories
            if file not in mySizes:
                mySizes[file] = 0
            mySizes[file] += int(myList[i][0])

# part one:
totalSize = 0
for key in mySizes.keys():
    if mySizes[key] <= 100000:
        totalSize += mySizes[key]
print(totalSize)

# part two:
totalSize = 70000000
freeSpace = totalSize - mySizes["/"]
toFree = 30000000 - freeSpace
smallest = totalSize
for key in mySizes.keys():
    if mySizes[key] > toFree and mySizes[key] < smallest:
        smallest = mySizes[key]
print(smallest)