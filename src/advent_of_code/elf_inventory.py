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

def findHighestInventory(elfInventories):
    caloriesPerElf = [sumCalories(inventory) for inventory in elfInventories]

    sortedCaloriesPerElf = sorted(caloriesPerElf, reverse=True)

    return sortedCaloriesPerElf[0]

def sumTopElfInventories(elfInventories):
    caloriesPerElf = [sumCalories(inventory) for inventory in elfInventories]

    sortedCaloriesPerElf = sorted(caloriesPerElf, reverse=True)

    numberOfElves = len(elfInventories) 

    if numberOfElves == 1 :
        return sortedCaloriesPerElf[0]
    elif numberOfElves == 2 :
        return sortedCaloriesPerElf[0] + sortedCaloriesPerElf[1]
    elif numberOfElves > 2 :
        return sortedCaloriesPerElf[0] + sortedCaloriesPerElf[1] + sortedCaloriesPerElf[2]
    
    return 0

