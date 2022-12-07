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

def test_find_matching_item():
    matchingItem = findMatchingItem("CrZsJsPPZsGzwwsLwLmpwMDw")

    assert matchingItem == 's'

def test_find_matching_item_priority():
    matchingItemPriority = findMatchingItemPriority("vJrwpWtwJgWrhcsFMMfFFhFp")

    assert matchingItemPriority == 16

def test_total_matching_items_priority():
    totalPriority = totalMatchingItemsPriority("day-3-test.txt")

    assert totalPriority == 157

def test_day_3_1():
    totalPriority = totalMatchingItemsPriority("day-3.txt")

    assert totalPriority == 7908

def test_find_common_item_in_rucksacks():
    rucksacks = [
        list("vJrwpWtwJgWrhcsFMMfFFhFp"),
        list("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"), 
        list("PmmdzqPrVvPwwTWBwg")]

    commonItem = findCommonItem(rucksacks)

    assert commonItem == 'r'

def test_find_common_item_in_more_rucksacks():
    rucksacks = [
        list("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
        list("ttgJtRGJQctTZtZT"), 
        list("CrZsJsPPZsGzwwsLwLmpwMDw")]

    commonItem = findCommonItem(rucksacks)

    assert commonItem == 'Z'

def test_split_into_groups_of_3():
    groups = splitIntoGroupsOf3("day-3-test.txt")

    assert len(groups) == 2

def test_find_common_items_total_priority():

    totalPriority = commonItemsTotalPriority("day-3-test.txt")

    assert totalPriority == 70

def test_day_3_2():
    totalPriority = commonItemsTotalPriority("day-3.txt")

    assert totalPriority == 2838

