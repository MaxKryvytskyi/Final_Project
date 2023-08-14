
from fields import PersonFormatterInfo


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

    def editing_phone(self, new_phone: PersonFormatterInfo):
        if "none" in [phone.value for phone in self.phones]: 
            self.phones[0] = new_phone
        else: self.phones.append(new_phone)
        return f"Phone змінено"

    def editing_email(self, new_email: PersonFormatterInfo):
        if "none" in [email.value for email in self.emails]: 
            self.emails[0] = new_email
        else: self.emails.append(new_email)
        return f"Email змінено"
    

    def editing_birthday(self, new_birthday: PersonFormatterInfo):
        self.birthday = new_birthday
        return f"Birthday змінено"
    
    def editing_status(self, new_status: PersonFormatterInfo):
        self.status = new_status
        return f"Status змінено"

    def editing_address(self, new_address: PersonFormatterInfo):
        self.address = new_address
        return f"Address змінено"

    def editing_note(self, new_note: PersonFormatterInfo):
        self.note = new_note
        return f"Note змінено"

    def editing_person_info(self):
        return f"Name: {self.name.value_of()}\nPhones: {[phone.value_of() for phone in self.phones]}\nEmail: {[email.value_of() for email in self.emails]}\nBirthday: {self.birthday.value_of()}\nStatus: {self.status.value_of()}\nAddress: {self.address.value_of()}\nNote: {self.note.value_of()}"
    
    