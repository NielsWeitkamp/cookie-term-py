from colorama import *

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

        case "info":
            print(
                "Welcome to terminal cookie clicker!\nType help into the terminal for help\nIt's based on / copied from Orteil's cookie clicker.\n(you can find it on https://orteil.dashnet.org/cookieclicker )"
            )

        case "help":
            if not commandArguments:
                print(
                    "You play this game through commands you can type into the terminal.\nType help --commmands for a list of commands"
                )
            elif commandArguments[0] in ["-c", "--commands"]:
                print(
                    "Command list:\n    cookie [args: --help, --click, --amount]\n    info\n    "
                )

        case "buildings":
            if not commandArguments:
                print(
                    Fore.RED + "error:",
                    Fore.WHITE + "no operation specified (use -h for help)",
                )
    mainLoop()

    print("\n", mainCommand)
    print(commandArguments)


mainLoop()
