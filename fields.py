import re
from datetime import datetime
from abc import ABC, abstractmethod
from my_exception import ExceptionIncorrectFormat


class PersonFormatterInfo(ABC):

    @abstractmethod
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
            if len(value) == 12: self.__value = value # "380 12 345 67 89"
            else: raise ExceptionIncorrectFormat(f"Не правильний формат телефону {value} очікуєтся 0500000000")
        else: self.__value = "none"
    
    def value_of(self):
        return f"{self.value if self.value.lower() != 'none' else ''}"
    

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
            if value.lower() == "none": 
                self.__value = "none"
            verified = str(*re.findall(r"[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", value))
            if verified: 
                self.__value = verified
            else: 
                raise ExceptionIncorrectFormat(f"Не правильний формат email \"{value}\" очікувалося m.k@gmail.com")
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
        city = self.city if self.city.lower() != 'none' else ''
        street = self.street if self.street.lower() != 'none' else ''
        house = self.house if self.house.lower() != 'none' else ''
        if city != '': city = f"City: {city + ','}"
        if street != '': street = f"Street: {street + ','}"
        if house != '': house = f"House: {house + '.'}"
        return f"{city} {street} {house}"
    

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
    
    def days_to_birthday(self) -> str|None:
        try:
            date_birthday = datetime.strptime(self.value, "%d.%m.%Y")
        except AttributeError: return None
        current_datetime = datetime.now()
        new_date = date_birthday.replace(year=current_datetime.year)
        days_birthday = new_date - current_datetime
        if days_birthday.days >= 0: return f"{days_birthday.days} days"
        else:
            date = date_birthday.replace(year=current_datetime.year + 1)
            days_birthday = date - current_datetime
            return f"{days_birthday.days} days"

    
class PersonNote(PersonFormatterInfo):
    def __init__(self, value: str="None"):
        self.value = value
    
    def value_of(self):
        return f"{self.value if self.value.lower() != 'none' else ''}"
    
