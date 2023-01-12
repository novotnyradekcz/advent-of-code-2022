import random

with  open('18/input.txt') as inputFile:
    rawLines = inputFile.readlines()

cubes = []  # convert to a list of integers
for line in rawLines:
    stripped = line.strip().split(',')
    cube = []
    for xyz in stripped:
        cube.append(int(xyz))
    cubes.append(cube)
# print(cubes)

# part one:
touching = 0
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        if (cubes[i][0] == cubes[j][0] and cubes[i][1] == cubes[j][1] and abs(cubes[i][2] - cubes[j][2]) == 1) or (cubes[i][0] == cubes[j][0] and abs(cubes[i][1] - cubes[j][1]) == 1 and cubes[i][2] == cubes[j][2]) or (abs(cubes[i][0] - cubes[j][0]) == 1 and cubes[i][1] == cubes[j][1] and cubes[i][2] == cubes[j][2]):
            touching -= 1
totalArea = 6 * len(cubes) + 2 * touching
print(totalArea)

# part two:
highestXYZ = [0, 0, 0]
lowestXYZ = [0, 0, 0]
for cube in cubes:  # finding droplet boundaries
    for i in range(3):
        if cube[i] < lowestXYZ[i]:
            lowestXYZ[i] = cube[i]
        if cube[i] > highestXYZ[i]:
            highestXYZ[i] = cube[i]

steam = [9, 9, 9]   # letting a steam droplet loose in the cavity
visited = []
for n in range(100000): # 100000 is enough to get the right result
    if steam not in visited:
        visited.append([])
        for i in range(3):
            visited[-1].append(steam[i])
    move = random.randint(0, 5)
    if move % 2 == 0:
        steam[move // 2] -= 1
    else:
        steam[move // 2] += 1
    if steam in cubes:
        if move % 2 == 0:
            steam[move // 2] += 1
        else:
            steam[move // 2] -= 1
# print(len(visited))

touchingCavity = 0  # calculate the surface area of large cavity
for i in range(len(visited)):
    for j in range(i + 1, len(visited)):
        if (visited[i][0] == visited[j][0] and visited[i][1] == visited[j][1] and abs(visited[i][2] - visited[j][2]) == 1) or (visited[i][0] == visited[j][0] and abs(visited[i][1] - visited[j][1]) == 1 and visited[i][2] == visited[j][2]) or (abs(visited[i][0] - visited[j][0]) == 1 and visited[i][1] == visited[j][1] and visited[i][2] == visited[j][2]):
            touchingCavity -= 1
areaCavity = 6 * len(visited) + 2 * touchingCavity
# print(areaCavity)

air = []    # let's find all cavities
for i in range(highestXYZ[0] + 1):
    for j in range(highestXYZ[1] + 1):
        for k in range(highestXYZ[2] + 1):
            if [i, j, k] not in cubes and [i, j, k] not in visited: # excluding large cavity as well
                air.append([i, j, k])
# print(len(air)) # number of air cubes (excluding largest cavity in the middle)

sizes = []
for steam in air:
    visited = []
    for n in range(100): # 100 is enough to get the right result for small cavities
        if steam not in visited:
            visited.append([])
            for i in range(3):
                visited[-1].append(steam[i])
        if len(visited) > 10:   # to exclude space outside the droplet
            break
        move = random.randint(0, 5)
        if move % 2 == 0:
            steam[move // 2] -= 1
        else:
            steam[move // 2] += 1
        if steam in cubes:
            if move % 2 == 0:
                steam[move // 2] += 1
            else:
                steam[move // 2] -= 1
    if len(visited) < 10:
        sizes.append(len(visited))
        # print(len(visited))
# print(sizes)

surfaceArea = totalArea - areaCavity - sizes.count(1) * 6 - sizes.count(2) * 5 - sizes.count(3) / 3 * 14    # subtract surface areas of all cavities
print(surfaceArea)