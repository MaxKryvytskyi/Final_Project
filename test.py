import re
from my_exception import IncorrectEmailFormat

class PersonFormatterInfo:

    def value_of(self):
        raise NotImplementedError
    

class PersonPhoneNumbers(PersonFormatterInfo):
    def __init__(self, operator_code: str, phone: str) -> None:
        self.operator_code = operator_code
        self.phone = phone
    
    def value_of(self):
        return f"+38({self.operator_code}){self.phone}"
    

class PersonEmailAddress(PersonFormatterInfo):
    def __init__(self, value: str) -> None:
        self.value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value:
            if value == None: self.__value = None
            verified = str(*re.findall(r"[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", value))
            if verified: self.__value = verified
            else: raise IncorrectEmailFormat
        else: self.__value = None
    
    

    def value_of(self):
        return f"{self.email}"
    

class PersonAddress(PersonFormatterInfo):
    def __init__(self, city: str, street: str, house: str) -> None:
        self.city = city
        self.street = street
        self.house = house
    
    def value_of(self):
        return f"City: {self.city} Street: {self.street} House: {self.house}"
    

class PersonBirthday(PersonFormatterInfo):
    def __init__(self, birthday: str) -> None:
        self.birthday = birthday
    
    def value_of(self):
        return f"{self.birthday}"
    

class PersonStatus(PersonFormatterInfo):
    def __init__(self, status: str) -> None:
        self.status = status
    
    def value_of(self):
        return f"{self.status}"
    

class PersonNote(PersonFormatterInfo):
    def __init__(self, note: str) -> None:
        self.note = note
    
    def value_of(self):
        return f"{self.note}"


class Person:
    def __init__(self, name: str, phone: PersonFormatterInfo, email: PersonFormatterInfo, birthday: PersonFormatterInfo, status: PersonFormatterInfo, address: PersonFormatterInfo, note: PersonFormatterInfo) -> None:
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
        return f"Name: {self.name}\nPhones: {[phone.value_of() for phone in self.phones]}\nEmail: {[email.value_of() for email in self.emails]}\nBirthday: {self.birthday.value_of()}\nStatus: {self.status.value_of()}\nAddress: {self.address.value_of()}\nNote: {self.note.value_of()}"
    

if __name__ == "__main__":
    phone = PersonPhoneNumbers("059", "1234545")
    email = PersonEmailAddress("dwasdaw") # "max.kriv@gmail.com"
    birthday = PersonBirthday("31.01.1999")
    status = PersonStatus("Friend")
    address = PersonAddress("Kyiv", "Balzaka", "77")
    note = PersonNote("Сrazy...")


    person = Person("Max", phone, email, birthday, status, address, note)

    print(person.get_person_info())
