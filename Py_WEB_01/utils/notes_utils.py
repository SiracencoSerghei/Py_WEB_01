from notes.note_manager import NotesRecord
from notes.note_manager import Notes
from decorators.input_errors import input_errors
from rich.console import Console
from rich.table import Table

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"
BOLD_RED_UNDERLINE = "\033[1;91;4m"
START_UNDERLINE = "\033[4m"
STOP_UNDERLINE = "\033[24m"
START_BOLD = "\033[1m"
STOP_BOLD = "\033[21m"


filename = 'outputs/notes.json'
def load_notes_from_file():
    try:
        return Notes.load_from_file('outputs/notes.json')
    except (FileNotFoundError, EOFError) as e:
        print(f"{RED}Error loading address book: {e}{RESET}")
        print(f"{YELLOW}Creating a new address book.{RESET}")
        return Notes()  # Creating a new instance

@input_errors
def add_note_record_to_notes(notesbook):
    """Add a note to the notes book.

    Args:
        book (NotesBook): The NotesBook instance.
        title (str): The title of the note.
        *notes (str): One or more notes to associate with the note.

    Returns:
        str: A message indicating the result of the operation.
    """
    title = input("Enter the title name: ... ")
    notes = input("Enter the notes for saving(dial separated by space): ... ")

    # Create a NotesRecord object
    record = NotesRecord(title)
    record.add_notes(notes)
    # Add the NotesRecord to the Notes instance
    notesbook.add_note_record(record)
    
    # Display the added record
    print("New added record is:")
    print(f'Title: {record.title}')
    print(f'Notes: {record.notes}')
    notesbook.save_to_file_notes('outputs/notes.json')
    return f"Note '{title}' was added successfully!"



def edit_note_in_book(book):
    title = input("Enter the title of the note to edit: ")
    if title in book.data:
        note_record = book.data[title]
        new_title = input(f"Enter a new title for the note (press Enter to keep '{title}'): ")
        new_notes = input(f"Enter new notes for the note (press Enter to keep the existing notes): ")
        note_record.edit_notes(new_title or title, new_notes)
        print(f'Note "{title}" has been edited successfully.')
    else:
        print(f'Note "{title}" not found in the book.')


def delete_note_from_book(book):
    title = input("Enter the title of the note to delete: ")
    book.delete_note_record(title)

def show_notes(notebook):
    """Display all contacts in the address book.

    Returns:
        None
    """
    console = Console()

    table = Table(title="Notes Book")
    table.add_column("Title", style="blue", justify="center", min_width=10, max_width=50)
    table.add_column("Notes", style="blue", justify="center", min_width=10, max_width=50)
    
    for record in notebook.data.values():
        table.add_row(record.title, str(record.notes))
        table.add_row("=" * 50, "=" * 50)
    console.print(table)

