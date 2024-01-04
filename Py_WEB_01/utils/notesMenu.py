


from rich.console import Console
from rich.table import Table

def show_notes_menu():
    console = Console()
    table = Table()
    column_name = "Notes Menu:"
    table.add_column(column_name, style="blue", justify="left", min_width=10, max_width=30)

    menu_commands = ("1. add-note",
                     "2. edit-note",
                     "3. find-in-notes",
                     "4. delete-note",
                     "5. show-notes",
                     "8. exit")
    for row in menu_commands:
        table.add_row(row)
    console.print(table)
