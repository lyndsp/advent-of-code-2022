# Some assignments fully contains the other.
# For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
# In this example, there are 2 such pairs.

# In how many assignment pairs does one range fully contain the other?

from advent_of_code.space_assignments import Assignment


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


def test_assignment_contains_another():
    assignmentPair = Assignment.parsePair("2-3, 1-4")

    overlaps = assignmentPair[1].contains(assignmentPair[0])

    assert overlaps


def test_assignment_does_not_contain_another():
    assignmentPair = Assignment.parsePair("1-2, 2-3")

    contains = assignmentPair[1].contains(assignmentPair[0])

    assert not contains


def test_assignment_also_does_not_contain_another():
    assignmentPair = Assignment.parsePair("1-3, 1-2")

    contains = assignmentPair[1].contains(assignmentPair[0])

    assert not contains


def test_day_4():
    contains = 0

    with open("day-4.txt") as f:
        for line in f:
            assignments = line.strip()
            assignmentPair = Assignment.parsePair(assignments)

            if assignmentPair[1].contains(assignmentPair[0]) or assignmentPair[
                0
            ].contains(assignmentPair[1]):
                contains += 1

    assert contains == 441


def test_assignments_overlap():
    assignmentPair = Assignment.parsePair("1-2, 2-3")

    assert assignmentPair[1].overlaps(assignmentPair[0])

    assert assignmentPair[0].overlaps(assignmentPair[1])


def test_assignments_dont_overlap():
    assignmentPair = Assignment.parsePair("1-1, 2-2")

    assert not assignmentPair[1].overlaps(assignmentPair[0])

    assert not assignmentPair[0].overlaps(assignmentPair[1])


def test_day_4_2():
    overlaps = 0

    with open("day-4.txt") as f:
        for line in f:
            assignments = line.strip()
            assignmentPair = Assignment.parsePair(assignments)

            if assignmentPair[1].overlaps(assignmentPair[0]) or assignmentPair[
                0
            ].overlaps(assignmentPair[1]):
                overlaps += 1

    assert overlaps == 861
