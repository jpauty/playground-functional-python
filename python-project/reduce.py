def reduce(accumulatingFunction,valueIter,startValue):
    s = startValue
    for v in valueIter:
        s = accumulatingFunction(s,v)
    return s
    #raise NotImplementedError
