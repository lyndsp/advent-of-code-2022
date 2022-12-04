def parseInventories(path):

    inventories = list()
    currentInventory = list()

    with open(path) as f:
        for line in f:
            inventory = line.strip()
            if len(inventory) == 0 :
                inventories.append(currentInventory.copy())
                currentInventory.clear()
            else:
                currentInventory.append(line)

    inventories.append(currentInventory)

    return inventories

def sumCalories(calories):
    calories = [int(c) for c in calories]

    return sum(calories)

def highestElfCalories(elfInventories):
    caloriesPerElf = [sumCalories(inventory) for inventory in elfInventories]

    sortedCaloriesPerElf = sorted(caloriesPerElf, reverse=True)

    return sortedCaloriesPerElf[0]
