from fields import Name, Phone, Birthday, Email, Address, Status
from my_exception import IncorrectDateFormat, IncorrectPhoneeFormat, IncorrectEmailFormat, IncorrectNameFormat, IncorrectStatusFormat, IncorrectAddressFormat, IncorrectBirthdayFormat
from log import log
from datetime import datetime


class Record:
    def __init__(self, name:Name, phone: Phone=None, birthday: Birthday=None, email: Email=None, status: Status=None, address: Address=None) -> None:
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.email = email
        self.status = status 
        self.address = address 
        if birthday: self.add_to_birthday(birthday)
        if phone: self.phones.append(phone)

# ======================================================================================================
# =========================================[ add ]======================================================
# ======================================================================================================

    def add_phone(self, phones:Phone) -> str:
        if len(self.phones) < 9:
            if phones not in self.phones:
                self.phones.append(phones)
                return log(f"Phone {phones} add to contact {self.name}", "[Bot's answer] ")
            return log(f"The contact {self.name} already has the phone {phones}", "[Bot's answer] ")
        else: return log(f"The limit of phones is 9", "[Bot's answer] ")
    
    def add_to_birthday(self, birthday:Birthday):
        self.birthday = birthday

    def add_email(self, email:Email) -> None: 
        self.email = email

    def add_status(self, status:Status) -> None: 
        self.status = status

    def add_address(self, address:Address) -> None: 
        self.address = address

# ======================================================================================================
# =========================================[ remove ]===================================================
# ======================================================================================================

    def remove_phone(self, phones:Phone) -> str:
        if len(self.phones) == 0: return log("This contact has no phone numbers saved", "[Bot's answer] ")
        for n in self.phones:
            if n.value == phones.value: 
                self.phones.remove(n)
                return phones

    def remove_birthday(self, birthday:Birthday) -> None:
        # birthday = datetime.strptime(birthday1, r'%d-%m-%Y')
        if self.birthday.value == birthday.value: self.birthday = None

    def remove_email(self, email:Email) -> None: 
        if self.email.value == email.value: self.email = None

    def remove_status(self, status:Status) -> None: 
        if self.status.value == status.value: self.status = None

    def remove_address(self) -> None: 
        self.address = None

# ======================================================================================================
# =========================================[ change ]===================================================
# ======================================================================================================

    def change_name(self, name:Name, new_name:Name) -> None | IncorrectNameFormat: 
        if self.name.value == name.value: self.name = new_name
        else: raise IncorrectNameFormat

    def change_phone(self, old_phone:Phone, new_phone:Phone) -> str:
        for phones in self.phones:
            if str(old_phone) == str(phones):
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                return log(f"Phone {old_phone} change to {new_phone} for {self.name} contact ", "[Bot's answer] ")
        return log(f"Phone {old_phone} for contact {self.name} doesn`t exist", "[Bot's answer] ")

    def change_birthday(self, birthday:Birthday, new_birthday:Birthday) -> None | IncorrectBirthdayFormat:
        if self.birthday.value == birthday.value: self.birthday = new_birthday
        else: raise IncorrectBirthdayFormat

    def change_email(self, email:Email, new_email:Email) -> None | IncorrectEmailFormat: 
        if self.email.value == email.value: self.email = new_email
        else: raise IncorrectEmailFormat

    def change_status(self, status:Status, new_status:Status) -> None | IncorrectStatusFormat: 
        if self.status.value == status.value: self.status = new_status
        else: raise IncorrectStatusFormat

    def change_address(self, new_address:Address) -> None | IncorrectAddressFormat: 
        if new_address:
            if new_address._city_value:
                self.address._city_value = new_address._city_value
            if new_address._street_value:
                self.address._street_value = new_address._street_value
            if new_address._country_value:
                self.address._country_value = new_address._country_value
        else: raise IncorrectAddressFormat

