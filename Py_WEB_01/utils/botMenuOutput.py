
from rich.tree import Tree
from rich import print as rprint

def botMenuPrinting():
    tree = Tree("    =============")
    tree.add(" Menu Options ")
    tree.add("=============")

    options = ["1. Contacts", "2. Notes", "3. ToDo's", "4. File Manager", "5. Help", "6. Exit"]
    colors = ["red", "blue", "green", "yellow", "cyan", "red", "blue", "green", "yellow", "cyan"]

    for i in range(len(options)):
        tree.add(f"[{colors[i]}] {options[i]}")

    rprint(tree)