from collections import UserDict
import pickle


from rich.table import Table

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


    # Ітерується за книгою контактів
    def iterator(self, num:int) -> str:
        result = self.create_page(num)
        if result == None: return "No saved contacts"
        for value in result: yield value


    # Розбиває книгу контактів посторінково 
    def create_page(self, num:int) -> dict|None:
        if len(self.data) == 0: return None
        result_list = []
        page = 1
        count = 0
        work = True

        for i in self.data.values():
            count +=1
            if work:
                table = Table(title=f"Page {page}")
                table.add_column("Name", justify="center", style="cyan", no_wrap=True)
                table.add_column("Phones", justify="center", style="magenta", no_wrap=True)
                table.add_column("Emails", justify="center", style="cyan", no_wrap=True)
                table.add_column("Birthday", justify="center", style="cyan", no_wrap=True)
                table.add_column("Status", justify="center", style="cyan", no_wrap=True)
                table.add_column("Address", justify="center", style="cyan", no_wrap=True)
                table.add_column("Note", justify="center", style="cyan", no_wrap=True)

            table.add_row(f"{i.name.value_of()}", 
                          f"{[el.value_of() for el in i.phones] if [el.value_of() for el in i.phones] != [''] else ''}", 
                          f"{[el.value_of() for el in i.emails] if [el.value_of() for el in i.emails] != [''] else ''}",
                          f"{i.birthday.value_of()}",
                          f"{i.status.value_of()}",
                          f"{i.address.value_of()}",
                          f"{i.note.value_of()}")
            
            work = False
            if count == len(self.data):
                result_list.append(table)
                return result_list
            if count == num: 
                result_list.append(table)
                count = 0
                page += 1
                work = True
     
        
        result_list.append(table)
        return result_list


    # # Виконує пошук в кнізі контактів за ключовим значенням
    # def search_contacts(self, name:list) -> str:
    #     dict_contacts = {}
    #     text = f"Nothing found"
    #     if name:
    #         num = 0
    #         for i in name:
    #             birthday = self.data[i].birthday.value.strftime('%d-%m-%Y') if self.data[i].birthday else "No birthday date"
    #             phones = self.data[i].phones if self.data[i].phones else " No phone"
    #             email = self.data[i].email if self.data[i].email else "No email"
    #             address = self.data[i].address if self.data[i].address else "No address"
    #             dict_contacts[num] = [str(self.data[i].name), phones, birthday, email, address]
    #             num += 1
    #         text = self.create_print_page(len(dict_contacts), dict_contacts, False)
        
    #     return text
