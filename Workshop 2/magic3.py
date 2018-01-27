import random

NUM_OF_RESPONSES = 3

def get_response():
    return random.randint(1, NUM_OF_RESPONSES)

def main():
    user_input = input("Enter the number of questions you have: ")
    play_times = NUM_OF_RESPONSES # setting the play_times to default
    if user_input.isdigit() and int(user_input) < 100:
        # if the input was appropriate, override play_times
        play_times = int(user_input)
    else:
        # otherwise the play_times remains default
        print("Bad input. You will play", NUM_OF_RESPONSES, "times as default.")
    while play_times > 0:
        question = input("What is your yes/no question? ")
        print("So your question is: ", question)
        response = get_response()
        if response == 1:
            print("Yes")
        elif response == 2:
            print("No")
        else:
            print("Hmm...Maybe")
        play_times -= 1
            
    print ("Thanks for playing.")

main()    
    
