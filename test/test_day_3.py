# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?

from advent_of_code.rucksack_compartments import *

# Compartments have equal number of contents
# Only one item type is shared across compartments

def test_a_has_priority_1():
    priority = itemPriority('a')

    assert priority == 1

def test_z_has_priority_26():
    priority = itemPriority('z')

    assert priority == 26

def test_A_has_priority_27():
    priority = itemPriority('A')

    assert priority == 27
