from advent_of_code.supply_stacks import *

# F <- Top
# G
# R
# J
# L
# D <- Bottom
  
def test_move_one_item():
    stack = Stack("DLJRVGF")

    assert stack.move(1) == list("F")

def test_move_two_items():
    stack = Stack("DLJRVGF")

    assert stack.move(2) == list("FG")

def test_multiple_stacks():
    stacks = list([Stack("DLJRVGF"), Stack("TPMBVHJS")])

    assert len(stacks) == 2

# move 3 from 4 to 6
# move 1 from 5 to 8

def test_parse_command():
    command = Command("move 1 from 5 to 8")

    assert command.fromStack == 5
    assert command.toStack == 8
    assert command.moveItems == 1

def test_move_item_from_one_stack_to_another():
    stacks = Stacks([Stack("DLJRVGF"), Stack("TPMBVHJS")])

    stacks.action("move 1 from 1 to 2")

    assert stacks.top() == "GF"

def test_day_5_1():
    stacks = Stacks([
        Stack("DLJRVGF"), 
        Stack("TPMBVHJS"),
        Stack("VHMFDGPC"),
        Stack("MDPNGQ"),
        Stack("FNHLJ"),
        Stack("NFVQDHTZ"),
        Stack("FDBL"),
        Stack("MJBSVDN"),
        Stack("GLD"),
        ])

    with open("day-5.txt") as f:
        for line in f:
            stacks.action(line.strip())
    
    assert stacks.top() == "NBTVTJNFJ"

