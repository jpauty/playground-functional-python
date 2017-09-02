from anyAll import hasEven

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testAnyAll():
    try:
        hasEven1 = hasEven([2,3]) 
        assert hasEven1 == True, """Running hasEven([2,3])... Expected True, got {}""".format(hasEven1)
        hasEven1 = hasEven([2,4]) 
        assert hasEven1 == True, """Running hasEven([2,4])... Expected True, got {}""".format(hasEven1)
        hasEven1 = hasEven([1,3]) 
        assert hasEven1 == False, """Running hasEven([1,3])... Expected True, got {}""".format(hasEven1)
        success()
        
        send_msg("You're a functional rookie 🌟", "You successfully implemented hasEven.")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testAnyAll()
