
from notes.note_manager import Notes
from utils.notesMenu import show_notes_menu
from  utils.chooseCommand import choseCommand
from utils.notes_utils import show_notes, add_note_record_to_notes

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


class NotesBot:
    def run(self):
        """Main function for user interaction.

               Returns:
                   None
               """
        try:
            book = Notes.load_from_file('outputs/notes.json')
        except (FileNotFoundError, EOFError) as e:
            print(f"{RED}Error loading notes book: {e}{RESET}")
            print(f"{YELLOW}Creating a new notes book.{RESET}")
            book = Notes()  # Creating a new instance
        while True:
            show_notes_menu()
            command = choseCommand()
            if command is False:
                continue

            if command is not None:
                match command:
                    case 1:
                        print(add_note_record_to_notes(book))
                    case 2:
                        book.search_notes_record()
                    case 3:
                        show_notes(book)
                    case 4:
                        book.delete_note()
                    case 5:
                        show_notes(book)
                    case 6:
                        
                        book.congratulate()
                        

                    case 7:
                        book.days_to_birthday()

                    case 8:
                        print(f"{RED}You have reached the main menu{RESET}")
                        break


            else:
                print(f"{RED}Don't know this command{RESET}")

