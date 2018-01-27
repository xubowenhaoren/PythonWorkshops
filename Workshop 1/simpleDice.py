import random

def roll():
    num_rolled = random.randint(1,6)
    return num_rolled

def main():
    num_rolled = roll()
    print ("you rolled a",num_rolled)

main()
