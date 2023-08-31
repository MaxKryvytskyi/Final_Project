
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

# ======================================================================================================
# =========================================[ add ]======================================================
# ======================================================================================================

    def phone_add(self, value):
        for i, phone in enumerate(self.phones):
            if phone.value == "none":
                self.phones[i] = value
                return f"Phone додано"
        self.phones.append(value)
        return f"Phone додано"
    
    def email_add(self, value):
        for i, email in enumerate(self.emails):
            if email.value in "none":
                self.emails[i] = value
                return f"Email додано"
        self.emails.append(value)
        return f"Email додано"

    def birthday_add(self, value):
        self.birthday = value
        return f"Birthday додано"

    def status_add(self, value):
        self.status = value
        return f"Status додано"

    def address_add(self, value):
        self.address = value
        return f"Address додано"

    def note_add(self, value):
        self.note = value
        return f"Note додано"

# ======================================================================================================
# =========================================[ change ]===================================================
# ======================================================================================================

    def phone_change(self, value, new_value=None):
        if new_value:
            for i, phone in enumerate(self.phones):
                if phone.value == value.value: 
                    self.phones[i] = new_value 
                    return f"Телефон {value.value_of()} замінено"
        else:
            for i, phone in enumerate(self.phones):
                if phone.value == value.value: 
                    self.phones.remove(value)
                    return f"Телефон {value.value_of()} видалено"
    
    def email_change(self, value, new_value=None):
        if new_value:
            for i, email in enumerate(self.emails):
                if email.value == value.value: 
                    self.emails[i] = new_value 
                    return f"Електронна адреса {value.value_of()} замінена"
        else:
            for i, email in enumerate(self.emails):
                if email.value == value.value: 
                    self.emails.remove(value)
                    return f"Електронна адреса {value.value_of()} видалена"

    def name_change(self, value, new_value):
        if self.name.value == value.value:
            self.name.value = new_value.value

    def birthday_change(self, value):
        self.birthday.value = value.value
        return f"Birthday змінено"

    def status_change(self, value):
        self.status.value = value.value
        return f"Status змінено"

    def address_change(self, value):
        self.address.city = value.city
        self.address.street = value.street
        self.address.house = value.house 
        return f"Address змінено"

    def note_change(self, value):
        self.note.value = value.value
        return f"Note змінено"

# ======================================================================================================
# =========================================[ del ]======================================================
# ======================================================================================================

    def phone_del(self, value):
        for phone in self.phones:
            if phone.value == value.value: 
                self.phones.remove(phone)
                return f"Телефон {value.value_of()} видалено"
    
    def email_del(self, value):
        for email in self.emails:
            if email.value == value.value: 
                self.emails.remove(email)
                return f"Електронна адреса {value.value_of()} видалена"
    
    def birthday_del(self):
        self.birthday.value = "none"
        return f"Birthday видалено"

    def status_del(self):
        self.status.value = "none"
        return f"Status видалено"

    def address_del(self):
        self.address.city = "none"
        self.address.street = "none"
        self.address.house = "none"
        return f"Address видалено"

    def note_del(self):
        self.note.value = "none"
        return f"Note видалено"

    def editing_person_info(self):
        return f"Name: {self.name.value_of()}\nPhones: {[phone.value_of() for phone in self.phones]}\nEmail: {[email.value_of() for email in self.emails]}\nBirthday: {self.birthday.value_of()}\nStatus: {self.status.value_of()}\nAddress: {self.address.value_of()}\nNote: {self.note.value_of()}"
    
    def __str__(self):
        return "{}{}{}{}{}{}{}".format(
                                   f"Name: {self.name.value_of()}\n", 
                                   f"Phones: {[phone.value_of() for phone in self.phones]}\n", 
                                   f"Email: {[email.value_of() for email in self.emails]}\n",
                                   f"Birthday: {self.birthday.value_of()}\n",
                                   f"Status: {self.status.value_of()}\n",
                                   f"Address: {self.address.value_of()}\n",
                                   f"Note: {self.note.value_of()}")                       