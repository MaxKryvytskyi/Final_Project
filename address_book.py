from collections import UserDict
import pickle

from person import Person


class AddressBook(UserDict):
    # Додає в словник экземпляр классу Record
    def add_person(self, person: Person) -> str:
        self.data[person.name.value] = person
        return f"Контакт {person.name.value_of()} доданий"


        # Зберігає книгу контактів
    def save_address_book(self, adress_book):
        with open("Save_adress_book.bin", "wb") as file:
            pickle.dump(adress_book, file)


    # Відповідає за завантаження книги контактів яку зберегли минулого разу
    def load_address_book(self): 
        with open("Save_adress_book.bin", "rb") as file:
            deserialized_adress_book = pickle.load(file)
            return deserialized_adress_book

