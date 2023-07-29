import re
from datetime import datetime


from my_exception import IncorrectDateFormat, IncorrectPhoneeFormat, IncorrectEmailFormat, IncorrectNameFormat, IncorrectStatusFormat


class Field:
    def __init__(self, value=None):
        self.__value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value: self.__value = value.capitalize()
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
    
    
class Name(Field):
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str) -> IncorrectNameFormat:
        if len(value) >= 3: self.__value = value.capitalize()
        else: raise IncorrectNameFormat


class Phone(Field):
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str) -> IncorrectPhoneeFormat:
        if value:
            correct_phone = ""
            for i in value: 
                if i in "+0123456789": correct_phone += i

            if len(correct_phone) == 13: self.__value = correct_phone # "+380123456789"
            elif len(correct_phone) == 12: self.__value = "+" + correct_phone # "380123456789"
            elif len(correct_phone) == 10: self.__value = "+38" + correct_phone # "0123456789"
            elif len(correct_phone) == 9: self.__value = "+380" + correct_phone # "123456789"
            else: raise IncorrectPhoneeFormat
        else: self.__value = "No phone"


class Birthday(Field):
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str) -> IncorrectDateFormat:
        if value: 
            if not type(value) == datetime: birthday = datetime.strptime(value, r'%d-%m-%Y')
            else: birthday = value
            if type(birthday) == datetime: self.__value = birthday 
            else: raise IncorrectDateFormat
        else: self.__value = None


class Email(Field): 
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str) -> IncorrectEmailFormat:
        if value:
            if value == None: self.__value = None
            verified = str(*re.findall(r"[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", value))
            if verified: self.__value = verified
            else: raise IncorrectEmailFormat
        else: self.__value = None


class Status(Field):
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str) -> IncorrectStatusFormat:
        if value:
            if value == None or value.lower() == "work" or value.lower() == "friends" or value.lower() == "family": self.__value = value.capitalize() if value else None
            else: raise IncorrectStatusFormat
        else: self.__value = None

    
class Address(Field):
    def __init__(self, city=None, street=None, country=None):
        self._city_value = city.capitalize() if city else None
        self._street_value = street.capitalize() if street else None
        self._country_value = country.capitalize() if country else None


    def __str__(self):
        return f"City: {self._city_value}, Street: {self._street_value}, Country: {self._country_value}"
    

