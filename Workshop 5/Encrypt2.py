alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789! "
  
def main():
    message = input("Please enter a message: ")
    decrypt = input("Do you want to decrypt? Yes/no")
    key = input("Enter a key (1-"+str(len(alphabet)-1)+"):")
    key = int(key)
    if decrypt.lower() == "yes":
        key = len(alphabet) - key
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
