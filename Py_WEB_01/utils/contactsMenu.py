

from rich.console import Console
from rich.table import Table

def show_contacts_menu():
    console = Console()
    table = Table()
    column_name = "Address Book Menu:"
    table.add_column(column_name, style="blue", justify="left", min_width=10, max_width=30)

    menu_commands = ("1. add-contact",
                     "2. edit-contact",
                     "3. find-in-contacts",
                     "4. delete-contact",
                     "5. show-records",
                     "6. congratulate",
                     "7. days-to-birthday",
                     "8. exit")
    for row in menu_commands:
        table.add_row(row)
    console.print(table)
