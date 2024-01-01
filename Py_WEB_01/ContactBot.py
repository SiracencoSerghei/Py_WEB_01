
from decorators.input_errors import input_errors
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from contacts.AddressBook import AddressBook
from utils.beginning import beginning
from utils.goodbye import good_bye
from utils.contactsMenu import show_contacts_menu
from  utils.chooseCommand import choseCommand

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


#  ================================

class ContactBot:
    def run(self):
        """Main function for user interaction.

               Returns:
                   None
               """
        try:
            book = AddressBook.load_json_from_file('outputs/address_book.json')
        except (FileNotFoundError, EOFError) as e:
            print(f"{RED}Error loading address book: {e}{RESET}")
            print(f"{YELLOW}Creating a new address book.{RESET}")
            book = AddressBook()  # Creating a new instance
        while True:
            show_contacts_menu()
            command = choseCommand()

            if command is not None:
                match command:
                    case 8:
                        print(f"{RED}You have reached the main menu{RESET}")
                        break
                    case 3:
                        book.find()
                    case "show-contact":
                        try:
                            book.show_records(book)
                        except IndexError:
                            pass

                   
                    case 'add-contact':
                        try:
                            pass
                        except IndexError:
                            print(f"{RED}You have to put name(or name-surname) and phone(s) after add-contact. "
                                  f"Example: \n"
                                  f"add-contact <name> <phone1> <phone2> ...{RESET}")
                    
                    case 'edit-contact':
                        pass
                        
                    case 'delete-contact':
                        pass


                    case "days-to-birthday":
                        if len(input_data) < 2:
                            print(
                                f"{RED}You need to provide a name after 'days-to-birthday'. "
                                f"Example: days-to-birthday <name>{RESET}"
                            )
                        else:
                            pass


            else:
                print(f"{RED}Don't know this command{RESET}")


if __name__ == '__main__':
    bot = ContactBot()
    bot.run()
