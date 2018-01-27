import random
NUM_OF_RESPONSES = 3

def get_response():
    return random.randint(1,NUM_OF_RESPONSES)

def main():
    user_input = input("Enter the number of questions you have: ")
    play_times = NUM_OF_RESPONSES # setting the play_times to default
    if user_input.isnumeric() and int(user_input) < 100:
        play_times = user_input
        # if the input was appropriate, override play_times
    else:
        print("Bad input. You will play",NUM_OF_RESPONSES,"times as default.")
        # otherwise the play_times remains default
    

main()    
    
