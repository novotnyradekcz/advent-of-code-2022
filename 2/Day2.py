with open('2/input.txt') as inputFile:
    lines = inputFile.readlines()

# part one:
score = 0
for line in lines:
    if line[0] == 'A':  # rock
        if line[2] == 'X':  # rock
            score += 4  # draw
        if line[2] == 'Y':  # paper
            score += 8  # win
        if line[2] == 'Z':  # scissors
            score += 3  # loss
    if line[0] == 'B':  # paper
        if line[2] == 'X':  # rock
            score += 1  # loss
        if line[2] == 'Y':  # paper
            score += 5  # draw
        if line[2] == 'Z':  # scissors
            score += 9  # win
    if line[0] == 'C':  # scissors
        if line[2] == 'X':  # rock
            score += 7  # win
        if line[2] == 'Y':  # paper
            score += 2  # loss
        if line[2] == 'Z':  # scissors
            score += 6  # draw
print(score)

# part two:
score = 0
for line in lines:
    if line[0] == 'A':  # rock
        if line[2] == 'X':  # lose
            score += 3  # scissors
        if line[2] == 'Y':  # draw
            score += 4  # rock
        if line[2] == 'Z':  # win
            score += 8  # paper
    if line[0] == 'B':  # paper
        if line[2] == 'X':  # lose
            score += 1  # rock
        if line[2] == 'Y':  # draw
            score += 5  # paper
        if line[2] == 'Z':  # win
            score += 9  # scissors
    if line[0] == 'C':  # scissors
        if line[2] == 'X':  # lose
            score += 2  # paper
        if line[2] == 'Y':  # draw
            score += 6  # scissors
        if line[2] == 'Z':  # win
            score += 7  # rock
print(score)