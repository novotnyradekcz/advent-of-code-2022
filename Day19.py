import random

with open('19/input.txt') as inputFile:
    rawLines = inputFile.readlines()
splitLines = []
for line in rawLines:
    splitLines.append(line.split())
justCosts = []
for line in splitLines:
    justCosts.append([int(line[6]), int(line[12]), int(line[18]), int(line[21]), int(line[27]), int(line[30])])
print(justCosts)

results = []
for blueprint in justCosts:
    maxGeode = 0
    for n in range(10000):  # 10000 is enough to get 1804 (which is wrong)
        time = 0
        ore = 0
        clay = 0
        obsidian = 0
        geode = 0
        oreRobot = 1
        clayRobot = 0
        obsidianRobot = 0
        geodeRobot = 0
        while time < 24:
            newOreRobot = 0
            newClayRobot = 0
            newObsidianRobot = 0
            newGeodeRobot = 0
            if ore >= blueprint[4] and obsidian >= blueprint[5]:
                ore -= blueprint[4]
                obsidian -= blueprint[5]
                newGeodeRobot = 1
            elif ore >= blueprint[2] and clay >= blueprint[3] and obsidianRobot < blueprint[5] and (ore >= blueprint[2] + blueprint[4] or obsidianRobot < random.randint(1,10)):
                ore -= blueprint[2]
                clay -= blueprint[3]
                newObsidianRobot = 1
            elif ore >= blueprint[1] and clayRobot < blueprint[3] and (ore >= blueprint[1] + blueprint[4] or clayRobot < random.randint(1,10)):
                ore -= blueprint[1]
                newClayRobot = 1
            elif ore >= blueprint[0] and (oreRobot < blueprint[0] or oreRobot < blueprint[1] or oreRobot < blueprint[2] or oreRobot < blueprint[4]) and oreRobot < random.randint(1,5):
                ore -= blueprint[0]
                newOreRobot = 1
            ore += oreRobot
            clay += clayRobot
            obsidian += obsidianRobot
            geode += geodeRobot
            oreRobot += newOreRobot
            clayRobot += newClayRobot
            obsidianRobot += newObsidianRobot
            geodeRobot += newGeodeRobot
            time += 1
        if geode > maxGeode:
            maxGeode = geode
            # print(oreRobot, clayRobot, obsidianRobot, geodeRobot)
    results.append(maxGeode)
print(results)

qualityLevel = 0
for i in range(len(results)):
    qualityLevel += (i + 1) * results[i]
print(qualityLevel)