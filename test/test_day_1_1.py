from advent_of_code.elf_inventory import sumCaloriesPerElf

def test_single_elf_single_item():
    calories = [1]
    total = sumCaloriesPerElf(calories)
    assert total == 1

def test_single_elf_with_multiple_items():
    calories = [1, 2]
    total = sumCaloriesPerElf(calories)
    assert total == 3
