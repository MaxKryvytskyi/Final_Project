import pickle
from collections import UserDict
import re

from bot_work import log
from record import Record

class AddressBook(UserDict):
    # Додає в словник экземпляр классу Record
    def add_record(self, record: Record) -> str:
        if record.name.value not in self.keys():
            self.data[record.name.value] = record
            t = str(record) + " "
            return log(f"{t.rstrip()}\nadd successful", "[Bot's answer] ")
        else: return log(f"Contact with name {record.name} already exist. Try add phone command for add extra phone.", "[Bot's answer] ")

    # Ітерується за книгою контактів
    def iterator(self, num:int) -> str:
        result = self.create_page(num)
        if result == None: return log("No saved contacts", "[Bot's answer] ")
        for _, value in result.items(): yield value

    # Розбиває книгу контактів посторінково 
    def create_page(self, num:int) -> dict|None:
        if len(self.data) == 0: return None
        result_list = {}
        count = 1
        page = 1
        new_list1 = []

        for i in self.data.values():
            value_phone = "No phone"
            value_birthday = "No birthday date"
            value_email = "No email"
            value_address = "No address"
           
            name_value = f"{i.name} "
            phone_value = f" { [el.value for el in i.phones] if [el.value for el in i.phones] else value_phone}"
            birthday_value = f"{i.birthday.value.strftime('%d-%m-%Y') if i.birthday else value_birthday}"
            email_value = f"{i.email if i.email else value_email}"
            address_value = f"{i.address if i.address else value_address}"

            new_list = [name_value, phone_value, birthday_value, email_value, address_value]
            new_list1.append(new_list)
            if count == int(num):
                result_list[page] = self.create_print_page(page, new_list1, True)
                new_list1.clear()
                page += 1
                count = 0
            count += 1

        result_list[page] = self.create_print_page(page, new_list1, True)

        return result_list

    # Записує книгу контактів посторінково для виводу в консоль 
    def create_print_page(self, page:int, contacts:list, flag:bool) -> str | None:
        # print(page, contacts, flag)
        result = ""
        n = 12
        pattern = r"[\[\'\'\"\"\]]" 
        if page > 9: n = 11
        elif page > 99: n = 10
        if contacts:
            if flag:
                x = "Page" 
                result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
                result += " {:^92}".format("|" + " "*n +f"{x} {page}" + " "*12 + "|") + "\n"
                result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"
            else:
                x = "Coincidence"
                result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
                result += " {:^92}".format("|" + " "*(n-4) +f"{page} {x}" + " "*9 + "|") + "\n"
                result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"

            for i in range(0, len(contacts)):
                name_value, phone_value, birthday_value, email_value, address_value = contacts[i]
                p = str(phone_value).split(",")
                count = 1 

                if len(p) > 1:
                    for iii in p:
                        new_i = re.sub(pattern, "", iii)
                        if count == 1 and i == 0: result += f"Name : {name_value}\n" + f"Phone {count} : {new_i}\n"
                        else: result += f"Phone {count} :{new_i}\n"
                        count += 1
                    result += f"Birthday : {birthday_value}\n"
                else:
                    new_i = re.sub(pattern, "", phone_value)
                    result += f"Name : {name_value}\n" + f"Phone {count} : {new_i}\n" + f"Birthday : {birthday_value}\n"
                result += f"Email : {email_value}\n" + f"Address : {address_value}\n\n" 
            return result
        return None

    def correct_text(self, text:str):
        new_text = text.split()
        suma = 0
        text = ""
        list_t = []
        for i in new_text:
            suma += len(i) 
            text += i + " "
            if suma > 60:
                list_t.append(text)
                text = ""
                suma = 0
        if text != "":
            list_t.append(text)
        return list_t

    # Виконує пошук в кнізі контактів за ключовим значенням
    def search_contacts(self, name:list) -> str:
        dict_contacts = {}
        text = log(f"Nothing found", "[Bot's answer] ")
        if name:
            num = 0
            for i in name:
                birthday = self.data[i].birthday.value.strftime('%d-%m-%Y') if self.data[i].birthday else log("No birthday date", "[Bot's answer] ")
                phones = self.data[i].phones if self.data[i].phones else log(" No phone", "[Bot's answer] ")
                email = self.data[i].email if self.data[i].email else log("No email", "[Bot's answer] ")
                address = self.data[i].address if self.data[i].address else log("No address", "[Bot's answer] ")
                dict_contacts[num] = [str(self.data[i].name), phones, birthday, email, address]
                num += 1
            text = self.create_print_page(len(dict_contacts), dict_contacts, False)
        
        return text
    
    # Зберігає книгу контактів
    def save_address_book(self, adress_book):
        with open("Save_adress_book.bin", "wb") as file:
            pickle.dump(adress_book, file)

    # Відповідає за завантаження книги контактів яку зберегли минулого разу
    def load_address_book(self): 
        with open("Save_adress_book.bin", "rb") as file:
            deserialized_adress_book = pickle.load(file)
            return deserialized_adress_book
        