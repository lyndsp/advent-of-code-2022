from advent_of_code.paper_scissors_rock import *

def test_score_draw_against_rock():
    score = scoreOneRound(('A', 'Y'))

    assert score == 4

def test_score_lose_against_paper():
    score = scoreOneRound(('B', 'X'))

    assert score == 1

def test_score_win_against_scissors():
    score = scoreOneRound(('C', 'Z'))

    assert score == 7

def test_score_lose_against_rock():
    score = scoreOneRound(('A', 'X'))

    assert score == 3

def test_score_paper_rock_loose():
    score = scoreOneRound(('B', 'X'))

    assert score == 1

def test_score_paper_paper_draw():
    score = scoreOneRound(('B', 'Y'))

    assert score == 5

def test_score_draw_against_scissors():
    score = scoreOneRound(('C', 'Z'))

    assert score == 6

def test_score_three_rounds():
    totalScore = scoreRounds((('A', 'Y'), ('B', 'X'),('C', 'Z')))

    assert totalScore == 12

def test_parse_rounds():
    rounds = parseRounds("day-2-test.txt")

    assert len(rounds) == 4

def test_day_2_1():
    rounds = parseRounds("day-2.txt")
    totalScore = scoreRounds(rounds)

    assert 13809 == 13809
