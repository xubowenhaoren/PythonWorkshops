#demo only.
import random
low_num = 1
high_num = 100
def is_number_valid(num):
    return num.isdigit() and low_num <= int(num) <= high_num

def random_number():
    return random.randint(low_num,high_num)

# both inputs are integers, low_num <= high_num
def initialize():
    global low_num
    low_num= int(input("Enter lowest number: "))
    global high_num
    high_num= int(input("Enter highest number: "))

def to_string():
    return "A number between "+str(low_num)+" and "+str(high_num)+": "
def bad():
    return "Bad input. "+to_string()
    
def main():
    initialize()
    number = random_number()
    guessed_number = False
    guess = input(to_string())
    num_guesses = 0
    while not guessed_number:
        if not is_number_valid(guess):
            guess = input(bad())
            continue
        else:
            num_guesses +=1
            guess = int(guess)
            if guess < number:
                guess = input("Too low. Guess again: ")
            elif guess > number:
                guess = input("Too high. Guess again: ")
            else:
                print("You got it in",num_guesses,("guess" if num_guesses == 1 else "guesses") + "!")
                guessed_number = True
    print("Thanks for playing.")
main()
