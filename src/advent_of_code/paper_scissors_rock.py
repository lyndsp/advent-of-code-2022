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
    plays = {'A':rock, 'B':paper, 'C':scissors}

    opponentPlay = plays[round[0]]

    lose = 0
    draw = 3
    win = 6
    outcomes = {'X':lose, 'Y':draw, 'Z':win}

    outcome = outcomes[round[1]]

    playForOutcome = { 
        rock: {lose:scissors, draw:rock, win:paper}, 
        paper: {lose:rock, draw:paper, win:scissors},
        scissors: {lose:paper, draw:scissors, win:rock} 
        }

    myPlay = playForOutcome[opponentPlay][outcome]

    roundScore = myPlay + outcome

    return roundScore

def scoreRounds(rounds):
    totalScore = sum(scoreOneRound(round) for round in rounds)

    return totalScore