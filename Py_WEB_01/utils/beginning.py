from utils.actions import run_contact_bot
from utils.actions import run_notes_bot
from utils.botMenuOutput import botMenuPrinting
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def beginning():

    while True:
        botMenuPrinting()
        try:
            action = int(input(f"{GREEN}What action do you want to choose?\n \t{RESET}"))
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid integer.{RESET}")

        if action == 1:
            run_contact_bot()
        elif action == 2:
            run_notes_bot()
        elif action == 3:
            print(3)
            #     run_todos_bot()
        elif action == 4:
            break
            #     run_file_manager()
        elif action == 5:
            break
            # help()
        elif action == 6:
            # goodbye()
            break

        else:
            continue
