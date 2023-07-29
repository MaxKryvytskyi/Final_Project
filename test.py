import re

from log import log
from fields import Name, Phone, Birthday, Email, Address, Status, Note
from record import Record
from address_book import AddressBook
from my_exception import IncorrectDateFormat, IncorrectPhoneeFormat, IncorrectEmailFormat, IncorrectNameFormat, IncorrectStatusFormat

def add(*args):
    DEBUG = False
    try:
        name = Name(input("Name ---> ")) if DEBUG else Name("ax")
    except IncorrectNameFormat:
        name = Name(input("Name ---> ")) if DEBUG else Name("max") 
    try:
        phone = Phone(input("Phone---> ")) if DEBUG else Phone("54545") 
    except IncorrectPhoneeFormat:
        phone = Phone(input("Phone---> ")) if DEBUG else Phone("+380993454545") 
    try:
        email = Email(input("Email ---> ")) if DEBUG else Email("gmail.com") 
    except IncorrectEmailFormat:
        email = Email(input("Email ---> ")) if DEBUG else Email("m.kriv@gmail.com") 

        city = input("City ---> ") if DEBUG else "Kiev"
        street = input("Street ---> ") if DEBUG else "Vatutina" 
        country = input("Country ---> ") if DEBUG else "Ua"
        address = Address(city, street, country)
    try:
        status = Status(input("Status --->")) if DEBUG else Status("ork")
    except IncorrectStatusFormat:
        status = Status(input("Status --->")) if DEBUG else Status("work")
    try:
        birthday = Birthday(input("Birthday --->")) if DEBUG else Birthday("-12-2000")
    except IncorrectDateFormat:
        birthday = Birthday(input("Birthday --->")) if DEBUG else Birthday("12-12-2000")  


    
    rec = Record(name, phone, birthday, email, address, status)
    ad.add_record(rec)
    print(ad["Max"])
    print(ad)
 




if __name__ == "__main__":
    ad = AddressBook()
    add()

