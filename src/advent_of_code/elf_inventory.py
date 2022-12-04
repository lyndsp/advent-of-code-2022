def sumCalories(calories):
    calories = [int(c) for c in calories]

    return sum(calories)

def highestElfCalories(elfInventories):
    highestCalorySum = 0

    for inventory in elfInventories :
        calorySum = sumCalories(inventory)

        if calorySum > highestCalorySum :
            highestCalorySum = calorySum
        
    return highestCalorySum
