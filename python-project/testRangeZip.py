from rangeZip import evenOdd,pairs

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testEvenOdd():
    try:
        pairs1 = list(pairs(3))
        assert pairs1 == [(0,1),(1,2),(2,3)], """Running pairs(3)... Expected [(0,1),(1,2),(2,3)], got {}""".format(pairs1)
        success()
        
        evenOdd1 = list(evenOdd(3))
        assert evenOdd1 == [(0,1),(2,3),(4,5)], """Running evenOdd(3)... Expected [(0,1),(2,3),(4,5)], got {}""".format(evenOdd1)
        success()

        send_msg("You're a functional rookie 🌟", "You successfully implemented evenOdd.")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testEvenOdd()



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