from colorama import *

cookieAmount = 0
cookieClickValue = 1
buildings = {
    "cursor": {"price": 15, "amount": 0, "generationAmount": 0.1},
    "grandma": {"price": 100, "amount": 0, "generationAmount": 1},
    "farm": {"price": 1_100, "amount": 0, "generationAmount": 8},
    "mine": {"price": 12_000, "amount": 0, "generationAmount": 47},
    "factory": {"price": 130_000, "amount": 0, "generationAmount": 260},
    "bank": {"price": 1_400_000, "amount": 0, "generationAmount": 1_400},
    "temple": {"price": 20_000_000, "amount": 0, "generationAmount": 7_800},
    "wizardtower": {"price": 330_000_000, "amount": 0, "generationAmount": 44_000},
    "shipment": {"price": 5_100_000_000, "amount": 0, "generationAmount": 260_000},
    "alchemylab": {"price": 75_000_000_000, "amount": 0, "generationAmount": 1_600_000},
    "portal": {"price": 1_000_000_000_000, "amount": 0, "generationAmount": 10_000_000},
    "timemachine": {
        "price": 14_000_000_000_000,
        "amount": 0,
        "generationAmount": 65_000_000,
    },
    "antimattercondenser": {
        "price": 170_000_000_000_000,
        "amount": 0,
        "generationAmount": 430_000_000,
    },
    "prism": {
        "price": 2_100_000_000_000_000,
        "amount": 0,
        "generationAmount": 2_900_000_000,
    },
    "chancemaker": {
        "price": 26_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 21_000_000_000,
    },
    "fractalengine": {
        "price": 310_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 150_000_000_000,
    },
    "editedfork": {
        "price": 71_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 1_100_000_000_000,
    },
    "idleverse": {
        "price": 12_000_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 8_300_000_000_000,
    },
    "cortexbaker": {
        "price": 1_900_000_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 64_000_000_000_000,
    },
    "you": {
        "price": 540_000_000_000_000_000_000_000_000,
        "amount": 0,
        "generationAmount": 512_000_000_000_000,
    },
}


def mainLoop():
    global cookieAmount
    global cookieClickValue
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
                    Fore.WHITE + "no operation specified (use -h for help)",
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
                    Fore.WHITE + "no operation specified (use -h for help)",
                )

        case " ":
            print("no comment")

        case _:
            print(mainCommand + ":", "no command found")
    mainLoop()

    print("\n", mainCommand)
    print(commandArguments)


mainLoop()
