KEY = None


def menu():
    global KEY

    while True:
        try:
            userInput = int(
                input("1. Set Person Number: \n2. Encrypt a message: \n3. Decrypt a message: \n4. Quit: \n\nInput: "))
        except ValueError:
            print("The value must be an Integer! ")
        else:
            break

    while True:
        if (userInput >= 1) and (userInput <= 4):
            if userInput == 1:  # Set
                KEY = setKey()
            elif userInput == 2:  # Encrypt
                if KEY is None:
                    print("You must input your Student Identity number! ")
                    break
                else:
                    encrypt()
            elif userInput == 3:  # Decrypt
                if KEY is None:
                    print("You must input your Student Identity number! ")
                    break
                else:
                    decrypt()
            else:  # Exit
                while True:
                    exitProgram = input("Are you sure you want to exit the program Y/N: ")
                    if exitProgram.lower() == "y":
                        print("Goodbye! ")
                        quit()
                    elif exitProgram.lower() == "n":
                        menu()
                    else:
                        print("The input MUST be either character Y or N")

        else:
            print("The value you entered MUST be between 1 and 4! ")

    menu()


def setKey():
    print("SET KEY")


def encrypt():
    print("ENCRYPT")


def decrypt():
    print("DECRYPT")


menu()
