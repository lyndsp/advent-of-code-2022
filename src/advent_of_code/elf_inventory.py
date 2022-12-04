def sumCaloriesPerElf(calories):
    calorySum = 0

    calories = list(map(int, calories))

    for item in calories :
        calorySum += item

    return calorySum
