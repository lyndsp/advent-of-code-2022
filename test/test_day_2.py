from advent_of_code.paper_scissors_rock import *

def test_score_rock_paper_win():
    score = scoreOneRound(('A', 'Y'))

    assert score == 8

def test_score_paper_scissors_win():
    score = scoreOneRound(('B', 'Z'))

    assert score == 9

def test_score_scissors_rock_win():
    score = scoreOneRound(('C', 'X'))

    assert score == 7

def test_score_rock_rock_draw():
    score = scoreOneRound(('A', 'X'))

    assert score == 4

def test_score_paper_rock_loose():
    score = scoreOneRound(('B', 'X'))

    assert score == 1

def test_score_paper_paper_draw():
    score = scoreOneRound(('B', 'Y'))

    assert score == 5

def test_score_scissors_draw():
    score = scoreOneRound(('C', 'Z'))

    assert score == 6

def test_score_three_rounds():
    totalScore = scoreRounds((('A', 'Y'), ('B', 'X'),('C', 'Z')))

    assert totalScore == 15

def test_parse_rounds():
    rounds = parseRounds("day-2-test.txt")

    assert len(rounds) == 4

def test_score_parsed_rounds():
    rounds = parseRounds("day-2-test.txt")
    totalScore = scoreRounds(rounds)

    assert totalScore == 29

def test_day_2_1():
    rounds = parseRounds("day-2.txt")
    totalScore = scoreRounds(rounds)

    assert totalScore == 13809
