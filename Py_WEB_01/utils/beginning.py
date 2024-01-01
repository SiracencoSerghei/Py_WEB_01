from utils.actions import run_contact_bot
from utils.botMenuOutput import botMenuPrinting

def beginning():

    while True:
        botMenuPrinting()
        action = int(input("What action do you want to choose?\n \t"))

        if action == 1:
            run_contact_bot()
        elif action == 2:
            print("1_2")
        elif action == 3:
            print(3)
        elif action == 4:
            break
        elif action == 5:
            break
            # help()
        elif action == 6:
            break

