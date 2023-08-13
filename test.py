import re
from collections import UserDict
from my_exception import ExceptionIncorrectFormat
from datetime import datetime
import pickle


class PersonFormatterInfo:

    def value_of(self):
        raise NotImplementedError
    
    
class PersonName(PersonFormatterInfo):
    def __init__(self, value: str):
        self.__value = None
        self.value = value

    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if len(value) >= 3: self.__value = value.capitalize()
        else: raise ExceptionIncorrectFormat(f"Ім'я \"{value}\" занадто кототке потрібно минимум 3 символи")

    def value_of(self):
        return f"{self.value}"


class PersonPhoneNumbers(PersonFormatterInfo):
    def __init__(self, value: str="None"):
        self.__value = None
        self.value = value

    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value and value.lower() != "none":
            if not value.isdigit():
                raise ExceptionIncorrectFormat(f"Телефон {value} має складатися тільки з літер")
            if len(value) == 10: self.__value = value # "012 3456789"
            else: raise ExceptionIncorrectFormat(f"Не правильний формат телефону {value} очікуєтся 0500000000")
        else: self.__value = "none"
    
    def value_of(self):
        return f"{'+38' if self.value.lower() != 'none' else ''}{self.value if self.value.lower() != 'none' else ''}"
    

class PersonEmailAddress(PersonFormatterInfo):
    def __init__(self, value: str="None"):
        self.value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value and value.lower() != "none":
            if value == None: 
                self.__value = "none"
            verified = str(*re.findall(r"[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", value))
            if verified: 
                self.__value = verified
            else: 
                raise ExceptionIncorrectFormat(f"Не правильний формат email {value} очікувалося m.k@gmail.com")
        else: self.__value = "none"
    
    def value_of(self):
        return f"{self.value if self.value.lower() != 'none' else ''}"


class PersonStatus(PersonFormatterInfo):
    def __init__(self, value: str="None"):
        self.value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value and value.lower() != "none":
            if value.lower() in ["work", "family", "friend"]:
                self.__value = value
        else: self.__value = "none"
    
    def value_of(self):
        return f"{self.value.capitalize() if self.value.lower() != 'none' else ''}"

class PersonAddress(PersonFormatterInfo):
    def __init__(self, city: str="None", street: str="None", house: str="None"):
        self.city = city
        self.street = street
        self.house = house
    
    def value_of(self):
        return f"City: {self.city + ',' if self.city.lower() != 'none' else ''} Street: {self.street + ',' if self.street.lower() != 'none' else ''} House: {self.house + '.' if self.house.lower() != 'none' else ''}"
    

class PersonBirthday(PersonFormatterInfo):
    def __init__(self, value: str="None"):
        self.value = None
        self.value = value
    
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value and value.lower() != "none":
            birthday = datetime.strptime(value, r'%d.%m.%Y')
            if birthday: 
                self.__value = value
            else: raise ExceptionIncorrectFormat(f"Не правильний формат дати {value} очікувалося день.місяць.рік")
        else: self.__value = "none"


    def value_of(self):
        return f"{self.value if self.value.lower() != 'none' else ''}"
    

class PersonNote(PersonFormatterInfo):
    def __init__(self, value: str="None"):
        self.value = value
    
    def value_of(self):
        return f"{self.value if self.value.lower() != 'none' else ''}"

class Person:
    def __init__(self, name: PersonFormatterInfo="None", phone: PersonFormatterInfo="None", email: PersonFormatterInfo="None", birthday: PersonFormatterInfo="None", status: PersonFormatterInfo="None", address: PersonFormatterInfo="None", note: PersonFormatterInfo="None") -> None:
        self.name = name
        self.phones = []
        self.emails = [] 
        self.birthday = birthday
        self.status = status
        self.address = address
        self.note = note
        self.phones.append(phone)
        self.emails.append(email)

    def add_phone(self, new_phone: PersonFormatterInfo):
        if "none" in [phone.value for phone in self.phones]: 
            self.phones[0] = new_phone
        else: self.phones.append(new_phone)

    def add_email(self, new_email: PersonFormatterInfo):
        if "none" in [email.value for email in self.emails]: 
            self.emails[0] = new_email
        else: self.emails.append(new_email)

    def add_birthday(self, new_birthday: PersonFormatterInfo):
        pass

    def add_status(self, new_status: PersonFormatterInfo):
        pass

    def add_address(self, new_address: PersonFormatterInfo):
        pass

    def add_note(self, new_note: PersonFormatterInfo):
        pass

    def get_person_info(self):
        return f"Name: {self.name.value_of()}\nPhones: {[phone.value_of() for phone in self.phones]}\nEmail: {[email.value_of() for email in self.emails]}\nBirthday: {self.birthday.value_of()}\nStatus: {self.status.value_of()}\nAddress: {self.address.value_of()}\nNote: {self.note.value_of()}"
    
class AddressBook(UserDict):
    # Додає в словник экземпляр классу Record
    def add_person(self, person: Person) -> str:
        print(person.name.value)
        print(person.get_person_info())
        if person.name.value not in self.keys():
            self.data[person.name.value] = person
            t = str(person) + " "
            return f"{t.rstrip()}\nadd successful"
        else: return f"Contact with name {person.name.value_of()} already exist. Try add phone command for add extra phone."


        # Зберігає книгу контактів
    def save_address_book(self, adress_book):
        with open("Save_adress_book.bin", "wb") as file:
            pickle.dump(adress_book, file)


    # Відповідає за завантаження книги контактів яку зберегли минулого разу
    def load_address_book(self): 
        with open("Save_adress_book.bin", "rb") as file:
            deserialized_adress_book = pickle.load(file)
            return deserialized_adress_book


if __name__ == "__main__":
    # name = PersonName("Max")
    # phone = PersonPhoneNumbers("0591234545")
    # email = PersonEmailAddress("max.kriv@gmail.com") # "max.kriv@gmail.com"
    # birthday = PersonBirthday("31.01.1999")
    # status = PersonStatus("friend")
    # address = PersonAddress("Kyiv", "Balzaka", "77")
    # note = PersonNote("Сrazy...")


    name = PersonName("Max")
    phone = PersonPhoneNumbers("0771232323")
    email = PersonEmailAddress() # "max.kriv@gmail.com"
    birthday = PersonBirthday()
    status = PersonStatus()
    address = PersonAddress()
    note = PersonNote()


    person = Person(name, phone, email, birthday, status, address, note)

    print(person.get_person_info())


