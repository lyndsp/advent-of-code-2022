def scoreOneRound(round):
    # A/X Rock, B/Y Paper, C/Z Scissors
    plays = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}

    opponentPlay = plays[round[0]]
    myPlay = plays[round[1]]

    win = myPlay > opponentPlay
    loose = myPlay < opponentPlay
    draw = myPlay == opponentPlay

    roundScore = myPlay

    if loose :
        roundScore += 0
    elif draw :
        roundScore += 3
    elif win :
        roundScore += 6

    return roundScore
