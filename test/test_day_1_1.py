from advent_of_code.elf_inventory import sumCaloriesPerElf

def test_single_elf_single_item():
    calories = [1]
    total = sumCaloriesPerElf(calories)
    assert total == 1
