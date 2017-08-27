from sortedWithCmp import sortedWithCmp
from operator import add,mul

def _sortedWithCmp(values,cmpFunc):
    # cmpFunc(a,b): take two arguments. Returns True is a > b else False
    # modify sortedWithCmp so that it uses cmpFunc to compare the element
    # you will need to modify merge 
    if len(values) < 2: 
        return values
    else:
        return merge(sorted(values[0:len(values)//2]), sorted(values[len(values)//2:]), cmpFunc)
    
def _merge(left,right,cmpFunc):
    leftIndex,rightIndex = 0,0
    merged = []
    while leftIndex < len(left) and rightIndex < len(right):
        if not cmpFunc(left[leftIndex],right[rightIndex]):
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    merged += left[leftIndex:]+right[rightIndex:]
    return merged



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testReduce():
    try:
        sorted1 = sortedWithCmp(['bere','az','aer','e'], lambda w1,w2:len(w1)>len(w2) )
        assert sorted1 == ['e','az','aer','bere'], """sortedWithCmp(['bere','az','aer','e'], lambda w1,w2:len(w1)>len(w2) )... Expected ['e','az','aer','bere'], got {}""".format(sorted1)
        success()

        send_msg("You're a functional rookie 🌟", "You successfully implemented sortedWithCmp.")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testReduce()
