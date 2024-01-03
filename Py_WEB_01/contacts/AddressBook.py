import json
import pathlib
from collections import UserDict
from contacts.Record import Record
from contacts.congratulates import print_week_bdays
from datetime import date, datetime
from rich.console import Console
from rich.table import Table

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


class AddressBook(UserDict):
    """A class representing an address book that stores records."""
    

    def add_contact(self):
        """
        Додати новий запис до адресної книги з введеними користувачем даними.

        Returns:
            None
        """
        while True:
            try:
                name = input("Enter the name(optional, press Enter to exit): ").strip()

                # Check if the name is provided
                if not name:
                    print("Exiting without creating a record.")
                    break
                else:
                    birthday = input("Enter the birthday (optional, press Enter to skip): ").strip() or None
                    email = input("Enter the email (optional, press Enter to skip): ").strip() or None
                    address = input("Enter the address (optional, press Enter to skip): ").strip() or None
                    status = input("Enter the status (optional, press Enter to skip): ").strip() or None
                    note = input("Enter the note (optional, press Enter to skip): ").strip() or None

                    new_record = Record(name, birthday, email, address, status, note)
                # Додавання телефонів
                while True:
                    phone_input = input("Enter a phone number (press Enter to finish adding phones): ").strip()
                    if not phone_input:
                        break
                    new_record.add_phone(phone_input)

                self.add_record(new_record)
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    def add_record(self, record):
        """Add a record to the address book.

        Args:
            record (Record): The record to add.

        Returns:
            None
        """
        if not isinstance(record, Record):
            record = Record(record)
        self.data[record.name.value] = record
        self.save_to_json_file()

    @staticmethod
    def convert_to_json(address_book):
        """Converts the AddressBook object to a serializable format.

        Args:
            address_book (AddressBook): The AddressBook object to convert.

        Returns:
            dict: A dictionary containing the serialized data.
        """
        json_data = {}
        for key, record in address_book.items():
            json_data[key] = {
                "name": record.name.value,
                "phones": record.get_all_phones()if record.get_all_phones() else None,
                "birthday": str(record.birthday) if record.birthday else None,
                "email": record.email if record.email else None,
                "address": record.address if record.address else None,
                "status": record.status if record.status else None,
                "note": record.note if record.note else None
            }
        return json_data

    def save_to_json_file(self):
        """
        Save the instance to a JSON file.

        Args:
            file_name (str): The name of the file to save the instance. The extension will determine the format.

        Returns:
            None
        """
        file_name = "outputs/address_book.json"
        data_to_json = self.convert_to_json(self)

        try:
            with open(file_name, "w", encoding="utf-8") as json_file:
                json.dump(data_to_json, json_file, indent=4)
            # print("Successfully saved to", file_name)
        except Exception as e:
            print(f"Error saving to {file_name}: {e}")

    def del_record(self):
        """Delete a record from the address book.

        Args:
            name_to_delete (str): The name of the record to delete.

        Returns:
            None
        """
        name_to_delete = input("Enter the name to delete(optional, press Enter to exit): ").strip()

        # Check if the name is provided
        if not name_to_delete:
            print("Exiting without deleting.")
            return

        try:
            if name_to_delete in self.data:
                del self.data[name_to_delete]
                self.save_to_json_file()  # Save changes to file
                print(f"{GREEN}Contact '{name_to_delete}' deleted successfully{RESET}")
            else:
                print(f"{RED}No contact found with the name '{name_to_delete}'{RESET}")
        except Exception as e:
            print(f"{RED}Error deleting contact: {e}{RESET}")

    

    @staticmethod
    def load_json_from_file(file_name):
        """
        Load an instance from a JSON file.

        Args:
            file_name (str): The name of the file to load the instance from.

        Returns:
            AddressBook: The loaded instance.
        """
        try:
            # with open(file_name, "r", encoding="utf-8") as f:
            #     data = f.read()
            #     print(data)
            #     if not data:
            #         return AddressBook()
            #     data = json.loads(data)
                
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
            address_book = AddressBook()
            for _, record_data in data.items():
                new_record = Record(record_data.get("name", ""))
                phones = record_data.get("phones", [])
                if phones is not None:
                    for phone in phones:
                        new_record.add_phone(phone)
                new_record.birthday = record_data.get("birthday", None)
                new_record.email = record_data.get("email", None)
                new_record.address = record_data.get("address", None)
                new_record.status = record_data.get("status", None)
                new_record.note = record_data.get("note", None)
                address_book.add_record(new_record)

            return address_book
        except (FileNotFoundError, EOFError):
            # Handle the case where the file is not found or empty
            return AddressBook()
        
    @staticmethod
    def show_records(book):
        """Display all contacts in the address book.

        Returns:
            None
        """
        console = Console()
        table = Table(title="Address Book")
        
        first_record = next(iter(book.data.values()), None)

        record_attributes = list(first_record.__dict__.keys())
        # Add columns dynamically based on the attributes
        for attribute in record_attributes:
            column_name = attribute.capitalize()  # Convert attribute name to title case
            table.add_column(column_name, style="blue", justify="center", min_width=10, max_width=30)

        for _, record in book.items():
            # Get attribute values dynamically
            row_data = []
            for attr in record_attributes:
                value = getattr(record, attr)

                # Check if the value is printable
                if hasattr(value, '__iter__') and not isinstance(value, str):
                    # If it's an iterable (like a list or tuple), join its elements
                    row_data.append("; ".join(map(str, value)))
                else:
                    # Otherwise, convert the value to a string
                    row_data.append(str(value))

            table.add_row(*row_data)

        console.print(table)


    def find(self) -> UserDict:
        """
        Find records that match the given parameter.

        Args:
            param (str): The search parameter.

        Returns:
            str: A string containing the matching records, separated by newline.

        Note:
            If the search parameter is less than 3 characters, it returns an error message.
        """
        while True:
            try:
                print("To find what you are looking for...")
                param = input("Enter search parameter (optional, press Enter to exit): ")
                if not param:
                    break

                if len(param) < 3:
                    print(f"{PINK}Sorry, the search parameter must be at least 3 characters.{RESET}")
                    continue
                result = UserDict()

                for i, record in enumerate(self.data.values()):
                    if param.lower() in record.name.value.lower():
                        result[record.name.value] = record
                    elif param.isdigit():
                        matching_phones = [
                            phone for phone in record.get_all_phones() if param in phone
                        ]
                        if matching_phones:
                            result[record.name.value] = record
                    elif record.birthday and param in str(record.birthday):
                        result[record.name.value] = record
                    elif record.email and param.lower() in record.email.lower():
                        result[record.name.value] = record
                    elif record.address and param.lower() in record.address.lower():
                        result[record.name.value] = record
                    elif record.status and param.lower() in record.status.lower():
                        result[record.name.value] = record
                    elif record.note and param.lower() in record.note.lower():
                        result[record.name.value] = record

                if not result:
                    print("No records found for the given parameter.")
                    return

                # self.show_records(result)
                return result


            except Exception as e:
                print(f"{RED}{e}{RESET}")


    
    def edit_contact(self):
        print("Now you have to choose edit parameter...")
        searched_contacts = self.find()
        print("searched_contacts: ", searched_contacts)
        print(" TYPE OF searched_contacts: ", type(searched_contacts))
        if not searched_contacts:
            return
        matching_records = []
        for i, record in enumerate(searched_contacts, start=1):
            print(f"\n{i}. {record}\n\t")
            print(self.data[record])
            matching_records.append(record)
            print("matching_records: ", matching_records)
            
        try:
            choice = input("Enter the contact's number to edit(optional, press Enter to exit):.... ")
            if choice == "":
                return
            choice = int(choice)
            if 1 <= choice <= len(matching_records):
                selected_name_of_record = matching_records[choice - 1]
                print("1:  ", selected_name_of_record)
                selected_record = searched_contacts[selected_name_of_record]
                print("2: ", selected_record)
                while True:
                    try:
                        console = Console()
                        table = Table(title="Record Fields:")
                        first_record = next(iter(self.data.values()), None)

                        record_attributes = list(first_record.__dict__.keys())
                        # Add columns dynamically based on the attributes
                        table.add_column("Number", justify="center")
                        table.add_column("Column Name", justify="center")
                        for i, attribute in enumerate(record_attributes, start=1):
                            column_name = f"  {attribute.capitalize()}"
                            table.add_row(str(i), column_name)

                        console.print(table)

                        
                        field_name = input("Choose the field for Editing (optional, press Enter to exit)...")
                        if field_name == "":
                            return
                        field_name = int(field_name)

                        fields = {
                            1: "name",
                            2: "birthday",
                            3: "phones",
                            4: "email",
                            5: "address",
                            6: "status",
                            7: "note",
                        }
                        print(field_name)
                        print(type(field_name))
                        print(fields.keys())
                        print(type(list(fields.keys())[0])) 

                        if field_name in fields:
                            field_key = fields[field_name]
                            print(field_key)
                            if field_name == 3:
                                old_phone = input(f"Enter the old phone: ")
                                new_phone = input(f"Enter the new phone: ")
                                selected_record.edit_phone(old_phone, new_phone)
                            else:
                                new_value = input(f"Enter the new {field_key}: ")
                                setattr(selected_record, field_key, new_value)
                            self.save_to_json_file()
                        else:
                            print("Invalid field number.")
                    except ValueError:
                        print("You must choose valid number!")
                        continue

                                        

                # After editing, save the changes to the file
                self.save_to_json_file()
                print(f"Contact '{selected_record.name.value}' updated successfully.")

            else:
                print("Invalid choice. Please enter a valid number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def days_to_birthday(self):
        if self:
            # Создаем список кортежей (record_name, days_to_birthday)
            results = [(record.name.value, record.days_to_birthday()) for record in self.data.values()
                       if record.birthday]

            # Сортируем список по второму элементу (количество дней до дня рождения)
            sorted_results = sorted(results, key=lambda x: x[1])

            # Выводим результаты
            for name, days in sorted_results:
                print(f"{name} - have {days} days to birthday")
        else:
            print('No date matched...')


    def congratulate(self):
        if self:
            
            # Создаем список словарей в формате users_list
            
            results = [{"name": record.name.value, "birthday": datetime.strptime(record.birthday, '%Y-%m-%d').date()} for record in self.data.values()
                    if record.birthday]

            # Сортируем список по второму элементу (дата рождения)
            sorted_results = sorted(results, key=lambda x: x["birthday"])

            # Выводим результаты
            print_week_bdays(sorted_results)
        else:
            print('No date matched...')
    


    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


if __name__ == "__main__":
    print("Loading address book from file...")
    book = AddressBook.load_json_from_file("../outputs/address_book.json")
    # print(book)
    # for nam, record in book.items():
    #     print(nam)
    #     print("==============")
    #     print(record)
    #     print("+++++++++++++++++++++++++++++++++++")
    # book.show_records(book)
    req = book.find('333')
    book.show_records(req)
    # rec = book.find("ser")
    # book.show_records(rec)
