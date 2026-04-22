cookieAmount = 0
cookieClickValue = 1


def mainLoop():
    global cookieAmount
    global cookieClickValue
    commandInput = input(">>> ")
    mainCommandParts = commandInput.split()
    mainCommand = mainCommandParts[0]
    commandArguments = mainCommandParts[1:]

    match mainCommand:
        case "cookie":
            if not commandArguments:
                print("No argument")
            elif commandArguments[0] in ["-h", "--help"]:
                print("help")
            elif commandArguments[0] in ["-c", "--click"]:
                cookieAmount += cookieClickValue
                print("You got", cookieClickValue, "Cookies")
            elif commandArguments[0] in ["-am", "--amount"]:
                print("You have:", cookieAmount, "cookies")
    mainLoop()

    print("\n", mainCommand)
    print(commandArguments)


mainLoop()
