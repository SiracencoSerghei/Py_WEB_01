from todo.todo_manager import ToDoRecord
from todo.todo_manager import ToDoBook
from rich.console import Console
from rich.table import Table

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


filename = 'outputs/todo.json'
def load_todo_from_file():
    try:
        return ToDoBook.load_from_file('outputs/todo.json')
    except (FileNotFoundError, EOFError) as e:
        print(f"{RED}Error loading To Do List: {e}{RESET}")
        print(f"{YELLOW}Creating a new To Do entrance.{RESET}")
        return ToDoBook()  # Creating a new instance

def add_todo_record_to_book(todobook):
    
    task = input("Enter the task name: ")
    begin = input("Enter the begin date in format YYYY-MM-DD: ")
    end = input("Enter the end date in format YYYY-MM-DD: ")
    status = input("Enter the status of task: ")
    tags = input("Enter the tags for this task: ")
    
    tags = tags.split(" ")
    print("TAGS: ", tags)
    
    
    record = ToDoRecord(task, begin, end, status, tags)
    if record is None:
        record = ToDoRecord()
    print("tags:  ", record.tags)
    print("r: ", record)
    
    todobook.add_to_do_record(record)

    todobook.save_to_file_todo('outputs/todo.json')
    return f"{GREEN}Task {task} was added successfully!{RESET}"


def show_todo(todobook):
    console = Console()
    table = Table(title="To Do List")
    table.add_column("Task", style="#5cd15a", justify="center", min_width=10, max_width=10)
    table.add_column("Begin Date", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("End Date", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("Status", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("Tags", style="#5cd15a", justify="center", min_width=10, max_width=50)
    
    for task, value in todobook.data.items():
        begin = value.begin
        end = value.end
        status = value.status
        tags = ", ".join(str(tag) for tag in value.tags)
        tags = tags.strip("[]")  # Remove square brackets
        table.add_row(str(task), str(begin), str(end), str(status), str(tags))
        table.add_row("-" * 10, "-" * 10, "-" * 10, "-" * 10, "-" * 10, style="#5cd15a")
    console.print(table)
