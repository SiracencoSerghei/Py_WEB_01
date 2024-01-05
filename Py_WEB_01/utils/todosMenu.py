
from rich.console import Console
from rich.table import Table

def show_todos_menu():
    console = Console()
    table = Table()
    column_name = "To Do Menu:"
    table.add_column(column_name, style="blue", justify="left", min_width=10, max_width=30)

    menu_commands = ("1. add-todo",
                     "2. edit-todo",
                     "3. find-in-todo's",
                     "4. delete-todo",
                     "5. show-todo's",
                     "6. exit")
    for row in menu_commands:
        table.add_row(row)
    console.print(table)
