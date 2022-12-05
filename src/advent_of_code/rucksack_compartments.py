def itemPriority(item) :
    ascii = ord(item)

    if ascii > 96 :
        ascii -= 96
    else :
        ascii -= 38

    return ascii