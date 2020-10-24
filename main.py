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
                    cipherMsg("encrypt")
            elif userInput == 3:  # Decrypt
                if KEY is None:
                    print("You must input your Student Identity number! ")
                    break
                else:
                    cipherMsg("decrypt")
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
    global KEY

    while True:
        inputValue = input("Enter your Student Identity number: ")

        if (len(inputValue) == 6) and (inputValue.isdigit()):
            print("You Identification number was accepted! ")
            return int(inputValue)
            break
        else:
            print("You Identification number was not accepted! \nThe number should be 6 digits in length! ")

    menu()


def cipherMsg(operation):

    global KEY

    shiftValue = [int(x) for x in str(KEY)]

    charList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ",
                "."]

    oldMessage = str(input("Enter message: "))
    newMessage = []

    incValue = 0
    try:
        for char in oldMessage:
            charIndex = charList.index(char)

            if incValue > 5:
                incValue = 0

            if operation == "encrypt":
                charIndex = charIndex + shiftValue[incValue]
            elif operation == "decrypt":
                charIndex = charIndex - shiftValue[incValue]

            if charIndex > 64:
                charIndex = charIndex % 64
            elif charIndex < 1:
                charIndex = 64 - ((charIndex * -1) % 64)

            newMessage.append(charList[charIndex])

            incValue = incValue + 1

        message = "".join(newMessage)

        print("Your " + operation + "ed Message: " + message)

    except ValueError:
        print("The message contains an invalid character! \nONLY lowercase/uppercase, digits, period and space characters are accepted! ")

    menu()


menu()
