import re
from datetime import datetime


from my_exception import ExceptionIncorrectFormat


class Field:
    def __init__(self, value=None):
        self.__value = None
        self.value = value
        
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value: self.__value = value
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
    
    
class Name(Field):
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if len(value) >= 3: self.__value = value.capitalize()
        else: raise ExceptionIncorrectFormat(f"Ім'я \"{value}\" занадто кототке потрібно минимум 3 символи")


class Phone(Field):
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
        else: self.__value = "No phone"


class Birthday(Field):
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value: 
            if not type(value) == datetime: birthday = datetime.strptime(value, r'%d-%m-%Y')
            else: birthday = value
            if type(birthday) == datetime: self.__value = birthday 
            else: raise ExceptionIncorrectFormat(f"Не правильний формат дати {value} очікувалося день.місяць.рік")
        else: self.__value = None


class Email(Field): 
    @property
    def value(self): 
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value:
            if value == None: 
                self.__value = "None"
            verified = str(*re.findall(r"[a-zA-Z]{1}[a-zA-Z0-9._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}", value))
            if verified: 
                self.__value = verified
            else: 
                raise ExceptionIncorrectFormat(f"Не правильний формат email {value} очікувалося m.k@gmail.com")
        else: self.__value = "None"

    
class Address(Field):
    pass