from advent_of_code.paper_scissors_rock import *

def test_score_one_round():
    score = scoreOneRound(('A', 'Y'))

    assert score == 8