
from notes.note_manager import Notes
from utils.notesMenu import show_notes_menu
from  utils.chooseCommand import choseCommand
from utils.notes_utils import load_notes_from_file, add_note_record_to_notes, show_notes

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
                        book.add_note_record_to_notes()
                    case 2:
                        book.edit_note()
                    case 3:
                        try:
                            book = Notes.load_from_file('outputs/notes.json')
                            show_notes(book)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case 4:
                        book.delete_notes()
                    case 5:
                        try:
                            book = Notes.load_from_file('outputs/notes.json')
                            show_notes(book)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case 6:
                        
                        book.congratulate()
                        

                    case 7:
                        book.days_to_birthday()

                    case 8:
                        print(f"{RED}You have reached the main menu{RESET}")
                        break


            else:
                print(f"{RED}Don't know this command{RESET}")

