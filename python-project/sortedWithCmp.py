def sortedWithCmp(values,cmpFunc):
    # cmpFunc(a,b): take two arguments. Returns True is a > b else False
    # Modify sortedWithCmp so that it uses cmpFunc to compare the elements.
    # You will need to use cmpFunc in merge. 
    if len(values) < 2: 
        return values
    else:
        return merge(sortedWithCmp(values[0:len(values)//2],cmpFunc), sortedWithCmp(values[len(values)//2:],cmpFunc))
    
def merge(left,right):
    leftIndex,rightIndex = 0,0
    merged = []
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    merged += left[leftIndex:]+right[rightIndex:]
    return merged