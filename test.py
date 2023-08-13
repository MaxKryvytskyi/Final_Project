import re
from my_exception import ExceptionIncorrectFormat
from datetime import datetime

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
    def __init__(self, value: str):
        self.__value = None
        self.value = value

    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value:
            if not value.isdigit():
                raise ExceptionIncorrectFormat(f"Телефон {value} має складатися тільки з літер")
            if len(value) == 10: self.__value = value # "012 3456789"
            else: raise ExceptionIncorrectFormat(f"Не правильний формат телефону {value} очікуєтся 0500000000")
        else: self.__value = "none"
    
    def value_of(self):
        return f"+38{self.value}"
    

class PersonEmailAddress(PersonFormatterInfo):
    def __init__(self, value: str):
        self.value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value:
            if value == None: 
                self.__value = "none"
            verified = str(*re.findall(r"[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", value))
            if verified: 
                self.__value = verified
            else: 
                raise ExceptionIncorrectFormat(f"Не правильний формат email {value} очікувалося m.k@gmail.com")
        else: self.__value = "none"
    
    def value_of(self):
        return f"{self.value}"


class PersonStatus(PersonFormatterInfo):
    def __init__(self, value: str):
        self.value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value:
            if value.lower() in ["work", "family", "friend"]:
                self.__value = value
        else: self.__value = "none"
    
    def value_of(self):
        return f"{self.value.capitalize()}"

class PersonAddress(PersonFormatterInfo):
    def __init__(self, city: str, street: str, house: str):
        self.city = city
        self.street = street
        self.house = house
    
    def value_of(self):
        return f"City: {self.city if self.city != 'none' else ''}, Street: {self.street if self.street != 'none' else ''}, House: {self.house if self.house != 'none' else ''}."
    

class PersonBirthday(PersonFormatterInfo):
    def __init__(self, value: str):
        self.value = None
        self.value = value
    
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value: 
            birthday = datetime.strptime(value, r'%d.%m.%Y')
            if birthday: 
                self.__value = value
            else: raise ExceptionIncorrectFormat(f"Не правильний формат дати {value} очікувалося день.місяць.рік")
        else: self.__value = "none"


    def value_of(self):
        return f"{self.value}"
    


    

class PersonNote(PersonFormatterInfo):
    def __init__(self, note: str):
        self.note = note
    
    def value_of(self):
        return f"{self.note}"

class Person:
    def __init__(self, name: PersonFormatterInfo, phone: PersonFormatterInfo, email: PersonFormatterInfo, birthday: PersonFormatterInfo, status: PersonFormatterInfo, address: PersonFormatterInfo, note: PersonFormatterInfo) -> None:
        self.name = name
        self.phones = []
        self.emails = [] 
        self.birthday = birthday
        self.status = status
        self.address = address
        self.note = note
        self.phones.append(phone)
        self.emails.append(email)

    def get_person_info(self):
        return f"Name: {self.name.value_of()}\nPhones: {[phone.value_of() for phone in self.phones]}\nEmail: {[email.value_of() for email in self.emails]}\nBirthday: {self.birthday.value_of()}\nStatus: {self.status.value_of()}\nAddress: {self.address.value_of()}\nNote: {self.note.value_of()}"
    

if __name__ == "__main__":
    name = PersonName("Max")
    phone = PersonPhoneNumbers("0591234545")
    email = PersonEmailAddress("max.kriv@gmail.com") # "max.kriv@gmail.com"
    birthday = PersonBirthday("31.01.1999")
    status = PersonStatus("friend")
    address = PersonAddress("Kyiv", "Balzaka", "77")
    note = PersonNote("Сrazy...")


    person = Person(name, phone, email, birthday, status, address, note)

    print(person.get_person_info())