# ======================================================================================================
# =========================================[ other ]====================================================
# ======================================================================================================

    # Відмаловує телефони певного контакту 
    def phone_print(self, name: Name, phones: Phone) -> str:
        result = ""
        
        dict_phone = {"Phone 1" : "", "Phone 2" : "", "Phone 3" : "", 
                      "Phone 4" : "", "Phone 5" : "", "Phone 6" : "", 
                      "Phone 7" : "", "Phone 8" : "", "Phone 9" : ""}

        for n, v in enumerate(phones): dict_phone[f"Phone {n+1}"] = v
        log([x for x in dict_phone.values() if x != "" ] )

        result += " {:^90}".format(" "*31 + "_"*30 + " "*29) + "\n"
        result += "{:<31}|{:^30}|{:>30}".format("", f"{name} Phones","") + "\n"
        result += " {:<90}".format(" "*30 + "|" + "_"*30 + "|" + " "*29) + "\n"

        if len(phones) > 0:
            result += " {:^91}".format("_"*91) + "\n"
            result += "|{:^30}|{:^30}|{:^29}|".format("Phone 1", f"Phone 2","Phone 3") + "\n"
            result += "|{:^30}|{:^30}|{:^29}|".format(str(dict_phone["Phone 1"]), str(dict_phone["Phone 2"]), str(dict_phone["Phone 3"])) + "\n"
            result += "|{:<30}|{:^30}|{:>28}|".format("_"*30, "_"*30, "_"*29) + "\n"

        if len(phones) > 3:
            result += " {:^91}".format("_"*91) + "\n"
            result += "|{:^30}|{:^30}|{:^29}|".format("Phone 4", f"Phone 5", "Phone 6") + "\n"
            result += "|{:^30}|{:^30}|{:^29}|".format(str(dict_phone["Phone 4"]), str(dict_phone["Phone 5"]), str(dict_phone["Phone 6"])) + "\n"
            result += "|{:<30}|{:^30}|{:>28}|".format("_"*30, "_"*30, "_"*29) + "\n"

        if len(phones) > 6:
            result += " {:^91}".format("_"*91) + "\n"
            result += "|{:^30}|{:^30}|{:^29}|".format("Phone 7", f"Phone 8","Phone 9") + "\n"
            result += "|{:^30}|{:^30}|{:^29}|".format(str(dict_phone["Phone 7"]), str(dict_phone["Phone 8"]), str(dict_phone["Phone 9"])) + "\n"
            result += "|{:<30}|{:^30}|{:>28}|".format("_"*30, "_"*30, "_"*29) + "\n"

        if len(phones) != 0: return f"{result}"
        else: return log(f"No phone number added to {name} contact yet ", "[Bot's answer] ")

    # Виводить залишок до дня народження певної людини 
    def days_to_birthday(self) -> str|None:
        try:
            date_birthday = self.birthday.value
        except AttributeError: return None
        current_datetime = datetime.now()
        new_date = date_birthday.replace(year=current_datetime.year)
        days_birthday = new_date - current_datetime
        if days_birthday.days >= 0: return log(f"{days_birthday.days} days", "[Bot's answer] ") 
        else:
            date = date_birthday.replace(year=current_datetime.year+1)
            days_birthday = date - current_datetime
            return log(f"{days_birthday.days} days", "[Bot's answer] ") 

    def __str__(self):
        return "{}{}{}{}{}{}".format(
                                   f"Name: {self.name}\n", 
                                   f'Phone: {", ".join([str(p) for p in self.phones]) if self.phones else "No phone"}\n', 
                                   'Birthday: ' + str(self.birthday.value.strftime("%d-%m-%Y")) + "\n" if self.birthday is not None else "Birthday: No birthday date\n", 
                                   'Email: ' + str(self.email.value) + "\n" if self.email is not None else "Email: No email\n", 
                                   'Status: ' + str(self.status.value) if self.status is not None else "Status: No status\n",
                                   'Address: ' + str(self.address) + "\n" if self.address is not None else 'Address: No address')
                                   