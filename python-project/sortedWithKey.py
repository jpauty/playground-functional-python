def sortedWithKey(values,keyFunc):
    # implement sortedWithKey here.
    # you should call sorted. There should be no need to modify sorted 

def sorted(values):
    if len(values) < 2: 
        return values
    else:
        return merge(sorted(values[0:len(values)//2]), sorted(values[len(values)//2:]))
    
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