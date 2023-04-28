subor = open("AoC.txt", "r")
x = subor.readlines()
score = 0
for i in x:
    if i == "A X\n":
        score += 4
    if i == "A Y\n":
        score += 8
    if i == "A Z\n":
        score += 3
    if i == "B X\n":
        score += 1
    if i == "B Y\n":
        score += 5
    if i == "B Z\n":
        score += 9
    if i == "C X\n":
        score += 7
    if i == "C Y\n":
        score += 2
    if i == "C Z\n":
        score += 6
print(score)
'''
with open("AoC.txt") as fin:
    lines = fin.read().strip().split("\n")


# X, Y, Z values represent offset in what to play
play_map = {"A": 0, "B": 1, "C": 2,
            "X": -1, "Y": 0, "Z": 1}

score_key = [1, 2, 3]

score = 0
for line in lines:
    opp, result = [play_map[i] for i in line.split()]

    score += (result + 1) * 3
    score += score_key[(opp + result) % 3]

'''