import random

def roll():
    numRolled = random.randint(1,6)
    return numRolled

def main():
    rolling = True
    while rolling :
        roll_again = input("Ready to roll? ENTER=Roll.Q=quit.")
        if roll_again.lower() !="q":
            numRolled = roll()
            print ("The first dice rolled a",numRolled)
            rollAgain = input("Do you want a second roll? type yes or no:")
            if rollAgain.lower() == "yes":
                numRolled2 = roll()
                print ("The second dice rolled a",numRolled2)
            elif rollAgain.lower() != "no":
                print ("Bad input")
        else:
            rolling = False
    print ("Thanks for playing.")

main()
