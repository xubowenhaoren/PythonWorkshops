import random
def is_number_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

def random_number():
    return random.randint(1, 100)
    
def main():
    number = random_number()
    guessed_number = False
    guess = input("Guess a number between 1 and 100: ")
    num_guesses = 0
    while not guessed_number:
        if not is_number_valid(guess):
            guess = input("Bad input. Guess a number between 1 and 100: ")
            continue # Optional
        else:
            num_guesses += 1
            guess = int(guess)
            if guess < number:
                guess = input("Too low. Guess again: ")
            elif guess > number:
                guess = input("Too high. Guess again: ")
            else:
                print("You got it in", num_guesses, ("guess" if num_guesses == 1 else "guesses") + "!")
                guessed_number = True
    print("Thanks for playing.")
main()
