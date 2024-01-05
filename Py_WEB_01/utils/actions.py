
def run_contact_bot():
    from ContactBot import ContactBot
    bot = ContactBot()
    bot.run()

def run_notes_bot():
    from NotesBot import NotesBot
    bot = NotesBot()
    bot.run()

def run_todos_bot():
    from TodosBot import TodosBot
    bot = TodosBot()
    bot.run()
    
def run_file_manager():
    from FileManagerBot import FileManagerBot
    bot = FileManagerBot()
    bot.run()