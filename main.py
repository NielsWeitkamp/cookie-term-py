cookieAmount = 0
cookieClickValue = 1


def mainLoop():
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
            else:
                print("no help")

    print("\n", mainCommand)
    print(commandArguments)


mainLoop()
