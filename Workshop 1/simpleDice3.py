import random

def roll():
    numRolled = random.randint(1,6)
    return numRolled

def main():
    numRolled = roll()
    print ("The first dice rolled a",numRolled)
    rollAgain = input("Do you want a second roll? type yes or no:")
    if rollAgain.lower() != "no":
        numRolled2 = roll()
        print ("The second dice rolled a",numRolled2)
        
main()
