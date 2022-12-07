def itemPriority(item) :
    ascii = ord(item)

    if ascii > 96 :
        ascii -= 96
    else :
        ascii -= 38

    return ascii

def findMatchingItem(items):
    itemsPerCompartment = len(items) / 2

    rightItems = []
    leftItems = list(items)

    while len(leftItems) > itemsPerCompartment:
        rightItems.append(leftItems.pop())

    matchingItem = {i for i in leftItems if i in rightItems}

    return matchingItem.pop()

def findMatchingItemPriority(items):
    matchingItem = findMatchingItem(items)

    return itemPriority(matchingItem)

def totalMatchingItemsPriority(path):
    totalPriority = 0

    with open(path) as f:
        for line in f:
            items = line.strip()
            totalPriority += findMatchingItemPriority(items)
    
    return totalPriority

def findCommonItem(rucksacks) :
    itemsInFirstTwoRucksacks = {i for i in rucksacks[0] if i in rucksacks[1]}

    itemsInThreeRucksacks = {i for i in itemsInFirstTwoRucksacks if i in rucksacks[2]}

    return itemsInThreeRucksacks.pop()

def splitIntoGroupsOf3(path):
    groups = list()
    singleGroup = list()

    with open(path) as f:
        for line in f:
            items = line.strip()
            singleGroup.append(items)

            if len(singleGroup) == 3 :
                groups.append(singleGroup.copy())
                singleGroup.clear()
    
    return groups


def commonItemsTotalPriority(path):
    groups = splitIntoGroupsOf3(path)

    priorities = list()

    for group in groups :
        item = findCommonItem(group)
        priority = itemPriority(item)
        priorities.append(priority)
    
    return sum(priorities)
