from reduceUseCase import all, any, sum
from operator import add, mul
import builtins

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def testReduce():
    try:
        any1 =  any([False,True]) 
        assert any1 == True, "Running any([False,True]) ... Expected True, got %s"%any1
        any2 =  any([False,False])
        assert any2 == False, "Running any([False,False]) ... Expected False, got %s"%any2
        any3 =  any([True,True])
        assert any3 == True, "Running any([True,True]) ... Expected True, got %s"%any3
        all1 =  all([False,True]) 
        assert all1 == False, "Running all([False,True]) ... Expected False, got %s"%all1
        all2 =  all([False,False])
        assert all2 == False, "Running all([False,False]) ... Expected False, got %s"%all2
        all3 =  all([True,True])
        assert any3 == True, "Running all([True,True]) ... Expected True, got %s"%all3
        sum1 = sum(range(10))
        expectedSum1 = builtins.sum(range(10))
        assert sum1 == expectedSum1, "Running sum(range(10)) ... Expected %s, got %s"%(expectedSum1,sum1)
        success()

        send_msg("You're a functional rookie 🌟", "You successfully implement any, all and sum.")
        
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        #send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    testReduce()
