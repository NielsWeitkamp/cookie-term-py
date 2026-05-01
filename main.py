import os

from colorama import *

nameInCommand = True
factoryName = "CookieFactory"
cookieAmount = 0
cookieClickValue = 1
buildings = {
    "cursor": {"price": 15, "amount": 0, "generationAmount": 0.1, "available": True},
    "grandma": {"price": 100, "amount": 0, "generationAmount": 1, "available": False},
    "farm": {"price": 1_100, "amount": 0, "generationAmount": 8, "available": False},
    "mine": {"price": 12_000, "amount": 0, "generationAmount": 47, "available": False},
    "factory": {
        "price": 130_000,
        "amount": 0,
        "generationAmount": 260,
        "available": False,
    },
    "bank": {
        "price": 1_400_000,
        "amount": 0,
        "generationAmount": 1_400,
        "available": False,
    },
    "temple": {
        "price": 20_000_000,
        "amount": 0,
        "generationAmount": 7_800,
        "available": False,
    },
    "wizardtower": {
        "price": 330_000_000,
        "amount": 0,
        "generationAmount": 44_000,
        "available": False,
    },
    "shipment": {
        "price": 5_100_000_000,
        "amount": 0,
        "generationAmount": 260_000,
        "available": False,
    },
    "alchemylab": {
        "price": 75_000_000_000,
        "amount": 0,
        "generationAmount": 1_600_000,
        "available": False,
    },
    "portal": {
        "price": 1_000_000_000_000,
        "amount": 0,
        "generationAmount": 10_000_000,
        "available": False,
    },
    "timemachine": {
        "price": 14_000_000_000_000,
        "amount": 0,
        "generationAmount": 65_000_000,
        "available": False,
    },
    "antimattercondenser": {
        "price": 170_000_000_000_000,
        "amount": 0,
        "generationAmount": 430_000_000,
        "available": False,
    },
    "prism": {
        "price": 2_100_000_000_000_000,
        "amount": 0,
        "generationAmount": 2_900_000_000,
        "available": False,
    },
    "chancemaker": {
        "price": 26_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 21_000_000_000,
        "available": False,
    },
    "fractalengine": {
        "price": 310_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 150_000_000_000,
        "available": False,
    },
    "editedfork": {
        "price": 71_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 1_100_000_000_000,
        "available": False,
    },
    "idleverse": {
        "price": 12_000_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 8_300_000_000_000,
        "available": False,
    },
    "cortexbaker": {
        "price": 1_900_000_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 64_000_000_000_000,
        "available": False,
    },
    "you": {
        "price": 540_000_000_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 512_000_000_000_000,
        "available": False,
    },
}


def mainLoop():
    global cookieAmount
    global cookieClickValue
    global factoryName
    global nameInCommand
    commandInput = "a"
    if nameInCommand == True:
        commandInput = input(f"{factoryName} >>> ")
    elif nameInCommand == False:
        commandInput = input(">>> ")
    mainCommandParts = commandInput.split()

    if not mainCommandParts:
        mainCommand = " "
    else:
        mainCommand = mainCommandParts[0]

    commandArguments = mainCommandParts[1:]

    match mainCommand:
        case "cookie":
            if not commandArguments:
                print(
                    Fore.RED + "error:",
                    Style.RESET_ALL + "no operation specified (use -h for help)",
                )
            elif commandArguments[0] in ["-h", "--help"]:
                print(
                    "usage:  cookie <operation> [...] \noperations: \n    cookie {-h - -help}\n    cookie {-c - -click} \n    cookie {-am - -amount}"
                )
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

        case "buildings" | "building":
            if not commandArguments:
                print(
                    Fore.RED + "error:",
                    Style.RESET_ALL + "no operation specified (use -h for help)",
                )
            if commandArguments[0] in ["-b", "--buy"]:
                print(mainCommandParts[2])
            elif commandArguments[0] in ["-l", "--list"]:
                for name, data in buildings.items():
                    if data["available"]:
                        print(name)

        case "name":
            if not commandArguments:
                print(
                    Fore.RED + "error:",
                    Style.RESET_ALL + "no operation specified (use -h for help)",
                )
            elif commandArguments[0] in ["-r", "--rename"]:
                if not commandArguments[1:]:
                    print(
                        Fore.RED + "error:",
                        Style.RESET_ALL + "enter a name for your factory",
                    )
                else:
                    factoryName = commandArguments[1]
                    print(f"Your factory is now called {factoryName}")
            elif commandArguments[0] in ["-h", "--help"]:
                print(
                    "usage: name <operation> [...]\n    name {-h - -help}\n    name {-r - -rename} \n    name {-p - -print}\n    {-s - -show}"
                )
            elif commandArguments[0] in ["-s", "--show"]:
                if not commandArguments[1:]:
                    if nameInCommand == True:
                        nameInCommand = False
                        print("Factory name hidden!")
                    elif nameInCommand == False:
                        nameInCommand = True
                        print("Factory name shown!")
                elif commandArguments[1] == "true":
                    nameInCommand = True
                    print("Factory name shown!")
                elif commandArguments[1] == "false":
                    nameInCommand = False
                    print("Factory name hidden!")
            elif commandArguments[0] in ["-p", "--print"]:
                print(f"The name of your factory is: {factoryName}")

        case "clear":
            if os.name == "posix":
                _ = os.system("clear")
            else:
                _ = os.system("cls")

        case "exit":
            quit()

        case " ":
            print("no comment")

        case _:
            print(f"{mainCommand}: no command found")
    mainLoop()


mainLoop()
