from utils.actions import run_contact_bot
from rich.tree import Tree
from rich import print as rprint


def beginning():
    tree = Tree("    =============")
    tree.add(" Menu Options ")
    tree.add("=============")

    options = ["1. Contacts", "2. Notes", "3. ToDo's", "4. Help", "5. Exit"]
    colors = ["red", "blue", "green", "yellow", "cyan"]

    for i in range(len(options)):
        tree.add(f"[{colors[i]}] {options[i]}")

    while True:
        rprint(tree)
        action = int(input("What action do you want to choose?\n \t"))

        if action == 1:
            run_contact_bot()
            
        elif action == 2:
            print("1_2")
        elif action == 3:
            print(3)
            # help()
        elif action == 4 or action == 5:
            break

