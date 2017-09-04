from enumerateZip import enumerate

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testEnumerate():
    try:
        enumerate1 = list(enumerate([2,3,4])) 
        assert enumerate1 ==[(0,2),(1,3),(2,4)], """Running list(enumerate([2,3,4])) ... Expected [(0,2),(1,3),(2,4)], got {}""".format(enumerate1)
        success()
        
        send_msg("You're a functional rookie 🌟", "You successfully implemented enumerate.")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testEnumerate()
