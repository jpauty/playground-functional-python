def hasEven(numbers):
    hasEven = False
    for x in numbers:
        if x%2 == 0:
            hasEven = True
            break
    return hasEven