# Some assignments fully contains the other. 
# For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
# In this example, there are 2 such pairs.

# In how many assignment pairs does one range fully contain the other?

from advent_of_code.space_assignments import *

def test_parse_assignment():
    assignment = Assignment("2-8")

    assert assignment.start == 2
    assert assignment.end == 8

def test_parse_another_assignment():
    assignment = Assignment("3-7")

    assert assignment.start == 3
    assert assignment.end == 7

def test_parse_pair_of_assignments():
    assignmentPair = Assignment.parsePair("3-39,14-97")

    assert assignmentPair[0].start == 3    
    assert assignmentPair[1].end == 97