from advent_of_code.paper_scissors_rock import *

def test_score_rock_paper_win():
    score = scoreOneRound(('A', 'Y'))

    assert score == 8

def test_score_paper_rock_loose():
    score = scoreOneRound(('B', 'X'))

    assert score == 1