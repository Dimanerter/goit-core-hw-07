from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError(f"Invalid phone number: {value}")
        super().__init__(value)
    
    def is_valid_phone(self, value):
        return value.isdigit() and len(value) == 10


class Birthday(Field):
    def __init__(self, value):
        try:
            self.birthday = datetime.strptime(value, "%d.%m.%Y")
            print(self.birthday)
            pass
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # реалізація класу
    def add_phone(self, phone_string):
        self.phones.append(Phone(phone_string))
    
    def remove_phone(self, phone_string):
        phone = self.find_phone(phone_string)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone number {phone_string} not found")

    def edit_phone(self, old_phone_number, new_phone_number):
        old_phone = self.find_phone(old_phone_number)
        if old_phone:
            self.add_phone(new_phone_number)
            self.remove_phone(old_phone_number)
        else:
            raise ValueError(f"Phone number {old_phone_number} not found")

    def find_phone(self, phone_string):
        for phone in self.phones:
            if phone.value == phone_string:
                return phone
        return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name_string):
        return self.data.get(name_string, None)
    # реалізація класу
    def delete(self,name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact with name {name} not found")

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книгиjohn_record.add_phone("5555555555")

book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")