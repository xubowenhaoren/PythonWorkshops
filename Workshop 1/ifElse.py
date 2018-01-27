def main():
    num = int(input("give me a number:"))
    #int() converts proper integer-strings back to integers
    if num >= 0:
        #runs when the condition following if is True
        print("the number is not negative")
    else:# num < 0
        #runs when the condition following if is False
        print("the number is negative")
main()
