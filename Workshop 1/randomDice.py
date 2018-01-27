import random

def roll():
    num_rolled = random.randint(1,6)
    # generates a number between 1 and 6 inclusive
    return num_rolled

def tester():
    num_rolled = roll()
    print (num_rolled)

tester()
