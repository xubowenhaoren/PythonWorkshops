import random

def get_response():
    return random.randint(1,3)

def main():
    user_input = input("Enter the number of questions you have: ")
    play_times = 3
    if user_input.isnumeric() and int(user_input) < 100:
        play_times = user_input
    else:
        print("Bad input. You will play",play_times,"times as default.")
    

main()    
    
