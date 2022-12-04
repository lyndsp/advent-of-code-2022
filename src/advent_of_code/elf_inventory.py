def sumCalories(calories):
    calories = [int(c) for c in calories]

    return sum(calories)

def highestElfCalories(elfInventories):
    caloriesPerElf = [sumCalories(inventory) for inventory in elfInventories]

    sortedCaloriesPerElf = sorted(caloriesPerElf, reverse=True)

    return sortedCaloriesPerElf[0]
