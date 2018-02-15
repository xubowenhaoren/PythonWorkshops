alphabet = "abcdefghijklmnopqrstuvwxyz"
  
def main():
    message = input("Please enter a message: ")
    print("If you want to decrypt a message, enter the difference of",len(alphabet),"and your key: ")
    key = input("Enter a key (1-"+str(len(alphabet)-1)+"):" )
    key = int(key)
    newMessage = ""
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % len(alphabet)
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character

    print("Your new message is: ", newMessage)
main()
