

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def choseCommand():
    user_input = input("Choose command number... ")
    user_input_without_spaces = user_input.replace(" ", "")  # видаляємо пробіли

    if len(user_input_without_spaces) > 0:
        try:
            input_command = int(user_input_without_spaces)
            print(f"{GREEN}Command entered: {input_command}{RESET}")
            return input_command
        except ValueError as e:
            print("Please, enter the number.")
    else:
        print(f"{RED}Empty input !!!{RESET}")
        return False
