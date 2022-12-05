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
