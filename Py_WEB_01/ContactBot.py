
from decorators.input_errors import input_errors
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from contacts.AddressBook import AddressBook
from utils.beginning import beginning
from utils.goodbye import good_bye


RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


#  ================================

class ContactBot:
    # noinspection PyTypeChecker
    def __init__(self):
        self.__known_commands = ("add-contact", "edit-contact", "find-in-contacts", "delete-contact",
                                 "show-contact", "days-to-birthday", "exit")
        self.session = PromptSession(
            history=FileHistory('outputs/history.txt'),
            completer=WordCompleter(self.__known_commands),
        )


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
            user_input = self.session.prompt("... ")
            if user_input == "":
                print(f"{RED}Empty input !!!{RESET}")
                continue
            input_data = user_input.split()
            input_command = input_data[0].lower()
            if input_command in self.__known_commands:
                match input_command:
                    case 'exit':
                        print(f"{RED}{good_bye()}{RESET}")
                        break
                    case "find-in-contacts":
                        try:
                            search_param = input("Enter search parameter: \t...")
                            book.find(search_param)
                            
                        except IndexError:
                            print(f"{RED}You have to provide a search parameter after 'find'.{RESET}")

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
