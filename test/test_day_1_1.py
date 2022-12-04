from advent_of_code.elf_inventory import *

def test_single_elf_single_item():
    calories = [1]
    total = sumCalories(calories)
    assert total == 1

def test_single_elf_with_multiple_items():
    calories = [1, 2]
    total = sumCalories(calories)
    assert total == 3

def test_multiple_elves_with_multiple_items():
    calories = [[1, 2],[3,4]]
    total = highestElfCalories(calories)
    assert total == 7

def test_multiple_elves_with_different_multiple_items():
    calories = [[5, 2],[8,4]]
    total = highestElfCalories(calories)
    assert total == 12

def test_parse_inventories():
    inventories = parseInventories("day-1-1-test.txt")

    assert len(inventories) == 2