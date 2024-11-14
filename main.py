from task import *


# Декоратор для обработки ошибок
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "The arguments are not correct."
        except IndexError:
            return "The arguments are not correct."
    return wrapper

# Парсинг ввода
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функция для добавления контакта
@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

# Функция для изменения контакта
@input_error
def change_contact(args, book):
    name, phone = args
    if name in book:
        book[name] = phone
        return "Contact updated."
    return "Contact not found."

# Функция для отображения телефона по имени
@input_error
def show_phone(args, book):
    return f"[{book[args[0]]}]"

# Функция для отображения всех контактов
@input_error
def show_all(book):
    if not book:
        return "No contacts found."
    return f"All contacts:\n {book}"

# Основная функция
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()