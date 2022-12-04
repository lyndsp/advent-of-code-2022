def parseRounds(path):
    rounds = list()

    with open(path) as f:
        for line in f:
            round = line.strip()
            rounds.append((round[0], round[2]))

    return rounds

def scoreOneRound(round):
    rock = 1
    paper = 2
    scissors = 3
    plays = {'A':rock, 'B':paper, 'C':scissors, 'X':rock, 'Y':paper, 'Z':scissors}

    opponentPlay = plays[round[0]]
    myPlay = plays[round[1]]

    roundScore = myPlay

    # draw
    if myPlay == opponentPlay :
        return roundScore + 3

    win = False

    # Rock > Scissors
    # Paper > Rock
    # Scissors > Paper

    if myPlay == rock and opponentPlay == scissors :
        win = True
    elif myPlay == paper and opponentPlay == rock :
        win = True
    elif myPlay == scissors and opponentPlay == paper :
        win = True

    if not win :
        return roundScore

    return roundScore + 6

def scoreRounds(rounds):
    totalScore = sum(scoreOneRound(round) for round in rounds)

    return totalScore