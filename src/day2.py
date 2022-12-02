import fileinput

scoreMap = {'X': 1, 'Y': 2, 'Z': 3}
moveMap = {'A': ['Z', 'X', 'Y'], 'B': ['X', 'Y', 'Z'], 'C': ['Y', 'Z', 'X']}


def calculateScore1(move):
    if move == "A Y" or move == "B Z" or move == "C X":
        return 6+scoreMap[move[2:]]
    elif move == "A X" or move == "B Y" or move == "C Z":
        return 3+scoreMap[move[2:]]
    else:
        return 0+scoreMap[move[2:]]


def calculateScore2(move):
    if move[2:] == "X":
        return 0 + scoreMap[moveMap[move[:1]][0]]
    elif move[2:] == "Y":
        return 3 + scoreMap[moveMap[move[:1]][1]]
    else:
        return 6 + scoreMap[moveMap[move[:1]][2]]


games = ''.join(fileinput.input(files='./inputs/day2.txt')).split('\n')

print(sum([calculateScore1(game) for game in games]))
print(sum([calculateScore2(game) for game in games]))
