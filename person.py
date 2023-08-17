
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


    def birthday_change(self, value):
        self.birthday = value
        return f"Birthday змінено"

    def status_change(self, value):
        self.status = value
        return f"Status змінено"

    def address_change(self, value):
        self.address.city = value.city
        self.address.street = value.street
        self.address.house = value.house 
        return f"Address змінено"

    def note_change(self, value):
        self.note = value
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
        self.birthday = "none"
        return f"Birthday видалено"

    def status_del(self):
        self.status = "none"
        return f"Status видалено"

    def address_del(self):
        self.address.city = "none"
        self.address.street = "none"
        self.address.house = "none"
        return f"Address видалено"

    def note_del(self):
        self.note = "none"
        return f"Note видалено"


    # def editing_phone(self, new_phone: PersonFormatterInfo, bool=False):
    #     if bool:
    #         for i in range(0, len(self.phones)-1):
    #             if self.phones[i].value_of() == new_phone.value_of():
    #                 del self.phones[i]
    #         return f"Phone Видалено"
    #     else:
    #         if "none" in [phone.value for phone in self.phones]: 
    #             self.phones[0] = new_phone
    #         else: self.phones.append(new_phone)
    #         return f"Phone змінено"

    # def editing_email(self, new_email: PersonFormatterInfo, bool=False):
    #     if bool:
    #         for i in range(0, len(self.emails)-1):
    #             if self.emails[i].value_of() == new_email.value_of():
    #                 del self.emails[i]
    #         return f"Email Видалено"
    #     else:
    #         if "none" in [email.value for email in self.emails]: 
    #             self.emails[0] = new_email
    #         else: self.emails.append(new_email)
    #         return f"Email змінено"
    

    # def editing_birthday(self, new_birthday: PersonFormatterInfo):
    #     self.birthday = new_birthday
    #     return f"Birthday змінено"
    
    # def editing_status(self, new_status: PersonFormatterInfo):
    #     self.status = new_status
    #     return f"Status змінено"

    # def editing_address(self, new_address: PersonFormatterInfo):
    #     self.address = new_address
    #     return f"Address змінено"

    # def editing_note(self, new_note: PersonFormatterInfo):
    #     self.note = new_note
    #     return f"Note змінено"

    def editing_person_info(self):
        return f"Name: {self.name.value_of()}\nPhones: {[phone.value_of() for phone in self.phones]}\nEmail: {[email.value_of() for email in self.emails]}\nBirthday: {self.birthday.value_of()}\nStatus: {self.status.value_of()}\nAddress: {self.address.value_of()}\nNote: {self.note.value_of()}"
    
    