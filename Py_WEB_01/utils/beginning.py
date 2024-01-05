from utils.actions import run_contact_bot
from utils.actions import run_notes_bot
from utils.actions import run_todos_bot
from utils.actions import run_file_manager
from utils.botMenuOutput import botMenuPrinting
from utils.help import help
from utils.goodbye import good_bye

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
            run_todos_bot()
        elif action == 4:
            run_file_manager()
        elif action == 5:
            help()
            continue
        elif action == 6:
            good_bye()
            break

        else:
            continue
