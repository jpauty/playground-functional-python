from sortedWithKey import sortedWithKey
from operator import add,mul

def _sortedWithKey(values,keyFunc):
    keyToVal = {keyFunc(val):val for val in values}
    sortedKeys = sorted(list(keyToVal.keys()))
    result = []
    for key in sortedKeys:
        result.append(keyToVal[key])
    return result

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testReduce():
    try:
        sorted1 = sortedWithKey(["ber","aze","zea","ty"], lambda word:word[-1] )
        assert sorted1 == ['zea', 'aze', 'ber', 'ty'], """Running sortedWithKey(["ber","aze","zea","ty"], lambda word:word[-1] )... Expected ['zea', 'aze', 'ber', 'ty'], got {}""".format(sorted1)
        success()

        send_msg("You're a functional rookie 🌟", "You successfully implemented sortedWithKey.")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testReduce()



def sortedWithCmp(values,cmpFunc):
    # cmpFunc(a,b): take two arguments. Returns True is a > b else False
    # modify sortedWithCmp so that it uses cmpFunc to compare the element
    # you will need to modify merge 
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