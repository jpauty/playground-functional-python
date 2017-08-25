from reduce import reduce
import builtins
from operator import add,mul

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testReduce():
    try:
        count1 = reduce(add,[1,2,3],0)
        assert count1 == 6, "Running myReduce(add,[1,2,3],0)... Expected 6, got {}".format(count1)
        count2 = reduce(mul,[1,2,3],2)
        assert count2 == 12, "myReduce(mul,[1,2,3],2)... Expected 12, got {}".format(count2)
        accList = reduce(add,[[1,2],[3,4]],[])
        assert accList == [1,2,3,4], "myReduce(add,[[1,2],[3,4]],[]).. Expected [1,2,3,4], got {}".format(accList)
        success()

        send_msg("Kudos 🌟", "Did you know that you could use the sum function? Try it!")
        #send_msg("Kudos 🌟", "")
        #    send_msg("Kudos 🌟", "galaxies = [37, 3, 2]")
        #    send_msg("Kudos 🌟", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testReduce()
