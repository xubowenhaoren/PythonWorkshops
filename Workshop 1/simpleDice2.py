import random

def roll():
    numRolled = random.randint(1,6)
    return numRolled

def main():
    numRolled = roll()
    print ("The first dice rolled a",numRolled)
    numRolled2 = roll()
    print ("The second dice rolled a",numRolled2)
    
main()
