

from todo.todo_manager import ToDoBook
from utils.todosMenu import show_todos_menu
from  utils.chooseCommand import choseCommand
from utils.todo_utils import show_todo, add_todo_record_to_book 

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


class TodosBot:
    def run(self):
        """Main function for user interaction.

               Returns:
                   None
               """
        try:
            book = ToDoBook.load_from_file('outputs/todo.json')
        except (FileNotFoundError, EOFError) as e:
            print(f"{RED}Error loading todos book: {e}{RESET}")
            print(f"{YELLOW}Creating a new todos book.{RESET}")
            book = ToDoBook()  # Creating a new instance
        while True:
            show_todos_menu()
            command = choseCommand()
            if command is False:
                continue

            if command is not None:
                match command:
                    case 1:
                        print(add_todo_record_to_book(book))
                    case 2:
                        book.edit_todo()
                    case 3:
                        book.search_todo()
                    case 4:
                        book.delete_task()
                    case 5:
                        show_todo(book)
                    case 6:
                        print(f"{RED}You have reached the main menu{RESET}")
                        break


            else:
                print(f"{RED}Don't know this command{RESET}")

